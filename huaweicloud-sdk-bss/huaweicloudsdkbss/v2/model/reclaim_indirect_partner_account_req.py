# coding: utf-8

import pprint
import re

import six





class ReclaimIndirectPartnerAccountReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'amount': 'float',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, amount=None, indirect_partner_id=None):
        """ReclaimIndirectPartnerAccountReq - a model defined in huaweicloud sdk"""
        
        

        self._amount = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.amount = amount
        self.indirect_partner_id = indirect_partner_id

    @property
    def amount(self):
        """Gets the amount of this ReclaimIndirectPartnerAccountReq.

        |参数名称：拨款金额。单位为元。不能为负数，精确到小数点后两位。| |参数的约束及描述：拨款金额。单位为元。不能为负数，浮点数精度为:小数点后两位。|

        :return: The amount of this ReclaimIndirectPartnerAccountReq.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReclaimIndirectPartnerAccountReq.

        |参数名称：拨款金额。单位为元。不能为负数，精确到小数点后两位。| |参数的约束及描述：拨款金额。单位为元。不能为负数，浮点数精度为:小数点后两位。|

        :param amount: The amount of this ReclaimIndirectPartnerAccountReq.
        :type: float
        """
        self._amount = amount

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ReclaimIndirectPartnerAccountReq.

        |参数名称：精英服务商伙伴的ID。| |参数约束及描述：精英服务商伙伴的ID。|

        :return: The indirect_partner_id of this ReclaimIndirectPartnerAccountReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ReclaimIndirectPartnerAccountReq.

        |参数名称：精英服务商伙伴的ID。| |参数约束及描述：精英服务商伙伴的ID。|

        :param indirect_partner_id: The indirect_partner_id of this ReclaimIndirectPartnerAccountReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ReclaimIndirectPartnerAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
