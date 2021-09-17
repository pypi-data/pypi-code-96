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


class IsOnboarding(object):
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
        'allowed': 'bool'
    }

    attribute_map = {
        'allowed': 'allowed'
    }

    def __init__(self, allowed=None):  # noqa: E501,D401,D403
        """IsOnboarding - a model defined in OpenAPI."""  # noqa: E501
        self._allowed = None
        self.discriminator = None

        if allowed is not None:
            self.allowed = allowed

    @property
    def allowed(self):
        """Get the allowed of this IsOnboarding.

        True means that the influxdb instance has NOT had initial setup; false means that the database has been setup.

        :return: The allowed of this IsOnboarding.
        :rtype: bool
        """  # noqa: E501
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Set the allowed of this IsOnboarding.

        True means that the influxdb instance has NOT had initial setup; false means that the database has been setup.

        :param allowed: The allowed of this IsOnboarding.
        :type: bool
        """  # noqa: E501
        self._allowed = allowed

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
        if not isinstance(other, IsOnboarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
