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


class BucketRetentionRules(object):
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
        'every_seconds': 'int',
        'shard_group_duration_seconds': 'int'
    }

    attribute_map = {
        'type': 'type',
        'every_seconds': 'everySeconds',
        'shard_group_duration_seconds': 'shardGroupDurationSeconds'
    }

    def __init__(self, type='expire', every_seconds=None, shard_group_duration_seconds=None):  # noqa: E501,D401,D403
        """BucketRetentionRules - a model defined in OpenAPI."""  # noqa: E501
        self._type = None
        self._every_seconds = None
        self._shard_group_duration_seconds = None
        self.discriminator = None

        self.type = type
        self.every_seconds = every_seconds
        if shard_group_duration_seconds is not None:
            self.shard_group_duration_seconds = shard_group_duration_seconds

    @property
    def type(self):
        """Get the type of this BucketRetentionRules.

        :return: The type of this BucketRetentionRules.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this BucketRetentionRules.

        :param type: The type of this BucketRetentionRules.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def every_seconds(self):
        """Get the every_seconds of this BucketRetentionRules.

        Duration in seconds for how long data will be kept in the database. 0 means infinite.

        :return: The every_seconds of this BucketRetentionRules.
        :rtype: int
        """  # noqa: E501
        return self._every_seconds

    @every_seconds.setter
    def every_seconds(self, every_seconds):
        """Set the every_seconds of this BucketRetentionRules.

        Duration in seconds for how long data will be kept in the database. 0 means infinite.

        :param every_seconds: The every_seconds of this BucketRetentionRules.
        :type: int
        """  # noqa: E501
        if every_seconds is None:
            raise ValueError("Invalid value for `every_seconds`, must not be `None`")  # noqa: E501
        if every_seconds is not None and every_seconds < 0:  # noqa: E501
            raise ValueError("Invalid value for `every_seconds`, must be a value greater than or equal to `0`")  # noqa: E501
        self._every_seconds = every_seconds

    @property
    def shard_group_duration_seconds(self):
        """Get the shard_group_duration_seconds of this BucketRetentionRules.

        Shard duration measured in seconds.

        :return: The shard_group_duration_seconds of this BucketRetentionRules.
        :rtype: int
        """  # noqa: E501
        return self._shard_group_duration_seconds

    @shard_group_duration_seconds.setter
    def shard_group_duration_seconds(self, shard_group_duration_seconds):
        """Set the shard_group_duration_seconds of this BucketRetentionRules.

        Shard duration measured in seconds.

        :param shard_group_duration_seconds: The shard_group_duration_seconds of this BucketRetentionRules.
        :type: int
        """  # noqa: E501
        self._shard_group_duration_seconds = shard_group_duration_seconds

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
        if not isinstance(other, BucketRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
