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


class Columns(object):
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
        'columns_count': 'int',
        'max_column': 'int',
        'columns_list': 'list[LinkElement]'
    }

    attribute_map = {
        'link': 'link',
        'columns_count': 'ColumnsCount',
        'max_column': 'MaxColumn',
        'columns_list': 'ColumnsList'
    }
    
    @staticmethod
    def get_swagger_types():
        return Columns.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Columns.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, columns_count=None, max_column=None, columns_list=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Columns - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['columns_count'] = None
        self.container['max_column'] = None
        self.container['columns_list'] = None

        if link is not None:
          self.link = link
        self.columns_count = columns_count
        self.max_column = max_column
        if columns_list is not None:
          self.columns_list = columns_list

    @property
    def link(self):
        """
        Gets the link of this Columns.

        :return: The link of this Columns.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Columns.

        :param link: The link of this Columns.
        :type: Link
        """

        self.container['link'] = link

    @property
    def columns_count(self):
        """
        Gets the columns_count of this Columns.

        :return: The columns_count of this Columns.
        :rtype: int
        """
        return self.container['columns_count']

    @columns_count.setter
    def columns_count(self, columns_count):
        """
        Sets the columns_count of this Columns.

        :param columns_count: The columns_count of this Columns.
        :type: int
        """
        """
        if columns_count is None:
            raise ValueError("Invalid value for `columns_count`, must not be `None`")
        """

        self.container['columns_count'] = columns_count

    @property
    def max_column(self):
        """
        Gets the max_column of this Columns.

        :return: The max_column of this Columns.
        :rtype: int
        """
        return self.container['max_column']

    @max_column.setter
    def max_column(self, max_column):
        """
        Sets the max_column of this Columns.

        :param max_column: The max_column of this Columns.
        :type: int
        """
        """
        if max_column is None:
            raise ValueError("Invalid value for `max_column`, must not be `None`")
        """

        self.container['max_column'] = max_column

    @property
    def columns_list(self):
        """
        Gets the columns_list of this Columns.

        :return: The columns_list of this Columns.
        :rtype: list[LinkElement]
        """
        return self.container['columns_list']

    @columns_list.setter
    def columns_list(self, columns_list):
        """
        Sets the columns_list of this Columns.

        :param columns_list: The columns_list of this Columns.
        :type: list[LinkElement]
        """

        self.container['columns_list'] = columns_list

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
        if not isinstance(other, Columns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
