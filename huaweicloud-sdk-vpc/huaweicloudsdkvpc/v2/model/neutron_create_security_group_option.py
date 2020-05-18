# coding: utf-8

import pprint
import re

import six


class NeutronCreateSecurityGroupOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, description=None, name=None):  # noqa: E501
        """NeutronCreateSecurityGroupOption - a model defined in huaweicloud sdk"""

        self._description = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this NeutronCreateSecurityGroupOption.

        功能说明：安全组描述 取值范围：0-255个字符

        :return: The description of this NeutronCreateSecurityGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronCreateSecurityGroupOption.

        功能说明：安全组描述 取值范围：0-255个字符

        :param description: The description of this NeutronCreateSecurityGroupOption.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this NeutronCreateSecurityGroupOption.

        功能说明：安全组名称 取值范围：0-255个字符 约束：不允许为“default”

        :return: The name of this NeutronCreateSecurityGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreateSecurityGroupOption.

        功能说明：安全组名称 取值范围：0-255个字符 约束：不允许为“default”

        :param name: The name of this NeutronCreateSecurityGroupOption.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, NeutronCreateSecurityGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other