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
from influxdb_client.domain.user_response import UserResponse


class ResourceOwner(UserResponse):
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
        'role': 'str',
        'id': 'str',
        'oauth_id': 'str',
        'name': 'str',
        'status': 'str',
        'links': 'UserResponseLinks'
    }

    attribute_map = {
        'role': 'role',
        'id': 'id',
        'oauth_id': 'oauthID',
        'name': 'name',
        'status': 'status',
        'links': 'links'
    }

    def __init__(self, role='owner', id=None, oauth_id=None, name=None, status='active', links=None):  # noqa: E501,D401,D403
        """ResourceOwner - a model defined in OpenAPI."""  # noqa: E501
        UserResponse.__init__(self, id=id, oauth_id=oauth_id, name=name, status=status, links=links)  # noqa: E501

        self._role = None
        self.discriminator = None

        if role is not None:
            self.role = role

    @property
    def role(self):
        """Get the role of this ResourceOwner.

        :return: The role of this ResourceOwner.
        :rtype: str
        """  # noqa: E501
        return self._role

    @role.setter
    def role(self, role):
        """Set the role of this ResourceOwner.

        :param role: The role of this ResourceOwner.
        :type: str
        """  # noqa: E501
        self._role = role

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
        if not isinstance(other, ResourceOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
