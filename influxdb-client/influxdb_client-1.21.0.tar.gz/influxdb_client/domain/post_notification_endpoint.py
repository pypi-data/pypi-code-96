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


class PostNotificationEndpoint(object):
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
        'type': 'NotificationEndpointType'
    }

    attribute_map = {
        'type': 'type'
    }

    discriminator_value_class_map = {
        'slack': 'SlackNotificationEndpoint',
        'pagerduty': 'PagerDutyNotificationEndpoint',
        'http': 'HTTPNotificationEndpoint',
        'telegram': 'TelegramNotificationEndpoint'
    }

    def __init__(self, type=None):  # noqa: E501,D401,D403
        """PostNotificationEndpoint - a model defined in OpenAPI."""  # noqa: E501
        self._type = None
        self.discriminator = 'type'

        self.type = type

    @property
    def type(self):
        """Get the type of this PostNotificationEndpoint.

        :return: The type of this PostNotificationEndpoint.
        :rtype: NotificationEndpointType
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this PostNotificationEndpoint.

        :param type: The type of this PostNotificationEndpoint.
        :type: NotificationEndpointType
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    def get_real_child_model(self, data):
        """Return the real base class specified by the discriminator."""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, PostNotificationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
