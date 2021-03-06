# coding: utf-8

import pprint
import re

import six





class MaintainWindows:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'seq': 'int',
        'default': 'bool',
        'begin': 'str',
        'end': 'str'
    }

    attribute_map = {
        'seq': 'seq',
        'default': 'default',
        'begin': 'begin',
        'end': 'end'
    }

    def __init__(self, seq=None, default=None, begin=None, end=None):
        """MaintainWindows - a model defined in huaweicloud sdk"""
        
        

        self._seq = None
        self._default = None
        self._begin = None
        self._end = None
        self.discriminator = None

        if seq is not None:
            self.seq = seq
        if default is not None:
            self.default = default
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end

    @property
    def seq(self):
        """Gets the seq of this MaintainWindows.

        序号。

        :return: The seq of this MaintainWindows.
        :rtype: int
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        """Sets the seq of this MaintainWindows.

        序号。

        :param seq: The seq of this MaintainWindows.
        :type: int
        """
        self._seq = seq

    @property
    def default(self):
        """Gets the default of this MaintainWindows.

        是否为默认时间段。

        :return: The default of this MaintainWindows.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this MaintainWindows.

        是否为默认时间段。

        :param default: The default of this MaintainWindows.
        :type: bool
        """
        self._default = default

    @property
    def begin(self):
        """Gets the begin of this MaintainWindows.

        维护时间窗开始时间

        :return: The begin of this MaintainWindows.
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this MaintainWindows.

        维护时间窗开始时间

        :param begin: The begin of this MaintainWindows.
        :type: str
        """
        self._begin = begin

    @property
    def end(self):
        """Gets the end of this MaintainWindows.

        维护时间窗结束时间。

        :return: The end of this MaintainWindows.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MaintainWindows.

        维护时间窗结束时间。

        :param end: The end of this MaintainWindows.
        :type: str
        """
        self._end = end

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, MaintainWindows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
