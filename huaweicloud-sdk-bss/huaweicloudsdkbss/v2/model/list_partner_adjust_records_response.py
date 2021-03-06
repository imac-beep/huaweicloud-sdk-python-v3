# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPartnerAdjustRecordsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'records': 'list[AdjustRecordV2]',
        'total_count': 'int'
    }

    attribute_map = {
        'records': 'records',
        'total_count': 'total_count'
    }

    def __init__(self, records=None, total_count=None):
        """ListPartnerAdjustRecordsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._records = None
        self._total_count = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if total_count is not None:
            self.total_count = total_count

    @property
    def records(self):
        """Gets the records of this ListPartnerAdjustRecordsResponse.

        |参数名称：调账记录列表。具体请参见表 AdjustRecordV2。| |参数约束以及描述：调账记录列表。具体请参见表 AdjustRecordV2。|

        :return: The records of this ListPartnerAdjustRecordsResponse.
        :rtype: list[AdjustRecordV2]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListPartnerAdjustRecordsResponse.

        |参数名称：调账记录列表。具体请参见表 AdjustRecordV2。| |参数约束以及描述：调账记录列表。具体请参见表 AdjustRecordV2。|

        :param records: The records of this ListPartnerAdjustRecordsResponse.
        :type: list[AdjustRecordV2]
        """
        self._records = records

    @property
    def total_count(self):
        """Gets the total_count of this ListPartnerAdjustRecordsResponse.

        |参数名称：返回总条数。| |参数的约束及描述：返回总条数。|

        :return: The total_count of this ListPartnerAdjustRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPartnerAdjustRecordsResponse.

        |参数名称：返回总条数。| |参数的约束及描述：返回总条数。|

        :param total_count: The total_count of this ListPartnerAdjustRecordsResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListPartnerAdjustRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
