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


class OnboardingResponse(object):
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
        'user': 'UserResponse',
        'org': 'Organization',
        'bucket': 'Bucket',
        'auth': 'Authorization'
    }

    attribute_map = {
        'user': 'user',
        'org': 'org',
        'bucket': 'bucket',
        'auth': 'auth'
    }

    def __init__(self, user=None, org=None, bucket=None, auth=None):  # noqa: E501,D401,D403
        """OnboardingResponse - a model defined in OpenAPI."""  # noqa: E501
        self._user = None
        self._org = None
        self._bucket = None
        self._auth = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if org is not None:
            self.org = org
        if bucket is not None:
            self.bucket = bucket
        if auth is not None:
            self.auth = auth

    @property
    def user(self):
        """Get the user of this OnboardingResponse.

        :return: The user of this OnboardingResponse.
        :rtype: UserResponse
        """  # noqa: E501
        return self._user

    @user.setter
    def user(self, user):
        """Set the user of this OnboardingResponse.

        :param user: The user of this OnboardingResponse.
        :type: UserResponse
        """  # noqa: E501
        self._user = user

    @property
    def org(self):
        """Get the org of this OnboardingResponse.

        :return: The org of this OnboardingResponse.
        :rtype: Organization
        """  # noqa: E501
        return self._org

    @org.setter
    def org(self, org):
        """Set the org of this OnboardingResponse.

        :param org: The org of this OnboardingResponse.
        :type: Organization
        """  # noqa: E501
        self._org = org

    @property
    def bucket(self):
        """Get the bucket of this OnboardingResponse.

        :return: The bucket of this OnboardingResponse.
        :rtype: Bucket
        """  # noqa: E501
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Set the bucket of this OnboardingResponse.

        :param bucket: The bucket of this OnboardingResponse.
        :type: Bucket
        """  # noqa: E501
        self._bucket = bucket

    @property
    def auth(self):
        """Get the auth of this OnboardingResponse.

        :return: The auth of this OnboardingResponse.
        :rtype: Authorization
        """  # noqa: E501
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Set the auth of this OnboardingResponse.

        :param auth: The auth of this OnboardingResponse.
        :type: Authorization
        """  # noqa: E501
        self._auth = auth

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
        if not isinstance(other, OnboardingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
