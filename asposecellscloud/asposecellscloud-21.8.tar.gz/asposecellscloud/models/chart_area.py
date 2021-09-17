# coding: utf-8

"""
Copyright (c) 2021 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from pprint import pformat
from six import iteritems
import re


class ChartArea(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_inner_mode': 'bool',
        'shape_properties': 'list[LinkElement]',
        'auto_scale_font': 'bool',
        'area': 'Area',
        'height': 'int',
        'width': 'int',
        'background_mode': 'str',
        'is_automatic_size': 'bool',
        'y': 'int',
        'x': 'int',
        'shadow': 'bool',
        'font': 'Font',
        'border': 'Line',
        'link': 'Link'
    }

    attribute_map = {
        'is_inner_mode': 'IsInnerMode',
        'shape_properties': 'ShapeProperties',
        'auto_scale_font': 'AutoScaleFont',
        'area': 'Area',
        'height': 'Height',
        'width': 'Width',
        'background_mode': 'BackgroundMode',
        'is_automatic_size': 'IsAutomaticSize',
        'y': 'Y',
        'x': 'X',
        'shadow': 'Shadow',
        'font': 'Font',
        'border': 'Border',
        'link': 'link'
    }
    
    @staticmethod
    def get_swagger_types():
        return ChartArea.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ChartArea.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, is_inner_mode=None, shape_properties=None, auto_scale_font=None, area=None, height=None, width=None, background_mode=None, is_automatic_size=None, y=None, x=None, shadow=None, font=None, border=None, link=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ChartArea - a model defined in Swagger
        """

        self.container['is_inner_mode'] = None
        self.container['shape_properties'] = None
        self.container['auto_scale_font'] = None
        self.container['area'] = None
        self.container['height'] = None
        self.container['width'] = None
        self.container['background_mode'] = None
        self.container['is_automatic_size'] = None
        self.container['y'] = None
        self.container['x'] = None
        self.container['shadow'] = None
        self.container['font'] = None
        self.container['border'] = None
        self.container['link'] = None

        if is_inner_mode is not None:
          self.is_inner_mode = is_inner_mode
        if shape_properties is not None:
          self.shape_properties = shape_properties
        if auto_scale_font is not None:
          self.auto_scale_font = auto_scale_font
        if area is not None:
          self.area = area
        if height is not None:
          self.height = height
        if width is not None:
          self.width = width
        if background_mode is not None:
          self.background_mode = background_mode
        if is_automatic_size is not None:
          self.is_automatic_size = is_automatic_size
        if y is not None:
          self.y = y
        if x is not None:
          self.x = x
        if shadow is not None:
          self.shadow = shadow
        if font is not None:
          self.font = font
        if border is not None:
          self.border = border
        if link is not None:
          self.link = link

    @property
    def is_inner_mode(self):
        """
        Gets the is_inner_mode of this ChartArea.

        :return: The is_inner_mode of this ChartArea.
        :rtype: bool
        """
        return self.container['is_inner_mode']

    @is_inner_mode.setter
    def is_inner_mode(self, is_inner_mode):
        """
        Sets the is_inner_mode of this ChartArea.

        :param is_inner_mode: The is_inner_mode of this ChartArea.
        :type: bool
        """

        self.container['is_inner_mode'] = is_inner_mode

    @property
    def shape_properties(self):
        """
        Gets the shape_properties of this ChartArea.

        :return: The shape_properties of this ChartArea.
        :rtype: list[LinkElement]
        """
        return self.container['shape_properties']

    @shape_properties.setter
    def shape_properties(self, shape_properties):
        """
        Sets the shape_properties of this ChartArea.

        :param shape_properties: The shape_properties of this ChartArea.
        :type: list[LinkElement]
        """

        self.container['shape_properties'] = shape_properties

    @property
    def auto_scale_font(self):
        """
        Gets the auto_scale_font of this ChartArea.

        :return: The auto_scale_font of this ChartArea.
        :rtype: bool
        """
        return self.container['auto_scale_font']

    @auto_scale_font.setter
    def auto_scale_font(self, auto_scale_font):
        """
        Sets the auto_scale_font of this ChartArea.

        :param auto_scale_font: The auto_scale_font of this ChartArea.
        :type: bool
        """

        self.container['auto_scale_font'] = auto_scale_font

    @property
    def area(self):
        """
        Gets the area of this ChartArea.

        :return: The area of this ChartArea.
        :rtype: Area
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this ChartArea.

        :param area: The area of this ChartArea.
        :type: Area
        """

        self.container['area'] = area

    @property
    def height(self):
        """
        Gets the height of this ChartArea.

        :return: The height of this ChartArea.
        :rtype: int
        """
        return self.container['height']

    @height.setter
    def height(self, height):
        """
        Sets the height of this ChartArea.

        :param height: The height of this ChartArea.
        :type: int
        """

        self.container['height'] = height

    @property
    def width(self):
        """
        Gets the width of this ChartArea.

        :return: The width of this ChartArea.
        :rtype: int
        """
        return self.container['width']

    @width.setter
    def width(self, width):
        """
        Sets the width of this ChartArea.

        :param width: The width of this ChartArea.
        :type: int
        """

        self.container['width'] = width

    @property
    def background_mode(self):
        """
        Gets the background_mode of this ChartArea.

        :return: The background_mode of this ChartArea.
        :rtype: str
        """
        return self.container['background_mode']

    @background_mode.setter
    def background_mode(self, background_mode):
        """
        Sets the background_mode of this ChartArea.

        :param background_mode: The background_mode of this ChartArea.
        :type: str
        """

        self.container['background_mode'] = background_mode

    @property
    def is_automatic_size(self):
        """
        Gets the is_automatic_size of this ChartArea.

        :return: The is_automatic_size of this ChartArea.
        :rtype: bool
        """
        return self.container['is_automatic_size']

    @is_automatic_size.setter
    def is_automatic_size(self, is_automatic_size):
        """
        Sets the is_automatic_size of this ChartArea.

        :param is_automatic_size: The is_automatic_size of this ChartArea.
        :type: bool
        """

        self.container['is_automatic_size'] = is_automatic_size

    @property
    def y(self):
        """
        Gets the y of this ChartArea.

        :return: The y of this ChartArea.
        :rtype: int
        """
        return self.container['y']

    @y.setter
    def y(self, y):
        """
        Sets the y of this ChartArea.

        :param y: The y of this ChartArea.
        :type: int
        """

        self.container['y'] = y

    @property
    def x(self):
        """
        Gets the x of this ChartArea.

        :return: The x of this ChartArea.
        :rtype: int
        """
        return self.container['x']

    @x.setter
    def x(self, x):
        """
        Sets the x of this ChartArea.

        :param x: The x of this ChartArea.
        :type: int
        """

        self.container['x'] = x

    @property
    def shadow(self):
        """
        Gets the shadow of this ChartArea.

        :return: The shadow of this ChartArea.
        :rtype: bool
        """
        return self.container['shadow']

    @shadow.setter
    def shadow(self, shadow):
        """
        Sets the shadow of this ChartArea.

        :param shadow: The shadow of this ChartArea.
        :type: bool
        """

        self.container['shadow'] = shadow

    @property
    def font(self):
        """
        Gets the font of this ChartArea.

        :return: The font of this ChartArea.
        :rtype: Font
        """
        return self.container['font']

    @font.setter
    def font(self, font):
        """
        Sets the font of this ChartArea.

        :param font: The font of this ChartArea.
        :type: Font
        """

        self.container['font'] = font

    @property
    def border(self):
        """
        Gets the border of this ChartArea.

        :return: The border of this ChartArea.
        :rtype: Line
        """
        return self.container['border']

    @border.setter
    def border(self, border):
        """
        Sets the border of this ChartArea.

        :param border: The border of this ChartArea.
        :type: Line
        """

        self.container['border'] = border

    @property
    def link(self):
        """
        Gets the link of this ChartArea.

        :return: The link of this ChartArea.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this ChartArea.

        :param link: The link of this ChartArea.
        :type: Link
        """

        self.container['link'] = link

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ChartArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
