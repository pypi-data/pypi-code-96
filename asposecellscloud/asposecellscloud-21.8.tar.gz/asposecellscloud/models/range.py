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


class Range(object):
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
        'column_count': 'int',
        'row_height': 'float',
        'name': 'str',
        'first_column': 'int',
        'column_width': 'float',
        'refers_to': 'str',
        'row_count': 'int',
        'first_row': 'int',
        'worksheet': 'str'
    }

    attribute_map = {
        'column_count': 'ColumnCount',
        'row_height': 'RowHeight',
        'name': 'Name',
        'first_column': 'FirstColumn',
        'column_width': 'ColumnWidth',
        'refers_to': 'RefersTo',
        'row_count': 'RowCount',
        'first_row': 'FirstRow',
        'worksheet': 'Worksheet'
    }
    
    @staticmethod
    def get_swagger_types():
        return Range.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Range.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, column_count=None, row_height=None, name=None, first_column=None, column_width=None, refers_to=None, row_count=None, first_row=None, worksheet=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Range - a model defined in Swagger
        """

        self.container['column_count'] = None
        self.container['row_height'] = None
        self.container['name'] = None
        self.container['first_column'] = None
        self.container['column_width'] = None
        self.container['refers_to'] = None
        self.container['row_count'] = None
        self.container['first_row'] = None
        self.container['worksheet'] = None

        self.column_count = column_count
        self.row_height = row_height
        if name is not None:
          self.name = name
        self.first_column = first_column
        self.column_width = column_width
        if refers_to is not None:
          self.refers_to = refers_to
        self.row_count = row_count
        self.first_row = first_row
        if worksheet is not None:
          self.worksheet = worksheet

    @property
    def column_count(self):
        """
        Gets the column_count of this Range.
        Gets the count of columns in the range.

        :return: The column_count of this Range.
        :rtype: int
        """
        return self.container['column_count']

    @column_count.setter
    def column_count(self, column_count):
        """
        Sets the column_count of this Range.
        Gets the count of columns in the range.

        :param column_count: The column_count of this Range.
        :type: int
        """
        """
        if column_count is None:
            raise ValueError("Invalid value for `column_count`, must not be `None`")
        """

        self.container['column_count'] = column_count

    @property
    def row_height(self):
        """
        Gets the row_height of this Range.
        Sets or gets the height of rows in this range

        :return: The row_height of this Range.
        :rtype: float
        """
        return self.container['row_height']

    @row_height.setter
    def row_height(self, row_height):
        """
        Sets the row_height of this Range.
        Sets or gets the height of rows in this range

        :param row_height: The row_height of this Range.
        :type: float
        """
        """
        if row_height is None:
            raise ValueError("Invalid value for `row_height`, must not be `None`")
        """

        self.container['row_height'] = row_height

    @property
    def name(self):
        """
        Gets the name of this Range.
        Gets or sets the name of the range.

        :return: The name of this Range.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Range.
        Gets or sets the name of the range.

        :param name: The name of this Range.
        :type: str
        """

        self.container['name'] = name

    @property
    def first_column(self):
        """
        Gets the first_column of this Range.
        Gets the index of the first column of the range.

        :return: The first_column of this Range.
        :rtype: int
        """
        return self.container['first_column']

    @first_column.setter
    def first_column(self, first_column):
        """
        Sets the first_column of this Range.
        Gets the index of the first column of the range.

        :param first_column: The first_column of this Range.
        :type: int
        """
        """
        if first_column is None:
            raise ValueError("Invalid value for `first_column`, must not be `None`")
        """

        self.container['first_column'] = first_column

    @property
    def column_width(self):
        """
        Gets the column_width of this Range.
        Sets or gets the column width of this range

        :return: The column_width of this Range.
        :rtype: float
        """
        return self.container['column_width']

    @column_width.setter
    def column_width(self, column_width):
        """
        Sets the column_width of this Range.
        Sets or gets the column width of this range

        :param column_width: The column_width of this Range.
        :type: float
        """
        """
        if column_width is None:
            raise ValueError("Invalid value for `column_width`, must not be `None`")
        """

        self.container['column_width'] = column_width

    @property
    def refers_to(self):
        """
        Gets the refers_to of this Range.
        Gets the range's refers to.

        :return: The refers_to of this Range.
        :rtype: str
        """
        return self.container['refers_to']

    @refers_to.setter
    def refers_to(self, refers_to):
        """
        Sets the refers_to of this Range.
        Gets the range's refers to.

        :param refers_to: The refers_to of this Range.
        :type: str
        """

        self.container['refers_to'] = refers_to

    @property
    def row_count(self):
        """
        Gets the row_count of this Range.
        Gets the count of rows in the range.

        :return: The row_count of this Range.
        :rtype: int
        """
        return self.container['row_count']

    @row_count.setter
    def row_count(self, row_count):
        """
        Sets the row_count of this Range.
        Gets the count of rows in the range.

        :param row_count: The row_count of this Range.
        :type: int
        """
        """
        if row_count is None:
            raise ValueError("Invalid value for `row_count`, must not be `None`")
        """

        self.container['row_count'] = row_count

    @property
    def first_row(self):
        """
        Gets the first_row of this Range.
        Gets the index of the first row of the range.

        :return: The first_row of this Range.
        :rtype: int
        """
        return self.container['first_row']

    @first_row.setter
    def first_row(self, first_row):
        """
        Sets the first_row of this Range.
        Gets the index of the first row of the range.

        :param first_row: The first_row of this Range.
        :type: int
        """
        """
        if first_row is None:
            raise ValueError("Invalid value for `first_row`, must not be `None`")
        """

        self.container['first_row'] = first_row

    @property
    def worksheet(self):
        """
        Gets the worksheet of this Range.
        Gets the Aspose.Cells.Range.Worksheetobject which contains this range.

        :return: The worksheet of this Range.
        :rtype: str
        """
        return self.container['worksheet']

    @worksheet.setter
    def worksheet(self, worksheet):
        """
        Sets the worksheet of this Range.
        Gets the Aspose.Cells.Range.Worksheetobject which contains this range.

        :param worksheet: The worksheet of this Range.
        :type: str
        """

        self.container['worksheet'] = worksheet

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
        if not isinstance(other, Range):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
