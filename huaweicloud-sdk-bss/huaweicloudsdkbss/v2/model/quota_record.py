# coding: utf-8

import pprint
import re

import six





class QuotaRecord:


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
        'id': 'str',
        'indirect_partner_account_name': 'str',
        'indirect_partner_id': 'str',
        'indirect_partner_name': 'str',
        'operation_time': 'str',
        'operation_type': 'str',
        'operator': 'str',
        'parent_quota_id': 'str',
        'quota_id': 'str',
        'remark': 'str',
        'result': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'id': 'id',
        'indirect_partner_account_name': 'indirect_partner_account_name',
        'indirect_partner_id': 'indirect_partner_id',
        'indirect_partner_name': 'indirect_partner_name',
        'operation_time': 'operation_time',
        'operation_type': 'operation_type',
        'operator': 'operator',
        'parent_quota_id': 'parent_quota_id',
        'quota_id': 'quota_id',
        'remark': 'remark',
        'result': 'result'
    }

    def __init__(self, amount=None, id=None, indirect_partner_account_name=None, indirect_partner_id=None, indirect_partner_name=None, operation_time=None, operation_type=None, operator=None, parent_quota_id=None, quota_id=None, remark=None, result=None):
        """QuotaRecord - a model defined in huaweicloud sdk"""
        
        

        self._amount = None
        self._id = None
        self._indirect_partner_account_name = None
        self._indirect_partner_id = None
        self._indirect_partner_name = None
        self._operation_time = None
        self._operation_type = None
        self._operator = None
        self._parent_quota_id = None
        self._quota_id = None
        self._remark = None
        self._result = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if id is not None:
            self.id = id
        if indirect_partner_account_name is not None:
            self.indirect_partner_account_name = indirect_partner_account_name
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if indirect_partner_name is not None:
            self.indirect_partner_name = indirect_partner_name
        if operation_time is not None:
            self.operation_time = operation_time
        if operation_type is not None:
            self.operation_type = operation_type
        if operator is not None:
            self.operator = operator
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id
        if quota_id is not None:
            self.quota_id = quota_id
        if remark is not None:
            self.remark = remark
        if result is not None:
            self.result = result

    @property
    def amount(self):
        """Gets the amount of this QuotaRecord.

        |参数名称：发放回收的金额，小数点后2位，单位元| |参数的约束及描述：发放回收的金额，小数点后2位，单位元|

        :return: The amount of this QuotaRecord.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this QuotaRecord.

        |参数名称：发放回收的金额，小数点后2位，单位元| |参数的约束及描述：发放回收的金额，小数点后2位，单位元|

        :param amount: The amount of this QuotaRecord.
        :type: float
        """
        self._amount = amount

    @property
    def id(self):
        """Gets the id of this QuotaRecord.

        |参数名称：记录ID| |参数约束及描述：记录ID|

        :return: The id of this QuotaRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaRecord.

        |参数名称：记录ID| |参数约束及描述：记录ID|

        :param id: The id of this QuotaRecord.
        :type: str
        """
        self._id = id

    @property
    def indirect_partner_account_name(self):
        """Gets the indirect_partner_account_name of this QuotaRecord.

        |参数名称：二级经销商的管理员账号名| |参数约束及描述：二级经销商的管理员账号名|

        :return: The indirect_partner_account_name of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_account_name

    @indirect_partner_account_name.setter
    def indirect_partner_account_name(self, indirect_partner_account_name):
        """Sets the indirect_partner_account_name of this QuotaRecord.

        |参数名称：二级经销商的管理员账号名| |参数约束及描述：二级经销商的管理员账号名|

        :param indirect_partner_account_name: The indirect_partner_account_name of this QuotaRecord.
        :type: str
        """
        self._indirect_partner_account_name = indirect_partner_account_name

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QuotaRecord.

        |参数名称：二级经销商ID| |参数约束及描述：二级经销商ID|

        :return: The indirect_partner_id of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QuotaRecord.

        |参数名称：二级经销商ID| |参数约束及描述：二级经销商ID|

        :param indirect_partner_id: The indirect_partner_id of this QuotaRecord.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def indirect_partner_name(self):
        """Gets the indirect_partner_name of this QuotaRecord.

        |参数名称：二级经销商的公司名称| |参数约束及描述：二级经销商的公司名称|

        :return: The indirect_partner_name of this QuotaRecord.
        :rtype: str
        """
        return self._indirect_partner_name

    @indirect_partner_name.setter
    def indirect_partner_name(self, indirect_partner_name):
        """Sets the indirect_partner_name of this QuotaRecord.

        |参数名称：二级经销商的公司名称| |参数约束及描述：二级经销商的公司名称|

        :param indirect_partner_name: The indirect_partner_name of this QuotaRecord.
        :type: str
        """
        self._indirect_partner_name = indirect_partner_name

    @property
    def operation_time(self):
        """Gets the operation_time of this QuotaRecord.

        |参数名称：操作时间，UTC时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：操作时间，UTC时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The operation_time of this QuotaRecord.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        """Sets the operation_time of this QuotaRecord.

        |参数名称：操作时间，UTC时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：操作时间，UTC时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param operation_time: The operation_time of this QuotaRecord.
        :type: str
        """
        self._operation_time = operation_time

    @property
    def operation_type(self):
        """Gets the operation_type of this QuotaRecord.

        |参数名称：操作类型10：发放额度11：回收额度| |参数约束及描述：操作类型10：发放额度11：回收额度|

        :return: The operation_type of this QuotaRecord.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this QuotaRecord.

        |参数名称：操作类型10：发放额度11：回收额度| |参数约束及描述：操作类型10：发放额度11：回收额度|

        :param operation_type: The operation_type of this QuotaRecord.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def operator(self):
        """Gets the operator of this QuotaRecord.

        |参数名称：操作员额账号名称| |参数约束及描述：操作员额账号名称|

        :return: The operator of this QuotaRecord.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QuotaRecord.

        |参数名称：操作员额账号名称| |参数约束及描述：操作员额账号名称|

        :param operator: The operator of this QuotaRecord.
        :type: str
        """
        self._operator = operator

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this QuotaRecord.

        |参数名称：父额度ID，这里指的是一级经销商发给二级经销商额度时，一级经销商的额度ID，或者从二级经销商回收的时候，回收到的一级经销商的额度ID| |参数约束及描述：父额度ID，这里指的是一级经销商发给二级经销商额度时，一级经销商的额度ID，或者从二级经销商回收的时候，回收到的一级经销商的额度ID|

        :return: The parent_quota_id of this QuotaRecord.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this QuotaRecord.

        |参数名称：父额度ID，这里指的是一级经销商发给二级经销商额度时，一级经销商的额度ID，或者从二级经销商回收的时候，回收到的一级经销商的额度ID| |参数约束及描述：父额度ID，这里指的是一级经销商发给二级经销商额度时，一级经销商的额度ID，或者从二级经销商回收的时候，回收到的一级经销商的额度ID|

        :param parent_quota_id: The parent_quota_id of this QuotaRecord.
        :type: str
        """
        self._parent_quota_id = parent_quota_id

    @property
    def quota_id(self):
        """Gets the quota_id of this QuotaRecord.

        |参数名称：额度ID，这里指的是一级经销商发给二级经销商额度时，产生的二级经销商的额度ID，或者从二级经销商回收的时候，二级经销商的额度ID| |参数约束及描述：额度ID，这里指的是一级经销商发给二级经销商额度时，产生的二级经销商的额度ID，或者从二级经销商回收的时候，二级经销商的额度ID|

        :return: The quota_id of this QuotaRecord.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this QuotaRecord.

        |参数名称：额度ID，这里指的是一级经销商发给二级经销商额度时，产生的二级经销商的额度ID，或者从二级经销商回收的时候，二级经销商的额度ID| |参数约束及描述：额度ID，这里指的是一级经销商发给二级经销商额度时，产生的二级经销商的额度ID，或者从二级经销商回收的时候，二级经销商的额度ID|

        :param quota_id: The quota_id of this QuotaRecord.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def remark(self):
        """Gets the remark of this QuotaRecord.

        |参数名称：备注| |参数约束及描述：备注|

        :return: The remark of this QuotaRecord.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this QuotaRecord.

        |参数名称：备注| |参数约束及描述：备注|

        :param remark: The remark of this QuotaRecord.
        :type: str
        """
        self._remark = remark

    @property
    def result(self):
        """Gets the result of this QuotaRecord.

        |参数名称：操作结果0：成功-1：失败| |参数约束及描述：操作结果0：成功-1：失败|

        :return: The result of this QuotaRecord.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QuotaRecord.

        |参数名称：操作结果0：成功-1：失败| |参数约束及描述：操作结果0：成功-1：失败|

        :param result: The result of this QuotaRecord.
        :type: str
        """
        self._result = result

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
        if not isinstance(other, QuotaRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
