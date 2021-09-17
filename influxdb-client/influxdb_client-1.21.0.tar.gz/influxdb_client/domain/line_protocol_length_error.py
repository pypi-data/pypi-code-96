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


class LineProtocolLengthError(object):
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
        'code': 'str',
        'message': 'str',
        'max_length': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'max_length': 'maxLength'
    }

    def __init__(self, code=None, message=None, max_length=None):  # noqa: E501,D401,D403
        """LineProtocolLengthError - a model defined in OpenAPI."""  # noqa: E501
        self._code = None
        self._message = None
        self._max_length = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.max_length = max_length

    @property
    def code(self):
        """Get the code of this LineProtocolLengthError.

        Code is the machine-readable error code.

        :return: The code of this LineProtocolLengthError.
        :rtype: str
        """  # noqa: E501
        return self._code

    @code.setter
    def code(self, code):
        """Set the code of this LineProtocolLengthError.

        Code is the machine-readable error code.

        :param code: The code of this LineProtocolLengthError.
        :type: str
        """  # noqa: E501
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        self._code = code

    @property
    def message(self):
        """Get the message of this LineProtocolLengthError.

        Message is a human-readable message.

        :return: The message of this LineProtocolLengthError.
        :rtype: str
        """  # noqa: E501
        return self._message

    @message.setter
    def message(self, message):
        """Set the message of this LineProtocolLengthError.

        Message is a human-readable message.

        :param message: The message of this LineProtocolLengthError.
        :type: str
        """  # noqa: E501
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        self._message = message

    @property
    def max_length(self):
        """Get the max_length of this LineProtocolLengthError.

        Max length in bytes for a body of line-protocol.

        :return: The max_length of this LineProtocolLengthError.
        :rtype: int
        """  # noqa: E501
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Set the max_length of this LineProtocolLengthError.

        Max length in bytes for a body of line-protocol.

        :param max_length: The max_length of this LineProtocolLengthError.
        :type: int
        """  # noqa: E501
        if max_length is None:
            raise ValueError("Invalid value for `max_length`, must not be `None`")  # noqa: E501
        self._max_length = max_length

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
        if not isinstance(other, LineProtocolLengthError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
