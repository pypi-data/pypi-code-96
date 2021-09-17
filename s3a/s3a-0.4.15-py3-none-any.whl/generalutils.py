import html
import warnings
from collections import defaultdict
from functools import wraps
from pathlib import Path
from typing import Callable, Tuple, Union, Sequence, List, Collection, Any

import cv2 as cv
import numpy as np
import pandas as pd
import pyqtgraph as pg
from skimage import io
from skimage import transform
from skimage.exposure import exposure

from utilitys import PrjParam, fns, ProcessStage
# Needs to be visible outside this file
# noinspection PyUnresolvedReferences
from utilitys.fns import hierarchicalUpdate
from utilitys.typeoverloads import FilePath
from .structures import TwoDArr, XYVertices, ComplexXYVertices, NChanImg, BlackWhiteImg


def stackedVertsPlusConnections(vertList: ComplexXYVertices) -> Tuple[XYVertices, np.ndarray]:
  """
  Utility for concatenating all vertices within a list while recording where separations
  occurred
  """
  allVerts = [np.zeros((0,2))]
  separationIdxs = []
  idxOffset = 0
  for curVerts in vertList:
    allVerts.append(curVerts)
    vertsLen = len(curVerts)
    if vertsLen == 0: continue
    # Close the current shape
    allVerts.append(curVerts[0,:])
    separationIdxs.append(idxOffset + vertsLen)
    idxOffset += vertsLen + 1
  # Take away last separator if it exists
  if len(separationIdxs) > 0:
    separationIdxs.pop()
  allVerts = np.vstack(allVerts)
  isfinite = np.ones(len(allVerts), bool)
  isfinite[separationIdxs] = False
  return XYVertices(allVerts, dtype=float), isfinite
  #return XYVertices(dtype=float)

def getClippedBbox(arrShape: tuple, bbox: TwoDArr, margin: int):
  """
  Given a bounding box and margin, create a clipped bounding box that does not extend
  past any dimension size from arrShape

  Parameters
  ----------
  arrShape :    2-element tuple
     Refrence array dimensions

  bbox     :    2x2 array
     [minX minY; maxX maxY] bounding box coordinates

  margin   :    int
     Offset from bounding box coords. This will not fully be added to the bounding box
     if the new margin causes coordinates to fall off either end of the reference array shape.
  """
  bbox = bbox.astype(int)
  bbox[0] -= margin
  # Add extra 1 since python slicing stops before last index
  bbox[1] += margin+1
  arrShape = arrShape[:2]
  return np.clip(bbox, 0, arrShape[::-1])

def coerceDfTypes(dataframe: pd.DataFrame, constParams: Collection[PrjParam]=None):
  """
  Pandas currently has a bug where datatypes are not preserved after update operations.
  Current workaround is to coerce all types to their original values after each operation
  """
  if constParams is None:
    constParams = dataframe.columns
  for field in constParams:
    try:
      dataframe[field] = dataframe[field].astype(type(field.value))
    except TypeError:
      # Coercion isn't possible, nothing to do here
      pass
  return dataframe

def largestList(verts: List[XYVertices]) -> XYVertices:
  maxLenList = []
  for vertList in verts:
    if len(vertList) > len(maxLenList): maxLenList = vertList
  # for vertList in newVerts:
  # vertList += cropOffset[0:2]
  return XYVertices(maxLenList)

def augmentException(ex: Exception, prependedMsg: str):
  exMsg = str(ex)
  ex.args = (prependedMsg + exMsg,)

def lower_NoSpaces(name: str):
  return name.replace(' ', '').lower()

def safeCallFuncList(fnNames: Collection[str], funcLst: List[Callable],
                     fnArgs: List[Sequence]=None):
  errs = []
  rets = []
  if fnArgs is None:
    fnArgs = [()]*len(fnNames)
  for key, fn, args in zip(fnNames, funcLst, fnArgs):
    curRet, curErr = safeCallFunc(key, fn, *args)
    rets.append(curRet)
    if curErr: errs.append(curErr)
  return rets, errs

