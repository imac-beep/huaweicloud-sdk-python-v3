# coding: utf-8

import pprint
import re

import six


class Links(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        '_self': 'str',
        'previous': 'str',
        'next': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'previous': 'previous',
        'next': 'next'
    }

    def __init__(self, _self=None, previous=None, next=None):  # noqa: E501
        """Links - a model defined in huaweicloud sdk"""

        self.__self = None
        self._previous = None
        self._next = None
        self.discriminator = None

        self._self = _self
        self.previous = previous
        self.next = next

    @property
    def _self(self):
        """Gets the _self of this Links.

        资源链接地址。

        :return: The _self of this Links.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Links.

        资源链接地址。

        :param _self: The _self of this Links.
        :type: str
        """
        self.__self = _self

    @property
    def previous(self):
        """Gets the previous of this Links.

        前一邻接资源链接地址。

        :return: The previous of this Links.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this Links.

        前一邻接资源链接地址。

        :param previous: The previous of this Links.
        :type: str
        """
        self._previous = previous

    @property
    def next(self):
        """Gets the next of this Links.

        后一邻接资源链接地址。

        :return: The next of this Links.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Links.

        后一邻接资源链接地址。

        :param next: The next of this Links.
        :type: str
        """
        self._next = next

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other