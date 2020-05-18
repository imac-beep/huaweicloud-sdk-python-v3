# coding: utf-8

import pprint
import re

import six


class GlanceShowImageMemberRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'image_id': 'str',
        'member_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'member_id': 'member_id'
    }

    def __init__(self, image_id=None, member_id=None):  # noqa: E501
        """GlanceShowImageMemberRequest - a model defined in huaweicloud sdk"""

        self._image_id = None
        self._member_id = None
        self.discriminator = None

        self.image_id = image_id
        self.member_id = member_id

    @property
    def image_id(self):
        """Gets the image_id of this GlanceShowImageMemberRequest.


        :return: The image_id of this GlanceShowImageMemberRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this GlanceShowImageMemberRequest.


        :param image_id: The image_id of this GlanceShowImageMemberRequest.
        :type: str
        """
        self._image_id = image_id

    @property
    def member_id(self):
        """Gets the member_id of this GlanceShowImageMemberRequest.


        :return: The member_id of this GlanceShowImageMemberRequest.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this GlanceShowImageMemberRequest.


        :param member_id: The member_id of this GlanceShowImageMemberRequest.
        :type: str
        """
        self._member_id = member_id

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
        if not isinstance(other, GlanceShowImageMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other