# coding: utf-8

import pprint
import re

import six


class NeutronUpdateFirewallPolicyRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'firewall_policy': 'NeutronUpdateFirewallPolicyOption'
    }

    attribute_map = {
        'firewall_policy': 'firewall_policy'
    }

    def __init__(self, firewall_policy=None):  # noqa: E501
        """NeutronUpdateFirewallPolicyRequestBody - a model defined in huaweicloud sdk"""

        self._firewall_policy = None
        self.discriminator = None

        self.firewall_policy = firewall_policy

    @property
    def firewall_policy(self):
        """Gets the firewall_policy of this NeutronUpdateFirewallPolicyRequestBody.


        :return: The firewall_policy of this NeutronUpdateFirewallPolicyRequestBody.
        :rtype: NeutronUpdateFirewallPolicyOption
        """
        return self._firewall_policy

    @firewall_policy.setter
    def firewall_policy(self, firewall_policy):
        """Sets the firewall_policy of this NeutronUpdateFirewallPolicyRequestBody.


        :param firewall_policy: The firewall_policy of this NeutronUpdateFirewallPolicyRequestBody.
        :type: NeutronUpdateFirewallPolicyOption
        """
        self._firewall_policy = firewall_policy

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
        if not isinstance(other, NeutronUpdateFirewallPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other