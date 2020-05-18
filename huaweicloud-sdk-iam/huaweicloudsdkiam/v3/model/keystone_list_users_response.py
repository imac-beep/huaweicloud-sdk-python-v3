# coding: utf-8

import pprint
import re

import six


class KeystoneListUsersResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'links': 'Links',
        'users': 'list[KeystoneUserResult]'
    }

    attribute_map = {
        'links': 'links',
        'users': 'users'
    }

    def __init__(self, links=None, users=None):  # noqa: E501
        """KeystoneListUsersResponse - a model defined in huaweicloud sdk"""

        self._links = None
        self._users = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if users is not None:
            self.users = users

    @property
    def links(self):
        """Gets the links of this KeystoneListUsersResponse.


        :return: The links of this KeystoneListUsersResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListUsersResponse.


        :param links: The links of this KeystoneListUsersResponse.
        :type: Links
        """
        self._links = links

    @property
    def users(self):
        """Gets the users of this KeystoneListUsersResponse.

        IAM用户信息列表。

        :return: The users of this KeystoneListUsersResponse.
        :rtype: list[KeystoneUserResult]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this KeystoneListUsersResponse.

        IAM用户信息列表。

        :param users: The users of this KeystoneListUsersResponse.
        :type: list[KeystoneUserResult]
        """
        self._users = users

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
        if not isinstance(other, KeystoneListUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other