def safeCallFunc(fnName: str, func: Callable, *fnArgs):
  ret = err = None
  try:
    ret = func(*fnArgs)
  except Exception as ex:
    err = f'{fnName}: {ex}'
  return ret, err

def _maybeBgrToRgb(image: np.ndarray):
  """Treats 3/4-channel images as BGR/BGRA for opencv saving/reading"""
  if image.ndim > 2:
    # if image.shape[0] == 1:
    #   image = image[...,0]
    if image.shape[2] >= 3:
      lastAx = np.arange(image.shape[2], dtype='int')
      # Swap B & R
      lastAx[[0,2]] = [2,0]
      image = image[...,lastAx]
  return image

def cvImsave_rgb(fname: FilePath, image: np.ndarray, *args, errOk=False, **kwargs):
  image = _maybeBgrToRgb(image)
  try:
    cv.imwrite(str(fname), image, *args, **kwargs)
  except cv.error:
    if not errOk:
      raise
    # Dtype incompatible
    io.imsave(fname, image)

def cvImread_rgb(fname: FilePath, *args, **kwargs):
  image = cv.imread(str(fname), *args, **kwargs)
  return _maybeBgrToRgb(image)

def tryCvResize(image: NChanImg, newSize: Union[tuple, float],
                asRatio=True, interp=cv.INTER_CUBIC):
  """
  Uses cv.resize where posisble, but if dtypes prevent this, it falls back to skimage.transform.rescale/resize

  :param image: Image to resize
  :param newSize: Either ratio to scale each axis or new image size (x, y -- not row, col)
  :param asRatio: Whether to interpret `newSize` as a ratio or new image dimensions
  :param interp: Interpolation to use, if cv.resize is available for the given dtype
  """
  if asRatio:
    if not isinstance(newSize, tuple):
      newSize = (newSize, newSize)
    args = dict(dsize=(0,0), fx=newSize[0], fy=newSize[1])
  else:
    args = dict(dsize=newSize)
  try:
    image = cv.resize(image, **args, interpolation=interp)
  except (TypeError, cv.error):
    oldRange = (image.min(), image.max())
    if asRatio:
      rescaled = transform.rescale(image, newSize, multichannel=image.ndim > 2)
    else:
      rescaled = transform.resize(image, newSize[::-1])
    image = exposure.rescale_intensity(rescaled, out_range=oldRange).astype(image.dtype)
  return image



def cornersToFullBoundary(cornerVerts: Union[XYVertices, ComplexXYVertices], sizeLimit: float=np.inf,
                          fillShape: Tuple[int]=None, stackResult=True) -> Union[XYVertices, ComplexXYVertices]:
  """
  From a list of corner vertices, returns a list with one vertex for every border pixel.
  Example:
  >>> cornerVerts = XYVertices([[0,0], [100,0], [100,100],[0,100]])
  >>> cornersToFullBoundary(cornerVerts)
  # [[0,0], [1,0], ..., [100,0], [100,1], ..., [100,100], ..., ..., [0,100]]
  :param cornerVerts: Corners of the represented polygon
  :param sizeLimit: The largest number of pixels from the enclosed area allowed before the full boundary is no
  longer returned. For instance:
    >>> cornerVerts = XYVertices([[0,0], [1000,0], [1000,1000],[0,1000]])
    >>> cornersToFullBoundary(cornerVerts, 10e5)
    will *NOT* return all boundary vertices, since the enclosed area (10e6) is larger than sizeLimit.
  :param fillShape: Size of mask to create. Useful if verts may extend beyond image dimensions
    and should be truncated. If None, no truncation will occur except for negative verts.
  :param stackResult: Whether the result should be ComplexXYVertices (if stackResult is False)
    or a stacked list of exterior verts (if stackResult is True)
  :return: List with one vertex for every border pixel, unless *sizeLimit* is violated.
  """
  if isinstance(cornerVerts, XYVertices):
    cornerVerts = ComplexXYVertices([cornerVerts])
  if fillShape is not None:
    fillShape = tuple(fillShape)
  filledMask = cornerVerts.toMask(fillShape, warnIfTooSmall=False)
  cornerVerts = ComplexXYVertices.fromBinaryMask(filledMask, simplifyVerts=False)
  if not stackResult:
    return cornerVerts
  cornerVerts = cornerVerts.filledVerts().stack()
  numCornerVerts = len(cornerVerts)
  if numCornerVerts > sizeLimit:
    spacingPerSamp = int(numCornerVerts/sizeLimit)
    cornerVerts = cornerVerts[::spacingPerSamp]
  return cornerVerts


