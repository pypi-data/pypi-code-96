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


class CalculationOptions(object):
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
        'precision_strategy': 'str',
        'ignore_error': 'bool',
        'recursive': 'bool',
        'calc_stack_size': 'int'
    }

    attribute_map = {
        'precision_strategy': 'PrecisionStrategy',
        'ignore_error': 'IgnoreError',
        'recursive': 'Recursive',
        'calc_stack_size': 'CalcStackSize'
    }
    
    @staticmethod
    def get_swagger_types():
        return CalculationOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return CalculationOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, precision_strategy=None, ignore_error=None, recursive=None, calc_stack_size=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        CalculationOptions - a model defined in Swagger
        """

        self.container['precision_strategy'] = None
        self.container['ignore_error'] = None
        self.container['recursive'] = None
        self.container['calc_stack_size'] = None

        if precision_strategy is not None:
          self.precision_strategy = precision_strategy
        if ignore_error is not None:
          self.ignore_error = ignore_error
        if recursive is not None:
          self.recursive = recursive
        if calc_stack_size is not None:
          self.calc_stack_size = calc_stack_size

    @property
    def precision_strategy(self):
        """
        Gets the precision_strategy of this CalculationOptions.

        :return: The precision_strategy of this CalculationOptions.
        :rtype: str
        """
        return self.container['precision_strategy']

    @precision_strategy.setter
    def precision_strategy(self, precision_strategy):
        """
        Sets the precision_strategy of this CalculationOptions.

        :param precision_strategy: The precision_strategy of this CalculationOptions.
        :type: str
        """

        self.container['precision_strategy'] = precision_strategy

    @property
    def ignore_error(self):
        """
        Gets the ignore_error of this CalculationOptions.

        :return: The ignore_error of this CalculationOptions.
        :rtype: bool
        """
        return self.container['ignore_error']

    @ignore_error.setter
    def ignore_error(self, ignore_error):
        """
        Sets the ignore_error of this CalculationOptions.

        :param ignore_error: The ignore_error of this CalculationOptions.
        :type: bool
        """

        self.container['ignore_error'] = ignore_error

    @property
    def recursive(self):
        """
        Gets the recursive of this CalculationOptions.

        :return: The recursive of this CalculationOptions.
        :rtype: bool
        """
        return self.container['recursive']

    @recursive.setter
    def recursive(self, recursive):
        """
        Sets the recursive of this CalculationOptions.

        :param recursive: The recursive of this CalculationOptions.
        :type: bool
        """

        self.container['recursive'] = recursive

    @property
    def calc_stack_size(self):
        """
        Gets the calc_stack_size of this CalculationOptions.

        :return: The calc_stack_size of this CalculationOptions.
        :rtype: int
        """
        return self.container['calc_stack_size']

    @calc_stack_size.setter
    def calc_stack_size(self, calc_stack_size):
        """
        Sets the calc_stack_size of this CalculationOptions.

        :param calc_stack_size: The calc_stack_size of this CalculationOptions.
        :type: int
        """

        self.container['calc_stack_size'] = calc_stack_size

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
        if not isinstance(other, CalculationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
