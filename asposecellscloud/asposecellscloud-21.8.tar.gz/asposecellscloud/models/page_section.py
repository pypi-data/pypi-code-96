# coding: utf-8

"""
Copyright (c) 2021 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from pprint import pformat
from six import iteritems
import re


class PageSection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'picture': 'str',
        'section': 'int',
        'fisrt_page_context': 'str',
        'context': 'str',
        'even_page_context': 'str'
    }

    attribute_map = {
        'picture': 'Picture',
        'section': 'Section',
        'fisrt_page_context': 'FisrtPageContext',
        'context': 'Context',
        'even_page_context': 'EvenPageContext'
    }
    
    @staticmethod
    def get_swagger_types():
        return PageSection.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PageSection.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, picture=None, section=None, fisrt_page_context=None, context=None, even_page_context=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PageSection - a model defined in Swagger
        """

        self.container['picture'] = None
        self.container['section'] = None
        self.container['fisrt_page_context'] = None
        self.container['context'] = None
        self.container['even_page_context'] = None

        if picture is not None:
          self.picture = picture
        self.section = section
        if fisrt_page_context is not None:
          self.fisrt_page_context = fisrt_page_context
        if context is not None:
          self.context = context
        if even_page_context is not None:
          self.even_page_context = even_page_context

    @property
    def picture(self):
        """
        Gets the picture of this PageSection.

        :return: The picture of this PageSection.
        :rtype: str
        """
        return self.container['picture']

    @picture.setter
    def picture(self, picture):
        """
        Sets the picture of this PageSection.

        :param picture: The picture of this PageSection.
        :type: str
        """
        if picture is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', picture):
            raise ValueError("Invalid value for `picture`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self.container['picture'] = picture

    @property
    def section(self):
        """
        Gets the section of this PageSection.
        0,1,2  left , middle ,right

        :return: The section of this PageSection.
        :rtype: int
        """
        return self.container['section']

    @section.setter
    def section(self, section):
        """
        Sets the section of this PageSection.
        0,1,2  left , middle ,right

        :param section: The section of this PageSection.
        :type: int
        """
        """
        if section is None:
            raise ValueError("Invalid value for `section`, must not be `None`")
        """

        self.container['section'] = section

    @property
    def fisrt_page_context(self):
        """
        Gets the fisrt_page_context of this PageSection.
        fisrt page context script

        :return: The fisrt_page_context of this PageSection.
        :rtype: str
        """
        return self.container['fisrt_page_context']

    @fisrt_page_context.setter
    def fisrt_page_context(self, fisrt_page_context):
        """
        Sets the fisrt_page_context of this PageSection.
        fisrt page context script

        :param fisrt_page_context: The fisrt_page_context of this PageSection.
        :type: str
        """

        self.container['fisrt_page_context'] = fisrt_page_context

    @property
    def context(self):
        """
        Gets the context of this PageSection.
        page context script             

        :return: The context of this PageSection.
        :rtype: str
        """
        return self.container['context']

    @context.setter
    def context(self, context):
        """
        Sets the context of this PageSection.
        page context script             

        :param context: The context of this PageSection.
        :type: str
        """

        self.container['context'] = context

    @property
    def even_page_context(self):
        """
        Gets the even_page_context of this PageSection.
        Even page context script

        :return: The even_page_context of this PageSection.
        :rtype: str
        """
        return self.container['even_page_context']

    @even_page_context.setter
    def even_page_context(self, even_page_context):
        """
        Sets the even_page_context of this PageSection.
        Even page context script

        :param even_page_context: The even_page_context of this PageSection.
        :type: str
        """

        self.container['even_page_context'] = even_page_context

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PageSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
