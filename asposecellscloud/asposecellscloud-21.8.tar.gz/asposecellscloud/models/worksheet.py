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


class Worksheet(object):
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
        'index': 'int',
        'pictures': 'LinkElement',
        'charts': 'LinkElement',
        'comments': 'LinkElement',
        'hyperlinks': 'LinkElement',
        'is_visible': 'bool',
        'view_type': 'str',
        'type': 'str',
        'is_gridlines_visible': 'bool',
        'is_row_column_headers_visible': 'bool',
        'is_page_break_preview': 'bool',
        'display_zeros': 'bool',
        'transition_evaluation': 'bool',
        'display_right_to_left': 'bool',
        'first_visible_column': 'int',
        'ole_objects': 'LinkElement',
        'is_outline_shown': 'bool',
        'name': 'str',
        'auto_shapes': 'LinkElement',
        'cells': 'LinkElement',
        'validations': 'LinkElement',
        'zoom': 'int',
        'conditional_formattings': 'LinkElement',
        'is_selected': 'bool',
        'tab_color': 'Color',
        'first_visible_row': 'int',
        'transition_entry': 'bool',
        'visibility_type': 'str',
        'is_ruler_visible': 'bool',
        'links': 'list[Link]',
        'is_protected': 'bool',
        'merged_cells': 'LinkElement'
    }

    attribute_map = {
        'index': 'Index',
        'pictures': 'Pictures',
        'charts': 'Charts',
        'comments': 'Comments',
        'hyperlinks': 'Hyperlinks',
        'is_visible': 'IsVisible',
        'view_type': 'ViewType',
        'type': 'Type',
        'is_gridlines_visible': 'IsGridlinesVisible',
        'is_row_column_headers_visible': 'IsRowColumnHeadersVisible',
        'is_page_break_preview': 'IsPageBreakPreview',
        'display_zeros': 'DisplayZeros',
        'transition_evaluation': 'TransitionEvaluation',
        'display_right_to_left': 'DisplayRightToLeft',
        'first_visible_column': 'FirstVisibleColumn',
        'ole_objects': 'OleObjects',
        'is_outline_shown': 'IsOutlineShown',
        'name': 'Name',
        'auto_shapes': 'AutoShapes',
        'cells': 'Cells',
        'validations': 'Validations',
        'zoom': 'Zoom',
        'conditional_formattings': 'ConditionalFormattings',
        'is_selected': 'IsSelected',
        'tab_color': 'TabColor',
        'first_visible_row': 'FirstVisibleRow',
        'transition_entry': 'TransitionEntry',
        'visibility_type': 'VisibilityType',
        'is_ruler_visible': 'IsRulerVisible',
        'links': 'Links',
        'is_protected': 'IsProtected',
        'merged_cells': 'MergedCells'
    }
    
    @staticmethod
    def get_swagger_types():
        return Worksheet.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Worksheet.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, index=None, pictures=None, charts=None, comments=None, hyperlinks=None, is_visible=None, view_type=None, type=None, is_gridlines_visible=None, is_row_column_headers_visible=None, is_page_break_preview=None, display_zeros=None, transition_evaluation=None, display_right_to_left=None, first_visible_column=None, ole_objects=None, is_outline_shown=None, name=None, auto_shapes=None, cells=None, validations=None, zoom=None, conditional_formattings=None, is_selected=None, tab_color=None, first_visible_row=None, transition_entry=None, visibility_type=None, is_ruler_visible=None, links=None, is_protected=None, merged_cells=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Worksheet - a model defined in Swagger
        """

        self.container['index'] = None
        self.container['pictures'] = None
        self.container['charts'] = None
        self.container['comments'] = None
        self.container['hyperlinks'] = None
        self.container['is_visible'] = None
        self.container['view_type'] = None
        self.container['type'] = None
        self.container['is_gridlines_visible'] = None
        self.container['is_row_column_headers_visible'] = None
        self.container['is_page_break_preview'] = None
        self.container['display_zeros'] = None
        self.container['transition_evaluation'] = None
        self.container['display_right_to_left'] = None
        self.container['first_visible_column'] = None
        self.container['ole_objects'] = None
        self.container['is_outline_shown'] = None
        self.container['name'] = None
        self.container['auto_shapes'] = None
        self.container['cells'] = None
        self.container['validations'] = None
        self.container['zoom'] = None
        self.container['conditional_formattings'] = None
        self.container['is_selected'] = None
        self.container['tab_color'] = None
        self.container['first_visible_row'] = None
        self.container['transition_entry'] = None
        self.container['visibility_type'] = None
        self.container['is_ruler_visible'] = None
        self.container['links'] = None
        self.container['is_protected'] = None
        self.container['merged_cells'] = None

        self.index = index
        if pictures is not None:
          self.pictures = pictures
        if charts is not None:
          self.charts = charts
        if comments is not None:
          self.comments = comments
        if hyperlinks is not None:
          self.hyperlinks = hyperlinks
        if is_visible is not None:
          self.is_visible = is_visible
        if view_type is not None:
          self.view_type = view_type
        if type is not None:
          self.type = type
        if is_gridlines_visible is not None:
          self.is_gridlines_visible = is_gridlines_visible
        if is_row_column_headers_visible is not None:
          self.is_row_column_headers_visible = is_row_column_headers_visible
        if is_page_break_preview is not None:
          self.is_page_break_preview = is_page_break_preview
        if display_zeros is not None:
          self.display_zeros = display_zeros
        if transition_evaluation is not None:
          self.transition_evaluation = transition_evaluation
        if display_right_to_left is not None:
          self.display_right_to_left = display_right_to_left
        if first_visible_column is not None:
          self.first_visible_column = first_visible_column
        if ole_objects is not None:
          self.ole_objects = ole_objects
        if is_outline_shown is not None:
          self.is_outline_shown = is_outline_shown
        if name is not None:
          self.name = name
        if auto_shapes is not None:
          self.auto_shapes = auto_shapes
        if cells is not None:
          self.cells = cells
        if validations is not None:
          self.validations = validations
        if zoom is not None:
          self.zoom = zoom
        if conditional_formattings is not None:
          self.conditional_formattings = conditional_formattings
        if is_selected is not None:
          self.is_selected = is_selected
        if tab_color is not None:
          self.tab_color = tab_color
        if first_visible_row is not None:
          self.first_visible_row = first_visible_row
        if transition_entry is not None:
          self.transition_entry = transition_entry
        if visibility_type is not None:
          self.visibility_type = visibility_type
        if is_ruler_visible is not None:
          self.is_ruler_visible = is_ruler_visible
        if links is not None:
          self.links = links
        self.is_protected = is_protected
        if merged_cells is not None:
          self.merged_cells = merged_cells

    @property
    def index(self):
        """
        Gets the index of this Worksheet.
        Gets the index of sheet in the worksheets collection.             

        :return: The index of this Worksheet.
        :rtype: int
        """
        return self.container['index']

    @index.setter
    def index(self, index):
        """
        Sets the index of this Worksheet.
        Gets the index of sheet in the worksheets collection.             

        :param index: The index of this Worksheet.
        :type: int
        """
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")
        """

        self.container['index'] = index

    @property
    def pictures(self):
        """
        Gets the pictures of this Worksheet.

        :return: The pictures of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['pictures']

    @pictures.setter
    def pictures(self, pictures):
        """
        Sets the pictures of this Worksheet.

        :param pictures: The pictures of this Worksheet.
        :type: LinkElement
        """

        self.container['pictures'] = pictures

    @property
    def charts(self):
        """
        Gets the charts of this Worksheet.

        :return: The charts of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['charts']

    @charts.setter
    def charts(self, charts):
        """
        Sets the charts of this Worksheet.

        :param charts: The charts of this Worksheet.
        :type: LinkElement
        """

        self.container['charts'] = charts

    @property
    def comments(self):
        """
        Gets the comments of this Worksheet.

        :return: The comments of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['comments']

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Worksheet.

        :param comments: The comments of this Worksheet.
        :type: LinkElement
        """

        self.container['comments'] = comments

    @property
    def hyperlinks(self):
        """
        Gets the hyperlinks of this Worksheet.

        :return: The hyperlinks of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['hyperlinks']

    @hyperlinks.setter
    def hyperlinks(self, hyperlinks):
        """
        Sets the hyperlinks of this Worksheet.

        :param hyperlinks: The hyperlinks of this Worksheet.
        :type: LinkElement
        """

        self.container['hyperlinks'] = hyperlinks

    @property
    def is_visible(self):
        """
        Gets the is_visible of this Worksheet.
        Represents if the worksheet is visible.             

        :return: The is_visible of this Worksheet.
        :rtype: bool
        """
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this Worksheet.
        Represents if the worksheet is visible.             

        :param is_visible: The is_visible of this Worksheet.
        :type: bool
        """

        self.container['is_visible'] = is_visible

    @property
    def view_type(self):
        """
        Gets the view_type of this Worksheet.
        Gets and sets the view type.

        :return: The view_type of this Worksheet.
        :rtype: str
        """
        return self.container['view_type']

    @view_type.setter
    def view_type(self, view_type):
        """
        Sets the view_type of this Worksheet.
        Gets and sets the view type.

        :param view_type: The view_type of this Worksheet.
        :type: str
        """

        self.container['view_type'] = view_type

    @property
    def type(self):
        """
        Gets the type of this Worksheet.
        Represents worksheet type

        :return: The type of this Worksheet.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this Worksheet.
        Represents worksheet type

        :param type: The type of this Worksheet.
        :type: str
        """

        self.container['type'] = type

    @property
    def is_gridlines_visible(self):
        """
        Gets the is_gridlines_visible of this Worksheet.
        Gets or sets a value indicating whether the gridelines are visible.Default     is true.

        :return: The is_gridlines_visible of this Worksheet.
        :rtype: bool
        """
        return self.container['is_gridlines_visible']

    @is_gridlines_visible.setter
    def is_gridlines_visible(self, is_gridlines_visible):
        """
        Sets the is_gridlines_visible of this Worksheet.
        Gets or sets a value indicating whether the gridelines are visible.Default     is true.

        :param is_gridlines_visible: The is_gridlines_visible of this Worksheet.
        :type: bool
        """

        self.container['is_gridlines_visible'] = is_gridlines_visible

    @property
    def is_row_column_headers_visible(self):
        """
        Gets the is_row_column_headers_visible of this Worksheet.
        Gets or sets a value indicating whether the worksheet will display row and column headers.Default is true.             

        :return: The is_row_column_headers_visible of this Worksheet.
        :rtype: bool
        """
        return self.container['is_row_column_headers_visible']

    @is_row_column_headers_visible.setter
    def is_row_column_headers_visible(self, is_row_column_headers_visible):
        """
        Sets the is_row_column_headers_visible of this Worksheet.
        Gets or sets a value indicating whether the worksheet will display row and column headers.Default is true.             

        :param is_row_column_headers_visible: The is_row_column_headers_visible of this Worksheet.
        :type: bool
        """

        self.container['is_row_column_headers_visible'] = is_row_column_headers_visible

    @property
    def is_page_break_preview(self):
        """
        Gets the is_page_break_preview of this Worksheet.
        Indications the specified worksheet is shown in normal view or page break preview.

        :return: The is_page_break_preview of this Worksheet.
        :rtype: bool
        """
        return self.container['is_page_break_preview']

    @is_page_break_preview.setter
    def is_page_break_preview(self, is_page_break_preview):
        """
        Sets the is_page_break_preview of this Worksheet.
        Indications the specified worksheet is shown in normal view or page break preview.

        :param is_page_break_preview: The is_page_break_preview of this Worksheet.
        :type: bool
        """

        self.container['is_page_break_preview'] = is_page_break_preview

    @property
    def display_zeros(self):
        """
        Gets the display_zeros of this Worksheet.
        True if zero values are displayed.

        :return: The display_zeros of this Worksheet.
        :rtype: bool
        """
        return self.container['display_zeros']

    @display_zeros.setter
    def display_zeros(self, display_zeros):
        """
        Sets the display_zeros of this Worksheet.
        True if zero values are displayed.

        :param display_zeros: The display_zeros of this Worksheet.
        :type: bool
        """

        self.container['display_zeros'] = display_zeros

    @property
    def transition_evaluation(self):
        """
        Gets the transition_evaluation of this Worksheet.
        Flag indicating whether the Transition Formula Evaluation (Lotus compatibility) option is enabled.             

        :return: The transition_evaluation of this Worksheet.
        :rtype: bool
        """
        return self.container['transition_evaluation']

    @transition_evaluation.setter
    def transition_evaluation(self, transition_evaluation):
        """
        Sets the transition_evaluation of this Worksheet.
        Flag indicating whether the Transition Formula Evaluation (Lotus compatibility) option is enabled.             

        :param transition_evaluation: The transition_evaluation of this Worksheet.
        :type: bool
        """

        self.container['transition_evaluation'] = transition_evaluation

    @property
    def display_right_to_left(self):
        """
        Gets the display_right_to_left of this Worksheet.
        Indicates if the specified worksheet is displayed from right to left instead    of from left to right.  Default is false.             

        :return: The display_right_to_left of this Worksheet.
        :rtype: bool
        """
        return self.container['display_right_to_left']

    @display_right_to_left.setter
    def display_right_to_left(self, display_right_to_left):
        """
        Sets the display_right_to_left of this Worksheet.
        Indicates if the specified worksheet is displayed from right to left instead    of from left to right.  Default is false.             

        :param display_right_to_left: The display_right_to_left of this Worksheet.
        :type: bool
        """

        self.container['display_right_to_left'] = display_right_to_left

    @property
    def first_visible_column(self):
        """
        Gets the first_visible_column of this Worksheet.
        Represents first visible column index.

        :return: The first_visible_column of this Worksheet.
        :rtype: int
        """
        return self.container['first_visible_column']

    @first_visible_column.setter
    def first_visible_column(self, first_visible_column):
        """
        Sets the first_visible_column of this Worksheet.
        Represents first visible column index.

        :param first_visible_column: The first_visible_column of this Worksheet.
        :type: int
        """

        self.container['first_visible_column'] = first_visible_column

    @property
    def ole_objects(self):
        """
        Gets the ole_objects of this Worksheet.

        :return: The ole_objects of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['ole_objects']

    @ole_objects.setter
    def ole_objects(self, ole_objects):
        """
        Sets the ole_objects of this Worksheet.

        :param ole_objects: The ole_objects of this Worksheet.
        :type: LinkElement
        """

        self.container['ole_objects'] = ole_objects

    @property
    def is_outline_shown(self):
        """
        Gets the is_outline_shown of this Worksheet.
        Indicates whether show outline.             

        :return: The is_outline_shown of this Worksheet.
        :rtype: bool
        """
        return self.container['is_outline_shown']

    @is_outline_shown.setter
    def is_outline_shown(self, is_outline_shown):
        """
        Sets the is_outline_shown of this Worksheet.
        Indicates whether show outline.             

        :param is_outline_shown: The is_outline_shown of this Worksheet.
        :type: bool
        """

        self.container['is_outline_shown'] = is_outline_shown

    @property
    def name(self):
        """
        Gets the name of this Worksheet.
        Gets or sets the name of the worksheet.             

        :return: The name of this Worksheet.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Worksheet.
        Gets or sets the name of the worksheet.             

        :param name: The name of this Worksheet.
        :type: str
        """

        self.container['name'] = name

    @property
    def auto_shapes(self):
        """
        Gets the auto_shapes of this Worksheet.

        :return: The auto_shapes of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['auto_shapes']

    @auto_shapes.setter
    def auto_shapes(self, auto_shapes):
        """
        Sets the auto_shapes of this Worksheet.

        :param auto_shapes: The auto_shapes of this Worksheet.
        :type: LinkElement
        """

        self.container['auto_shapes'] = auto_shapes

    @property
    def cells(self):
        """
        Gets the cells of this Worksheet.

        :return: The cells of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['cells']

    @cells.setter
    def cells(self, cells):
        """
        Sets the cells of this Worksheet.

        :param cells: The cells of this Worksheet.
        :type: LinkElement
        """

        self.container['cells'] = cells

    @property
    def validations(self):
        """
        Gets the validations of this Worksheet.

        :return: The validations of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['validations']

    @validations.setter
    def validations(self, validations):
        """
        Sets the validations of this Worksheet.

        :param validations: The validations of this Worksheet.
        :type: LinkElement
        """

        self.container['validations'] = validations

    @property
    def zoom(self):
        """
        Gets the zoom of this Worksheet.
        Represents the scaling factor in percent. It should be btween 10 and 400.             

        :return: The zoom of this Worksheet.
        :rtype: int
        """
        return self.container['zoom']

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom of this Worksheet.
        Represents the scaling factor in percent. It should be btween 10 and 400.             

        :param zoom: The zoom of this Worksheet.
        :type: int
        """

        self.container['zoom'] = zoom

    @property
    def conditional_formattings(self):
        """
        Gets the conditional_formattings of this Worksheet.

        :return: The conditional_formattings of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['conditional_formattings']

    @conditional_formattings.setter
    def conditional_formattings(self, conditional_formattings):
        """
        Sets the conditional_formattings of this Worksheet.

        :param conditional_formattings: The conditional_formattings of this Worksheet.
        :type: LinkElement
        """

        self.container['conditional_formattings'] = conditional_formattings

    @property
    def is_selected(self):
        """
        Gets the is_selected of this Worksheet.
        Indicates whether this worksheet is selected when the workbook is opened.

        :return: The is_selected of this Worksheet.
        :rtype: bool
        """
        return self.container['is_selected']

    @is_selected.setter
    def is_selected(self, is_selected):
        """
        Sets the is_selected of this Worksheet.
        Indicates whether this worksheet is selected when the workbook is opened.

        :param is_selected: The is_selected of this Worksheet.
        :type: bool
        """

        self.container['is_selected'] = is_selected

    @property
    def tab_color(self):
        """
        Gets the tab_color of this Worksheet.
        Represents worksheet tab color.

        :return: The tab_color of this Worksheet.
        :rtype: Color
        """
        return self.container['tab_color']

    @tab_color.setter
    def tab_color(self, tab_color):
        """
        Sets the tab_color of this Worksheet.
        Represents worksheet tab color.

        :param tab_color: The tab_color of this Worksheet.
        :type: Color
        """

        self.container['tab_color'] = tab_color

    @property
    def first_visible_row(self):
        """
        Gets the first_visible_row of this Worksheet.
        Represents first visible row index.             

        :return: The first_visible_row of this Worksheet.
        :rtype: int
        """
        return self.container['first_visible_row']

    @first_visible_row.setter
    def first_visible_row(self, first_visible_row):
        """
        Sets the first_visible_row of this Worksheet.
        Represents first visible row index.             

        :param first_visible_row: The first_visible_row of this Worksheet.
        :type: int
        """

        self.container['first_visible_row'] = first_visible_row

    @property
    def transition_entry(self):
        """
        Gets the transition_entry of this Worksheet.
        Flag indicating whether the Transition Formula Entry (Lotus compatibility) option is enabled.

        :return: The transition_entry of this Worksheet.
        :rtype: bool
        """
        return self.container['transition_entry']

    @transition_entry.setter
    def transition_entry(self, transition_entry):
        """
        Sets the transition_entry of this Worksheet.
        Flag indicating whether the Transition Formula Entry (Lotus compatibility) option is enabled.

        :param transition_entry: The transition_entry of this Worksheet.
        :type: bool
        """

        self.container['transition_entry'] = transition_entry

    @property
    def visibility_type(self):
        """
        Gets the visibility_type of this Worksheet.
        Indicates the state for this sheet visibility             

        :return: The visibility_type of this Worksheet.
        :rtype: str
        """
        return self.container['visibility_type']

    @visibility_type.setter
    def visibility_type(self, visibility_type):
        """
        Sets the visibility_type of this Worksheet.
        Indicates the state for this sheet visibility             

        :param visibility_type: The visibility_type of this Worksheet.
        :type: str
        """

        self.container['visibility_type'] = visibility_type

    @property
    def is_ruler_visible(self):
        """
        Gets the is_ruler_visible of this Worksheet.
        Indicates whether the ruler is visible. Only apply for page break preview.

        :return: The is_ruler_visible of this Worksheet.
        :rtype: bool
        """
        return self.container['is_ruler_visible']

    @is_ruler_visible.setter
    def is_ruler_visible(self, is_ruler_visible):
        """
        Sets the is_ruler_visible of this Worksheet.
        Indicates whether the ruler is visible. Only apply for page break preview.

        :param is_ruler_visible: The is_ruler_visible of this Worksheet.
        :type: bool
        """

        self.container['is_ruler_visible'] = is_ruler_visible

    @property
    def links(self):
        """
        Gets the links of this Worksheet.

        :return: The links of this Worksheet.
        :rtype: list[Link]
        """
        return self.container['links']

    @links.setter
    def links(self, links):
        """
        Sets the links of this Worksheet.

        :param links: The links of this Worksheet.
        :type: list[Link]
        """

        self.container['links'] = links

    @property
    def is_protected(self):
        """
        Gets the is_protected of this Worksheet.
        Indicates if the worksheet is protected.

        :return: The is_protected of this Worksheet.
        :rtype: bool
        """
        return self.container['is_protected']

    @is_protected.setter
    def is_protected(self, is_protected):
        """
        Sets the is_protected of this Worksheet.
        Indicates if the worksheet is protected.

        :param is_protected: The is_protected of this Worksheet.
        :type: bool
        """
        """
        if is_protected is None:
            raise ValueError("Invalid value for `is_protected`, must not be `None`")
        """

        self.container['is_protected'] = is_protected

    @property
    def merged_cells(self):
        """
        Gets the merged_cells of this Worksheet.

        :return: The merged_cells of this Worksheet.
        :rtype: LinkElement
        """
        return self.container['merged_cells']

    @merged_cells.setter
    def merged_cells(self, merged_cells):
        """
        Sets the merged_cells of this Worksheet.

        :param merged_cells: The merged_cells of this Worksheet.
        :type: LinkElement
        """

        self.container['merged_cells'] = merged_cells

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
        if not isinstance(other, Worksheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
