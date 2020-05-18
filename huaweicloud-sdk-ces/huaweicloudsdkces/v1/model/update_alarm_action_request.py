# coding: utf-8

import pprint
import re

import six


class UpdateAlarmActionRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'content_type': 'str',
        'alarm_id': 'str',
        'body': 'ModifyAlarmActionReq'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'alarm_id': 'alarm_id',
        'body': 'body'
    }

    def __init__(self, content_type='application/json; charset=UTF-8', alarm_id='al15454523384878yogJg6ao', body=None):  # noqa: E501
        """UpdateAlarmActionRequest - a model defined in huaweicloud sdk"""

        self._content_type = None
        self._alarm_id = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        self.alarm_id = alarm_id
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        """Gets the content_type of this UpdateAlarmActionRequest.


        :return: The content_type of this UpdateAlarmActionRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateAlarmActionRequest.


        :param content_type: The content_type of this UpdateAlarmActionRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def alarm_id(self):
        """Gets the alarm_id of this UpdateAlarmActionRequest.


        :return: The alarm_id of this UpdateAlarmActionRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this UpdateAlarmActionRequest.


        :param alarm_id: The alarm_id of this UpdateAlarmActionRequest.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def body(self):
        """Gets the body of this UpdateAlarmActionRequest.


        :return: The body of this UpdateAlarmActionRequest.
        :rtype: ModifyAlarmActionReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAlarmActionRequest.


        :param body: The body of this UpdateAlarmActionRequest.
        :type: ModifyAlarmActionReq
        """
        self._body = body

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
        if not isinstance(other, UpdateAlarmActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other