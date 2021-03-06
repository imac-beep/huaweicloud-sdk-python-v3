# coding: utf-8

import pprint
import re

import six





class AmountInfomation:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_amount': 'float',
        'discounts': 'list[DiscountEntry]',
        'flexipurchase_coupon_amount': 'float',
        'stored_card_amount': 'float'
    }

    attribute_map = {
        'coupon_amount': 'coupon_amount',
        'discounts': 'discounts',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_card_amount': 'stored_card_amount'
    }

    def __init__(self, coupon_amount=None, discounts=None, flexipurchase_coupon_amount=None, stored_card_amount=None):
        """AmountInfomation - a model defined in huaweicloud sdk"""
        
        

        self._coupon_amount = None
        self._discounts = None
        self._flexipurchase_coupon_amount = None
        self._stored_card_amount = None
        self.discriminator = None

        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if discounts is not None:
            self.discounts = discounts
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_card_amount is not None:
            self.stored_card_amount = stored_card_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this AmountInfomation.

        |参数名称：代金券金额。| |参数的约束及描述：代金券金额。|

        :return: The coupon_amount of this AmountInfomation.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this AmountInfomation.

        |参数名称：代金券金额。| |参数的约束及描述：代金券金额。|

        :param coupon_amount: The coupon_amount of this AmountInfomation.
        :type: float
        """
        self._coupon_amount = coupon_amount

    @property
    def discounts(self):
        """Gets the discounts of this AmountInfomation.

        |参数名称：费用项。| |参数约束及描述： 费用项。|

        :return: The discounts of this AmountInfomation.
        :rtype: list[DiscountEntry]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this AmountInfomation.

        |参数名称：费用项。| |参数约束及描述： 费用项。|

        :param discounts: The discounts of this AmountInfomation.
        :type: list[DiscountEntry]
        """
        self._discounts = discounts

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this AmountInfomation.

        |参数名称：现金券金额。| |参数的约束及描述：现金券金额。|

        :return: The flexipurchase_coupon_amount of this AmountInfomation.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this AmountInfomation.

        |参数名称：现金券金额。| |参数的约束及描述：现金券金额。|

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this AmountInfomation.
        :type: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        """Gets the stored_card_amount of this AmountInfomation.

        |参数名称：储值卡金额。| |参数的约束及描述：储值卡金额。|

        :return: The stored_card_amount of this AmountInfomation.
        :rtype: float
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        """Sets the stored_card_amount of this AmountInfomation.

        |参数名称：储值卡金额。| |参数的约束及描述：储值卡金额。|

        :param stored_card_amount: The stored_card_amount of this AmountInfomation.
        :type: float
        """
        self._stored_card_amount = stored_card_amount

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
        if not isinstance(other, AmountInfomation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
