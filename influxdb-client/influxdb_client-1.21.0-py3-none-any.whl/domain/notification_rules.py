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


class NotificationRules(object):
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
        'notification_rules': 'list[NotificationRule]',
        'links': 'Links'
    }

    attribute_map = {
        'notification_rules': 'notificationRules',
        'links': 'links'
    }

    def __init__(self, notification_rules=None, links=None):  # noqa: E501,D401,D403
        """NotificationRules - a model defined in OpenAPI."""  # noqa: E501
        self._notification_rules = None
        self._links = None
        self.discriminator = None

        if notification_rules is not None:
            self.notification_rules = notification_rules
        if links is not None:
            self.links = links

    @property
    def notification_rules(self):
        """Get the notification_rules of this NotificationRules.

        :return: The notification_rules of this NotificationRules.
        :rtype: list[NotificationRule]
        """  # noqa: E501
        return self._notification_rules

    @notification_rules.setter
    def notification_rules(self, notification_rules):
        """Set the notification_rules of this NotificationRules.

        :param notification_rules: The notification_rules of this NotificationRules.
        :type: list[NotificationRule]
        """  # noqa: E501
        self._notification_rules = notification_rules

    @property
    def links(self):
        """Get the links of this NotificationRules.

        :return: The links of this NotificationRules.
        :rtype: Links
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this NotificationRules.

        :param links: The links of this NotificationRules.
        :type: Links
        """  # noqa: E501
        self._links = links

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
        if not isinstance(other, NotificationRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
