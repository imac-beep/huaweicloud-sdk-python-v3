# coding: utf-8

import pprint
import re

import six





class BackendParamBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'origin': 'str',
        'name': 'str',
        'remark': 'str',
        'location': 'str',
        'value': 'str'
    }

    attribute_map = {
        'origin': 'origin',
        'name': 'name',
        'remark': 'remark',
        'location': 'location',
        'value': 'value'
    }

    def __init__(self, origin=None, name=None, remark=None, location=None, value=None):
        """BackendParamBase - a model defined in huaweicloud sdk"""
        
        

        self._origin = None
        self._name = None
        self._remark = None
        self._location = None
        self._value = None
        self.discriminator = None

        self.origin = origin
        self.name = name
        if remark is not None:
            self.remark = remark
        self.location = location
        self.value = value

    @property
    def origin(self):
        """Gets the origin of this BackendParamBase.

        参数类别：REQUEST、CONSTANT、SYSTEM

        :return: The origin of this BackendParamBase.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BackendParamBase.

        参数类别：REQUEST、CONSTANT、SYSTEM

        :param origin: The origin of this BackendParamBase.
        :type: str
        """
        self._origin = origin

    @property
    def name(self):
        """Gets the name of this BackendParamBase.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :return: The name of this BackendParamBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendParamBase.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :param name: The name of this BackendParamBase.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this BackendParamBase.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this BackendParamBase.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackendParamBase.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this BackendParamBase.
        :type: str
        """
        self._remark = remark

    @property
    def location(self):
        """Gets the location of this BackendParamBase.

        参数位置：PATH、QUERY、HEADER

        :return: The location of this BackendParamBase.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BackendParamBase.

        参数位置：PATH、QUERY、HEADER

        :param location: The location of this BackendParamBase.
        :type: str
        """
        self._location = location

    @property
    def value(self):
        """Gets the value of this BackendParamBase.

        参数值。字符长度不超过255，类别为REQUEST时，值为req_params中的参数名称；类别为CONSTANT时，值为参数真正的值；类别为SYSTEM时，值为网关参数名称

        :return: The value of this BackendParamBase.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BackendParamBase.

        参数值。字符长度不超过255，类别为REQUEST时，值为req_params中的参数名称；类别为CONSTANT时，值为参数真正的值；类别为SYSTEM时，值为网关参数名称

        :param value: The value of this BackendParamBase.
        :type: str
        """
        self._value = value

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
        if not isinstance(other, BackendParamBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
