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
from influxdb_client.domain.node import Node


class Block(Node):
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
        'body': 'list[Statement]'
    }

    attribute_map = {
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, type=None, body=None):  # noqa: E501,D401,D403
        """Block - a model defined in OpenAPI."""  # noqa: E501
        Node.__init__(self)  # noqa: E501

        self._type = None
        self._body = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if body is not None:
            self.body = body

    @property
    def type(self):
        """Get the type of this Block.

        Type of AST node

        :return: The type of this Block.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this Block.

        Type of AST node

        :param type: The type of this Block.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def body(self):
        """Get the body of this Block.

        Block body

        :return: The body of this Block.
        :rtype: list[Statement]
        """  # noqa: E501
        return self._body

    @body.setter
    def body(self, body):
        """Set the body of this Block.

        Block body

        :param body: The body of this Block.
        :type: list[Statement]
        """  # noqa: E501
        self._body = body

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
        if not isinstance(other, Block):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
