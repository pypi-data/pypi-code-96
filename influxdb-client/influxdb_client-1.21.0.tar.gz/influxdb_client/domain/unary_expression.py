# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.expression import Expression


class UnaryExpression(Expression):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'operator': 'str',
        'argument': 'Expression'
    }

    attribute_map = {
        'type': 'type',
        'operator': 'operator',
        'argument': 'argument'
    }

    def __init__(self, type=None, operator=None, argument=None):  # noqa: E501,D401,D403
        """UnaryExpression - a model defined in OpenAPI."""  # noqa: E501
        Expression.__init__(self)  # noqa: E501

        self._type = None
        self._operator = None
        self._argument = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if operator is not None:
            self.operator = operator
        if argument is not None:
            self.argument = argument

    @property
    def type(self):
        """Get the type of this UnaryExpression.

        Type of AST node

        :return: The type of this UnaryExpression.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this UnaryExpression.

        Type of AST node

        :param type: The type of this UnaryExpression.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def operator(self):
        """Get the operator of this UnaryExpression.

        :return: The operator of this UnaryExpression.
        :rtype: str
        """  # noqa: E501
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Set the operator of this UnaryExpression.

        :param operator: The operator of this UnaryExpression.
        :type: str
        """  # noqa: E501
        self._operator = operator

    @property
    def argument(self):
        """Get the argument of this UnaryExpression.

        :return: The argument of this UnaryExpression.
        :rtype: Expression
        """  # noqa: E501
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Set the argument of this UnaryExpression.

        :param argument: The argument of this UnaryExpression.
        :type: Expression
        """  # noqa: E501
        self._argument = argument

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, UnaryExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