def getCroppedImg(image: NChanImg, verts: np.ndarray, margin=0, *otherBboxes: np.ndarray,
                  coordsAsSlices=False, returnCoords=True) -> (np.ndarray, np.ndarray):
  """
  Crops an image according to the specified vertices such that the returned image does not extend
  past vertices plus margin (including other bboxes if specified). All bboxes and output coords
  are of the form [[xmin, ymin], [xmax, ymax]]. Slices are (row slices, col slices) if `coordsAsSlices`
  is specified.
  """
  verts = np.vstack(verts)
  img_np = image
  compCoords = np.vstack([verts.min(0), verts.max(0)])
  if len(otherBboxes) > 0:
    for dim in range(2):
      for ii, cmpFunc in zip(range(2), [min, max]):
        otherCmpVals = [curBbox[ii, dim] for curBbox in otherBboxes]
        compCoords[ii,dim] = cmpFunc(compCoords[ii,dim], *otherCmpVals)
  compCoords = getClippedBbox(img_np.shape, compCoords, margin)
  coordSlices = (slice(compCoords[0,1], compCoords[1,1]),
                 slice(compCoords[0,0],compCoords[1,0]))
  # Verts are x-y, index into image with row-col
  indexer = coordSlices
  if image.ndim > 2:
    indexer += (slice(None),)
  croppedImg = image[indexer]
  if not returnCoords:
    return croppedImg
  if coordsAsSlices:
    return croppedImg, coordSlices
  else:
    return croppedImg, compCoords

def imgCornerVertices(img: NChanImg=None) -> XYVertices:
  """Returns [x,y] vertices for each corner of the input image"""
  if img is None:
    return XYVertices()
  fullImShape_xy = img.shape[:2][::-1]
  return XYVertices([[0,                   0],
              [0,                   fullImShape_xy[1]-1],
              [fullImShape_xy[0]-1, fullImShape_xy[1]-1],
              [fullImShape_xy[0]-1, 0]
              ])

