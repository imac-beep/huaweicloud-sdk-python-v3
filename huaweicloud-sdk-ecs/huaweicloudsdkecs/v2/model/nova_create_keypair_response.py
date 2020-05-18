# coding: utf-8

import pprint
import re

import six


class NovaCreateKeypairResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'keypair': 'NovaKeypair'
    }

    attribute_map = {
        'keypair': 'keypair'
    }

    def __init__(self, keypair=None):  # noqa: E501
        """NovaCreateKeypairResponse - a model defined in huaweicloud sdk"""

        self._keypair = None
        self.discriminator = None

        if keypair is not None:
            self.keypair = keypair

    @property
    def keypair(self):
        """Gets the keypair of this NovaCreateKeypairResponse.


        :return: The keypair of this NovaCreateKeypairResponse.
        :rtype: NovaKeypair
        """
        return self._keypair

    @keypair.setter
    def keypair(self, keypair):
        """Sets the keypair of this NovaCreateKeypairResponse.


        :param keypair: The keypair of this NovaCreateKeypairResponse.
        :type: NovaKeypair
        """
        self._keypair = keypair

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
        if not isinstance(other, NovaCreateKeypairResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other