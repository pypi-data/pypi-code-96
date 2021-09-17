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


class DashboardColor(object):
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
        'id': 'str',
        'type': 'str',
        'hex': 'str',
        'name': 'str',
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'hex': 'hex',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, id=None, type=None, hex=None, name=None, value=None):  # noqa: E501,D401,D403
        """DashboardColor - a model defined in OpenAPI."""  # noqa: E501
        self._id = None
        self._type = None
        self._hex = None
        self._name = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.hex = hex
        self.name = name
        self.value = value

    @property
    def id(self):
        """Get the id of this DashboardColor.

        The unique ID of the view color.

        :return: The id of this DashboardColor.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this DashboardColor.

        The unique ID of the view color.

        :param id: The id of this DashboardColor.
        :type: str
        """  # noqa: E501
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id

    @property
    def type(self):
        """Get the type of this DashboardColor.

        Type is how the color is used.

        :return: The type of this DashboardColor.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this DashboardColor.

        Type is how the color is used.

        :param type: The type of this DashboardColor.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def hex(self):
        """Get the hex of this DashboardColor.

        The hex number of the color

        :return: The hex of this DashboardColor.
        :rtype: str
        """  # noqa: E501
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Set the hex of this DashboardColor.

        The hex number of the color

        :param hex: The hex of this DashboardColor.
        :type: str
        """  # noqa: E501
        if hex is None:
            raise ValueError("Invalid value for `hex`, must not be `None`")  # noqa: E501
        if hex is not None and len(hex) > 7:
            raise ValueError("Invalid value for `hex`, length must be less than or equal to `7`")  # noqa: E501
        if hex is not None and len(hex) < 7:
            raise ValueError("Invalid value for `hex`, length must be greater than or equal to `7`")  # noqa: E501
        self._hex = hex

    @property
    def name(self):
        """Get the name of this DashboardColor.

        The user-facing name of the hex color.

        :return: The name of this DashboardColor.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this DashboardColor.

        The user-facing name of the hex color.

        :param name: The name of this DashboardColor.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def value(self):
        """Get the value of this DashboardColor.

        The data value mapped to this color.

        :return: The value of this DashboardColor.
        :rtype: float
        """  # noqa: E501
        return self._value

    @value.setter
    def value(self, value):
        """Set the value of this DashboardColor.

        The data value mapped to this color.

        :param value: The value of this DashboardColor.
        :type: float
        """  # noqa: E501
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        self._value = value

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
        if not isinstance(other, DashboardColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