def resize_pad(img: NChanImg,
               shape: Sequence[int],
               allowReorient=False,
               keepAspectRatio=True,
               interpolation=cv.INTER_NEAREST,
               padVal=0,
               returnStats=False):
  """
  Resizes image to the requested size using the specified interpolation method.
  :param img: Image to resize
  :param shape: New shape for image
  :param allowReorient: If *True*, the image can be rotated 90 degrees if it results in less padding to reach
    the desired shape
  :param keepAspectRatio: If *False*, the image will be stretched instead of padded on the lacking dimension.
    The portion of the image which couldn't be resized fully is padded with a constant value of `padVal`.
    For instance, if the original image is 5x10 and the requested new size is 10x15, then after resizing
    the image will be 7x15 to preserve aspect ratio. 2 pixels of padding will be added on the left and
    1 pixel of padding will be added on the right so the final output is 10x15.
  :param padVal: Value to pad dimension that couldn't be fully resized
  :param interpolation: Interpolation method to use during resizing
  :param returnStats: If *True*, the return value of this function will be a tuple where the first argument
    is the resized/padded image and the second is a dict of stats. Keys are:

      - 'top'/'left'/'bottom'/'right': Padding added to top, left, ... sides of the image
      - 'reoriented': Boolean, whether the image was rotated
  """
  initialShape = img.shape[:2]
  shape = np.asarray(shape)
  ratios = shape / initialShape
  rotated = False
  if allowReorient:
    # Choose whichever orientation leads to the closest ratio to the original size
    tmpRatios = shape / img.shape[:2][::-1]
    if np.abs(1 - tmpRatios[0] / tmpRatios[1]) < np.abs(1 - ratios[0] / ratios[1]):
      img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
      ratios = tmpRatios
      rotated = True

  # Dummy pad values, will be updated if padding actually occurs
  top, left, bottom, right = [0] * 4
  stats = dict(initialShape=initialShape, rotated=rotated, interpolation=interpolation)
  if not keepAspectRatio:
    paddedImg = cv.resize(img, tuple(shape[::-1]), interpolation=interpolation)
    if returnStats:
      return paddedImg, stats
    return paddedImg

  ratio = ratios.min()
  paddedImg = cv.resize(img, (0, 0), fx=ratio, fy=ratio, interpolation=interpolation)
  padding = (shape - paddedImg.shape[:2])

  if (padding > 0).any():
    top, left = map(int, padding//2)
    bottom, right = map(int, padding - padding//2)
    paddedImg = cv.copyMakeBorder(paddedImg, top, bottom, left, right, cv.BORDER_CONSTANT, value=padVal)
  if returnStats:
    # No pre-resize padding added
    stats.update(postResizePadding=(top, bottom, left, right))
    return paddedImg, stats
  return paddedImg

def showMaskDiff(oldMask: BlackWhiteImg, newMask: BlackWhiteImg):
  infoMask = np.tile(oldMask[...,None].astype('uint8')*255, (1,1,3))
  # Was there, now it's not -- color red
  infoMask[oldMask & ~newMask,:] = [255,0,0]
  # Wasn't there, now it is -- color green
  infoMask[~oldMask & newMask,:] = [0,255,0]
  return infoMask

# Poor man's LRU dict, since I don't yet feel like including another pypi dependency
class MaxSizeDict(dict):
  def __init__(self, *args, maxsize:int=np.inf, **kwargs):
    super().__init__(*args, **kwargs)
    self.maxsize = maxsize

  def __setitem__(self, key, value):
    if len(self) >= self.maxsize:
      # Evict oldest inserted entry
      self.pop(next(iter(self.keys())))
    super().__setitem__(key, value)

def _getPtAngles(pts):
  midpt = np.mean(pts, 0)
  relPosPts = (pts - midpt).view(np.ndarray)
  return np.arctan2(*relPosPts.T[::-1])

def orderContourPts(pts: XYVertices, ccw=True):
  """
  Only guaranteed to work for convex hulls, i.e. shapes not intersecting themselves. Orderes
  an arbitrary list of coordinates into one that works well line plotting, i.e. doesn't show
  excessive self-crossing when plotting
  """
  if len(pts) < 3:
    return pts
  angles = _getPtAngles(pts)
  ptOrder = np.argsort(angles)
  if not ccw:
    ptOrder = ptOrder[::-1]
  return pts[ptOrder]

# def movePtsTowardCenter(pts: XYVertices, dist=1):
#   if not pts.size:
#     return pts
#   angles = _getPtAngles(pts)
#   adjusts = np.column_stack([np.cos(angles), np.sin(angles)])
#   adjusts[np.abs(adjusts) < 0.01] = 0
#   # Adjust by whole steps
#   adjusts = np.sign(adjusts)*dist
#   return pts - adjusts

def symbolFromVerts(verts: Union[ComplexXYVertices, XYVertices, np.ndarray]):
  if isinstance(verts, ComplexXYVertices):
    concatRegion, isfinite = stackedVertsPlusConnections(verts)
  else:
    concatRegion, isfinite = verts, np.all(np.isfinite(verts), axis=1)
    # Qt doesn't like subclassed ndarrays
    concatRegion = concatRegion.view(np.ndarray)
  if not len(concatRegion):
    boundLoc = np.array([[0,0]])
  else:
    boundLoc = np.nanmin(concatRegion, 0, keepdims=True)
  useVerts = concatRegion - boundLoc + 0.5
  # pyqtgraph 0.12.2 errs on an empty symbol https://github.com/pyqtgraph/pyqtgraph/issues/1888
  if not len(isfinite):
    isfinite='all'
  return pg.arrayToQPath(*useVerts.T, connect=isfinite), boundLoc

# Credit: https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
def bboxIou(boxA, boxB):
  """
  determine the (x, y)-coordinates of the intersection rectangle. Both boxes are formatted
   [[xmin, ymin], [xmax, ymax]]"""
  boxA = boxA.ravel()
  boxB = boxB.ravel()
  xA = max(boxA[0], boxB[0])
  yA = max(boxA[1], boxB[1])
  xB = min(boxA[2], boxB[2])
  yB = min(boxA[3], boxB[3])
  # compute the area of intersection rectangle
  interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
  # compute the area of both the prediction and ground-truth
  # rectangles
  boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
  boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
  # compute the intersection over union by taking the intersection
  # area and dividing it by the sum of prediction + ground-truth
  # areas - the interesection area
  iou = interArea / float(boxAArea + boxBArea - interArea)
  # return the intersection over union value
  return iou

def minVertsCoord(verts: XYVertices):
  """
  Finds the coordinate in the vertices list that is closest to the origin. `verts` must
  have length > 0.
  """
  # Early exit condition
  if verts.ndim < 2:
    # One point
    return verts
  allMin = verts.min(0)
  closestPtIdx  = np.argmin(np.sum(np.abs(verts - allMin), 1))
  return verts[closestPtIdx]


# Credit: https://stackoverflow.com/a/13624858/9463643
class classproperty:

  def __init__(self, fget):
    self.fget = fget

  def __get__(self, owner_self, owner_cls):
    return self.fget(owner_cls)

def imgPathtoHtml(imgPath: FilePath, width=None):
  outStr = f'<img src="{imgPath}"'
  if width is not None:
    outStr += f' width="{width}px"'
  outStr += '>'
  return outStr

def incrStageNames(stages: Sequence[ProcessStage]):
  """
  Returns a list of names numerically incrementing where they would otherwise be duplicated. E.g. if the stage
  list was [Open, Open], this is converted to [Open, Open#2]
  """
  preExisting = defaultdict(int)
  names = []
  for stage in stages:
    name = stage.name
    if preExisting[name] > 0:
      name += f'#{preExisting[name] + 1}'
    preExisting[name] += 1
    names.append(name)
  return names

class DirectoryDict(MaxSizeDict):
  """
  Used to shim the API between file-system and programmatically generated content. If a directory is passed, files are
  read and cached when a name is passed. Otherwise, treat as a normal dict of things. For instance, a directory of
  png images can be accessed through this data structure as ddict['x.png'] which will load the image. Next time 'x.png'
  is accessed, it will be instantaneous due to caching. Similarly, `ddict` could be given an initial dict if contents
  are not directory-backed
  """
  _UNSET = object()

  def __init__(self, initData:Union[FilePath, dict, 'DirectoryDict']=None,
               readFunc: Callable[[str], Any]=None,
               allowAbsolute=False,
               **kwargs,):
    """
    :param initData: Either startup dict or backing directory path. If a DirectoryDict is passed, its attribute will
      be used instead of the value passed for allowAbsolute. Its readFunc will be used if the passed
      readFunc is *None*
    :param readFunc: Function used to read files from the directory, i.e. `io.imread`, `attemptFileLoad`, etc.
      Must accept the name of the file to read
    :param allowAbsolute: Whether to allow reading absolute paths
    :param kwargs: Passed to super constructor
    """
    if isinstance(initData, FilePath.__args__):
      self.fileDir = Path(initData)
      super().__init__(**kwargs)
    else:
      if isinstance(initData, DirectoryDict):
        readFunc = readFunc or initData.readFunc
        allowAbsolute = initData.allowAbsolute
        self.fileDir = initData.fileDir
      super().__init__(initData, **kwargs)
    self.readFunc = readFunc
    self.allowAbsolute = allowAbsolute

  def __missing__(self, key):
    key = str(key)
    exists = super().get(key, self._UNSET)
    if exists is not self._UNSET:
      return exists
    if self.fileDir is None:
      raise KeyError(f'"{key}" is not in dict and no backing file system was provided')
    pathKey = Path(key)
    isAbsolute = pathKey.is_absolute()
    if not self.allowAbsolute and isAbsolute:
      raise KeyError(f'Directory paths must be relative, received {key}')
    testPath = pathKey if isAbsolute else self.fileDir/key
    candidates = list(testPath.parent.glob(testPath.name))
    if len(candidates) != 1:
      grammar = ': ' if len(candidates) else ''
      raise KeyError(f'"{key}" corresponds to {len(candidates)} files{grammar}{", ".join(c.name for c in candidates)}')
    else:
      file = candidates[0]
      ret = self[key] = self.readFunc(file)
    return ret

  def get(self, key, default=None):
    ret = super().get(key, self._UNSET)
    if ret is self._UNSET:
      # See if directory has this data
      try:
        ret = self[key]
      except KeyError:
        return default
    return ret


def deprecateKwargs(**oldToNewNameMapping):
  def deco(func):
    @wraps(func)
    def inner(*args, **kwargs):
      usedDeprecated = set(oldToNewNameMapping) & set(kwargs)
      if usedDeprecated:
        grammar = 'is' if len(usedDeprecated) == 1 else 'are'
        replacements = {k: oldToNewNameMapping[k] for k in usedDeprecated if oldToNewNameMapping[k] is not None}
        msg = f'{", ".join(usedDeprecated)} {grammar} deprecated and will be removed in a future release.'
        if replacements:
          for orig, replace in replacements.items():
            kwargs[replace] = kwargs[orig]
            del kwargs[orig]
          msg += f' Use the following replacement guide: {replacements}'
        warnings.warn(msg, DeprecationWarning, stacklevel=3)
      return func(*args, **kwargs)
    return inner
  return deco

def _indexUsingPad(image, tblrPadding):
  """Extracts an inner portion of an image accounting for top/bottom/left/right padding tuple"""
  imshape = image.shape[:2]
  rows = slice(tblrPadding[0], imshape[0] - tblrPadding[1])
  cols = slice(tblrPadding[2], imshape[1] - tblrPadding[3])
  return image[rows, cols, ...]


def getCroppedImg_resize_pad(fullImage, coords, margin=0, returnCoords=True, padVal=np.nan, **resizeOpts):
  shape = np.array(resizeOpts.pop('shape'))
  min_ = np.min(coords, 0)
  max_ = np.max(coords, 0)
  # x-y to row-col
  span = (max_ - min_ + 1)[::-1]
  initialShape = tuple(map(int, span))

  ratios = shape / span
  needsRotate = False
  if resizeOpts.get('allowReorient'):
    # Choose whichever orientation leads to the closest ratio to the original size
    tmpRatios = shape / span[::-1]
    if np.abs(1 - tmpRatios.min()/tmpRatios.max()) < np.abs(1 - ratios.min()/ratios.max()):
      ratios = tmpRatios
      span = span[::-1]
      needsRotate = True
  padAx = np.argmax(ratios)
  padAmt = (ratios.max()/ratios.min()-1)*span[padAx]
  # left/right could be top/bottom, but the concept is the same either way
  leftPad = int(np.ceil(padAmt/2))
  rightPad = int(padAmt.round() - leftPad)
  # Correction happens relative to xy unless the image will be rotated, in which case x will be height
  if not needsRotate:
    padAx = 1 - padAx
  if np.isnan(padVal) and resizeOpts.get('keepAspectRatio', True):
    # Non-nan value means user wants constant padding, not padding that came from image background
    min_[padAx] -= leftPad
    max_[padAx] += rightPad
    # Extra padding means the aspect ratio should be 1, so no need to account for this in `resize_pad`
    resizeOpts.update(keepAspectRatio=False)
  else:
    # Zero out to avoid false accounting when updating `stats` below
    leftPad = rightPad = 0
  img, bounds = getCroppedImg(fullImage, np.vstack([min_, max_]), margin)
  # If padding caused min or max to go beyond image borders, make sure to spoof this with yet another padding
  extraPadding = _computeEdgePadding(bounds, fullImage.shape[:2], max_, min_)
  if any(extraPadding):
    img = cv.copyMakeBorder(img, *extraPadding, cv.BORDER_CONSTANT, value=0)
  # Due to custom padding, resized image can at most be off by one pixel. This is fine to allow a bit of stretch
  oldReturnStats = resizeOpts.pop('returnStats', False)
  img, stats = resize_pad(img, shape, **resizeOpts, padVal=padVal, returnStats=True)
  # Since padding might have occured at this stack level, make sure the original width and height values are correct
  # Also make sure the raw image size is correct
  stats['preResizePadding'] = (0, 0, leftPad, rightPad) if padAx == 0 else (leftPad, rightPad, 0, 0)
  stats['initialShape'] = initialShape

  ret = [img]
  if returnCoords:
    ret.append(bounds)
  if oldReturnStats:
    ret.append(stats)
  if len(ret) == 1:
    return ret[0]
  return tuple(ret)

def inverseResize_pad(image, stats):
  """
  If `image` and `stats` are the result of a `resize_pad` operation with ``returnStats=True``, this will
  return a version of `image` that is normalized back to the unresized, unpadded state.
  """
  NO_PADDING = [0]*4
  image = _indexUsingPad(image, stats.get('postResizePadding', NO_PADDING))

  # If the image was rotated, the initial shape should be altered to account for this during pad math
  initialShape = stats['initialShape']
  if stats.get('rotated'):
    initialShape = initialShape[::-1]

  prepad = stats.get('preResizePadding', NO_PADDING)
  preresizeShape = np.array(initialShape, dtype=int) + [sum(prepad[:2]), sum(prepad[2:])]
  image = cv.resize(image, tuple(preresizeShape[::-1].astype(int)), interpolation=stats.get('interpolation'))

  image = _indexUsingPad(image, prepad)
  if stats['rotated']:
    image = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
  return image


def _computeEdgePadding(bounds, fullImageShape, maxCoords, min_):
  # Turn shape into x-y
  fullImageShape = fullImageShape[::-1]
  needsMinPad = min_ < 0
  leftTopPad = np.array([0, 0])
  minPad = -min_[needsMinPad]
  leftTopPad[needsMinPad] = minPad
  bounds[0, needsMinPad] = minPad

  needsMaxPad = maxCoords > fullImageShape
  rightBotPad = np.array([0, 0])
  maxPad = (maxCoords - fullImageShape)[needsMaxPad]
  rightBotPad[needsMaxPad] = maxPad
  bounds[1, needsMaxPad] += maxPad
  # Turn into order expected by cv2 -- top, bot, left, right
  extraPadding = [int(pad) for pad in [leftTopPad[1], rightBotPad[1], leftTopPad[0], rightBotPad[0]]]
  return extraPadding

def pd_iterdict(df: pd.DataFrame, index=False):
  """
  pandas to_dict() keeps all rows in memory at once. This method is similar, but is a generator version only yielding
  one row at a time.
  """
  cols = df.columns.to_list()
  # Define out here to avoid if-statement in every evaluation
  if index:
    idx = df.index.to_list()
    for ii, row in enumerate(df.itertuples(index=False)):
      yield idx[ii], dict(zip(cols, row))
  else:
    for row in df.itertuples(index=False):
      yield dict(zip(cols, row))