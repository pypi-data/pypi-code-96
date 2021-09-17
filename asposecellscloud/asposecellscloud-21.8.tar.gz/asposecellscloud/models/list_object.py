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


class ListObject(object):
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
        'link': 'Link',
        'show_totals': 'bool',
        'table_style_type': 'str',
        'display_name': 'str',
        'show_header_row': 'bool',
        'start_column': 'int',
        'show_table_style_last_column': 'bool',
        'show_table_style_column_stripes': 'bool',
        'show_table_style_first_column': 'bool',
        'start_row': 'int',
        'auto_filter': 'AutoFilter',
        'show_table_style_row_stripes': 'bool',
        'end_column': 'int',
        'table_style_name': 'str',
        'list_columns': 'list[ListColumn]',
        'end_row': 'int'
    }

    attribute_map = {
        'link': 'link',
        'show_totals': 'ShowTotals',
        'table_style_type': 'TableStyleType',
        'display_name': 'DisplayName',
        'show_header_row': 'ShowHeaderRow',
        'start_column': 'StartColumn',
        'show_table_style_last_column': 'ShowTableStyleLastColumn',
        'show_table_style_column_stripes': 'ShowTableStyleColumnStripes',
        'show_table_style_first_column': 'ShowTableStyleFirstColumn',
        'start_row': 'StartRow',
        'auto_filter': 'AutoFilter',
        'show_table_style_row_stripes': 'ShowTableStyleRowStripes',
        'end_column': 'EndColumn',
        'table_style_name': 'TableStyleName',
        'list_columns': 'ListColumns',
        'end_row': 'EndRow'
    }
    
    @staticmethod
    def get_swagger_types():
        return ListObject.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ListObject.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, show_totals=None, table_style_type=None, display_name=None, show_header_row=None, start_column=None, show_table_style_last_column=None, show_table_style_column_stripes=None, show_table_style_first_column=None, start_row=None, auto_filter=None, show_table_style_row_stripes=None, end_column=None, table_style_name=None, list_columns=None, end_row=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ListObject - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['show_totals'] = None
        self.container['table_style_type'] = None
        self.container['display_name'] = None
        self.container['show_header_row'] = None
        self.container['start_column'] = None
        self.container['show_table_style_last_column'] = None
        self.container['show_table_style_column_stripes'] = None
        self.container['show_table_style_first_column'] = None
        self.container['start_row'] = None
        self.container['auto_filter'] = None
        self.container['show_table_style_row_stripes'] = None
        self.container['end_column'] = None
        self.container['table_style_name'] = None
        self.container['list_columns'] = None
        self.container['end_row'] = None

        if link is not None:
          self.link = link
        if show_totals is not None:
          self.show_totals = show_totals
        if table_style_type is not None:
          self.table_style_type = table_style_type
        if display_name is not None:
          self.display_name = display_name
        if show_header_row is not None:
          self.show_header_row = show_header_row
        if start_column is not None:
          self.start_column = start_column
        if show_table_style_last_column is not None:
          self.show_table_style_last_column = show_table_style_last_column
        if show_table_style_column_stripes is not None:
          self.show_table_style_column_stripes = show_table_style_column_stripes
        if show_table_style_first_column is not None:
          self.show_table_style_first_column = show_table_style_first_column
        if start_row is not None:
          self.start_row = start_row
        if auto_filter is not None:
          self.auto_filter = auto_filter
        if show_table_style_row_stripes is not None:
          self.show_table_style_row_stripes = show_table_style_row_stripes
        if end_column is not None:
          self.end_column = end_column
        if table_style_name is not None:
          self.table_style_name = table_style_name
        if list_columns is not None:
          self.list_columns = list_columns
        if end_row is not None:
          self.end_row = end_row

    @property
    def link(self):
        """
        Gets the link of this ListObject.

        :return: The link of this ListObject.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this ListObject.

        :param link: The link of this ListObject.
        :type: Link
        """

        self.container['link'] = link

    @property
    def show_totals(self):
        """
        Gets the show_totals of this ListObject.
        Gets and sets whether this ListObject show total row.

        :return: The show_totals of this ListObject.
        :rtype: bool
        """
        return self.container['show_totals']

    @show_totals.setter
    def show_totals(self, show_totals):
        """
        Sets the show_totals of this ListObject.
        Gets and sets whether this ListObject show total row.

        :param show_totals: The show_totals of this ListObject.
        :type: bool
        """

        self.container['show_totals'] = show_totals

    @property
    def table_style_type(self):
        """
        Gets the table_style_type of this ListObject.
        Gets and the built-in table style.

        :return: The table_style_type of this ListObject.
        :rtype: str
        """
        return self.container['table_style_type']

    @table_style_type.setter
    def table_style_type(self, table_style_type):
        """
        Sets the table_style_type of this ListObject.
        Gets and the built-in table style.

        :param table_style_type: The table_style_type of this ListObject.
        :type: str
        """

        self.container['table_style_type'] = table_style_type

    @property
    def display_name(self):
        """
        Gets the display_name of this ListObject.
        Gets and sets the display name.Gets the data range of the ListObject.

        :return: The display_name of this ListObject.
        :rtype: str
        """
        return self.container['display_name']

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ListObject.
        Gets and sets the display name.Gets the data range of the ListObject.

        :param display_name: The display_name of this ListObject.
        :type: str
        """

        self.container['display_name'] = display_name

    @property
    def show_header_row(self):
        """
        Gets the show_header_row of this ListObject.
        Gets and sets whether this ListObject show header row.             

        :return: The show_header_row of this ListObject.
        :rtype: bool
        """
        return self.container['show_header_row']

    @show_header_row.setter
    def show_header_row(self, show_header_row):
        """
        Sets the show_header_row of this ListObject.
        Gets and sets whether this ListObject show header row.             

        :param show_header_row: The show_header_row of this ListObject.
        :type: bool
        """

        self.container['show_header_row'] = show_header_row

    @property
    def start_column(self):
        """
        Gets the start_column of this ListObject.
        Gets the start column of the range.

        :return: The start_column of this ListObject.
        :rtype: int
        """
        return self.container['start_column']

    @start_column.setter
    def start_column(self, start_column):
        """
        Sets the start_column of this ListObject.
        Gets the start column of the range.

        :param start_column: The start_column of this ListObject.
        :type: int
        """

        self.container['start_column'] = start_column

    @property
    def show_table_style_last_column(self):
        """
        Gets the show_table_style_last_column of this ListObject.
        Indicates whether the last column in the table should have the style applied.

        :return: The show_table_style_last_column of this ListObject.
        :rtype: bool
        """
        return self.container['show_table_style_last_column']

    @show_table_style_last_column.setter
    def show_table_style_last_column(self, show_table_style_last_column):
        """
        Sets the show_table_style_last_column of this ListObject.
        Indicates whether the last column in the table should have the style applied.

        :param show_table_style_last_column: The show_table_style_last_column of this ListObject.
        :type: bool
        """

        self.container['show_table_style_last_column'] = show_table_style_last_column

    @property
    def show_table_style_column_stripes(self):
        """
        Gets the show_table_style_column_stripes of this ListObject.
        Indicates whether column stripe formatting is applied.

        :return: The show_table_style_column_stripes of this ListObject.
        :rtype: bool
        """
        return self.container['show_table_style_column_stripes']

    @show_table_style_column_stripes.setter
    def show_table_style_column_stripes(self, show_table_style_column_stripes):
        """
        Sets the show_table_style_column_stripes of this ListObject.
        Indicates whether column stripe formatting is applied.

        :param show_table_style_column_stripes: The show_table_style_column_stripes of this ListObject.
        :type: bool
        """

        self.container['show_table_style_column_stripes'] = show_table_style_column_stripes

    @property
    def show_table_style_first_column(self):
        """
        Gets the show_table_style_first_column of this ListObject.
        Inidicates whether the first column in the table should have the style applied.

        :return: The show_table_style_first_column of this ListObject.
        :rtype: bool
        """
        return self.container['show_table_style_first_column']

    @show_table_style_first_column.setter
    def show_table_style_first_column(self, show_table_style_first_column):
        """
        Sets the show_table_style_first_column of this ListObject.
        Inidicates whether the first column in the table should have the style applied.

        :param show_table_style_first_column: The show_table_style_first_column of this ListObject.
        :type: bool
        """

        self.container['show_table_style_first_column'] = show_table_style_first_column

    @property
    def start_row(self):
        """
        Gets the start_row of this ListObject.
        Gets the start row of the range.

        :return: The start_row of this ListObject.
        :rtype: int
        """
        return self.container['start_row']

    @start_row.setter
    def start_row(self, start_row):
        """
        Sets the start_row of this ListObject.
        Gets the start row of the range.

        :param start_row: The start_row of this ListObject.
        :type: int
        """

        self.container['start_row'] = start_row

    @property
    def auto_filter(self):
        """
        Gets the auto_filter of this ListObject.
        Gets auto filter.             

        :return: The auto_filter of this ListObject.
        :rtype: AutoFilter
        """
        return self.container['auto_filter']

    @auto_filter.setter
    def auto_filter(self, auto_filter):
        """
        Sets the auto_filter of this ListObject.
        Gets auto filter.             

        :param auto_filter: The auto_filter of this ListObject.
        :type: AutoFilter
        """

        self.container['auto_filter'] = auto_filter

    @property
    def show_table_style_row_stripes(self):
        """
        Gets the show_table_style_row_stripes of this ListObject.
        Indicates whether row stripe formatting is applied.

        :return: The show_table_style_row_stripes of this ListObject.
        :rtype: bool
        """
        return self.container['show_table_style_row_stripes']

    @show_table_style_row_stripes.setter
    def show_table_style_row_stripes(self, show_table_style_row_stripes):
        """
        Sets the show_table_style_row_stripes of this ListObject.
        Indicates whether row stripe formatting is applied.

        :param show_table_style_row_stripes: The show_table_style_row_stripes of this ListObject.
        :type: bool
        """

        self.container['show_table_style_row_stripes'] = show_table_style_row_stripes

    @property
    def end_column(self):
        """
        Gets the end_column of this ListObject.
        Gets the end column of the range.

        :return: The end_column of this ListObject.
        :rtype: int
        """
        return self.container['end_column']

    @end_column.setter
    def end_column(self, end_column):
        """
        Sets the end_column of this ListObject.
        Gets the end column of the range.

        :param end_column: The end_column of this ListObject.
        :type: int
        """

        self.container['end_column'] = end_column

    @property
    def table_style_name(self):
        """
        Gets the table_style_name of this ListObject.
        Gets and sets the table style name.

        :return: The table_style_name of this ListObject.
        :rtype: str
        """
        return self.container['table_style_name']

    @table_style_name.setter
    def table_style_name(self, table_style_name):
        """
        Sets the table_style_name of this ListObject.
        Gets and sets the table style name.

        :param table_style_name: The table_style_name of this ListObject.
        :type: str
        """

        self.container['table_style_name'] = table_style_name

    @property
    def list_columns(self):
        """
        Gets the list_columns of this ListObject.
        Gets ListColumns of the ListObject.

        :return: The list_columns of this ListObject.
        :rtype: list[ListColumn]
        """
        return self.container['list_columns']

    @list_columns.setter
    def list_columns(self, list_columns):
        """
        Sets the list_columns of this ListObject.
        Gets ListColumns of the ListObject.

        :param list_columns: The list_columns of this ListObject.
        :type: list[ListColumn]
        """

        self.container['list_columns'] = list_columns

    @property
    def end_row(self):
        """
        Gets the end_row of this ListObject.
        Gets the end row of the range.

        :return: The end_row of this ListObject.
        :rtype: int
        """
        return self.container['end_row']

    @end_row.setter
    def end_row(self, end_row):
        """
        Sets the end_row of this ListObject.
        Gets the end row of the range.

        :param end_row: The end_row of this ListObject.
        :type: int
        """

        self.container['end_row'] = end_row

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
        if not isinstance(other, ListObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
