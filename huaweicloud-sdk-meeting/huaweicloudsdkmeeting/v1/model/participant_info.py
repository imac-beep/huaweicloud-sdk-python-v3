# coding: utf-8

import pprint
import re

import six





class ParticipantInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'name': 'str',
        'subscriber_id': 'str',
        'role': 'int',
        'state': 'str',
        'address': 'str',
        'attendee_type': 'str',
        'account_id': 'str',
        'phone2': 'str',
        'phone3': 'str',
        'email': 'str',
        'sms': 'str',
        'dept_name': 'str',
        'user_uuid': 'str'
    }

    attribute_map = {
        'participant_id': 'participantID',
        'name': 'name',
        'subscriber_id': 'subscriberID',
        'role': 'role',
        'state': 'state',
        'address': 'address',
        'attendee_type': 'attendeeType',
        'account_id': 'accountId',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'email': 'email',
        'sms': 'sms',
        'dept_name': 'deptName',
        'user_uuid': 'userUUID'
    }

    def __init__(self, participant_id=None, name=None, subscriber_id=None, role=None, state=None, address=None, attendee_type=None, account_id=None, phone2=None, phone3=None, email=None, sms=None, dept_name=None, user_uuid=None):
        """ParticipantInfo - a model defined in huaweicloud sdk"""
        
        

        self._participant_id = None
        self._name = None
        self._subscriber_id = None
        self._role = None
        self._state = None
        self._address = None
        self._attendee_type = None
        self._account_id = None
        self._phone2 = None
        self._phone3 = None
        self._email = None
        self._sms = None
        self._dept_name = None
        self._user_uuid = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        if name is not None:
            self.name = name
        if subscriber_id is not None:
            self.subscriber_id = subscriber_id
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if address is not None:
            self.address = address
        if attendee_type is not None:
            self.attendee_type = attendee_type
        if account_id is not None:
            self.account_id = account_id
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms
        if dept_name is not None:
            self.dept_name = dept_name
        if user_uuid is not None:
            self.user_uuid = user_uuid

    @property
    def participant_id(self):
        """Gets the participant_id of this ParticipantInfo.

        与会者的号码。

        :return: The participant_id of this ParticipantInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this ParticipantInfo.

        与会者的号码。

        :param participant_id: The participant_id of this ParticipantInfo.
        :type: str
        """
        self._participant_id = participant_id

    @property
    def name(self):
        """Gets the name of this ParticipantInfo.

        与会者的名称（昵称）。

        :return: The name of this ParticipantInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParticipantInfo.

        与会者的名称（昵称）。

        :param name: The name of this ParticipantInfo.
        :type: str
        """
        self._name = name

    @property
    def subscriber_id(self):
        """Gets the subscriber_id of this ParticipantInfo.

        与会者的号码（预留字段）。

        :return: The subscriber_id of this ParticipantInfo.
        :rtype: str
        """
        return self._subscriber_id

    @subscriber_id.setter
    def subscriber_id(self, subscriber_id):
        """Sets the subscriber_id of this ParticipantInfo.

        与会者的号码（预留字段）。

        :param subscriber_id: The subscriber_id of this ParticipantInfo.
        :type: str
        """
        self._subscriber_id = subscriber_id

    @property
    def role(self):
        """Gets the role of this ParticipantInfo.

        会议中的角色。 - 1: 会议主持人。 - 0: 普通与会者。

        :return: The role of this ParticipantInfo.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ParticipantInfo.

        会议中的角色。 - 1: 会议主持人。 - 0: 普通与会者。

        :param role: The role of this ParticipantInfo.
        :type: int
        """
        self._role = role

    @property
    def state(self):
        """Gets the state of this ParticipantInfo.

        用户状态。目前固定返回MEETTING。

        :return: The state of this ParticipantInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ParticipantInfo.

        用户状态。目前固定返回MEETTING。

        :param state: The state of this ParticipantInfo.
        :type: str
        """
        self._state = state

    @property
    def address(self):
        """Gets the address of this ParticipantInfo.

        终端所在会议室信息。（预留字段）

        :return: The address of this ParticipantInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ParticipantInfo.

        终端所在会议室信息。（预留字段）

        :param address: The address of this ParticipantInfo.
        :type: str
        """
        self._address = address

    @property
    def attendee_type(self):
        """Gets the attendee_type of this ParticipantInfo.

        - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 用户固定电话。（预留字段）

        :return: The attendee_type of this ParticipantInfo.
        :rtype: str
        """
        return self._attendee_type

    @attendee_type.setter
    def attendee_type(self, attendee_type):
        """Sets the attendee_type of this ParticipantInfo.

        - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 用户固定电话。（预留字段）

        :param attendee_type: The attendee_type of this ParticipantInfo.
        :type: str
        """
        self._attendee_type = attendee_type

    @property
    def account_id(self):
        """Gets the account_id of this ParticipantInfo.

        预订者的账号ID。

        :return: The account_id of this ParticipantInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ParticipantInfo.

        预订者的账号ID。

        :param account_id: The account_id of this ParticipantInfo.
        :type: str
        """
        self._account_id = account_id

    @property
    def phone2(self):
        """Gets the phone2 of this ParticipantInfo.

        当attendeeType为telepresence时，且设备为三屏智真，则该字段填写左屏号码。（预留字段）

        :return: The phone2 of this ParticipantInfo.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this ParticipantInfo.

        当attendeeType为telepresence时，且设备为三屏智真，则该字段填写左屏号码。（预留字段）

        :param phone2: The phone2 of this ParticipantInfo.
        :type: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this ParticipantInfo.

        当attendeeType为telepresence时，且设备为三屏智真，则该字段填写右屏号码。（预留字段）

        :return: The phone3 of this ParticipantInfo.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this ParticipantInfo.

        当attendeeType为telepresence时，且设备为三屏智真，则该字段填写右屏号码。（预留字段）

        :param phone3: The phone3 of this ParticipantInfo.
        :type: str
        """
        self._phone3 = phone3

    @property
    def email(self):
        """Gets the email of this ParticipantInfo.

        邮件地址。最大不超过255个字符。

        :return: The email of this ParticipantInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParticipantInfo.

        邮件地址。最大不超过255个字符。

        :param email: The email of this ParticipantInfo.
        :type: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this ParticipantInfo.

        短信通知的手机号码。最大不超过127个字符。

        :return: The sms of this ParticipantInfo.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this ParticipantInfo.

        短信通知的手机号码。最大不超过127个字符。

        :param sms: The sms of this ParticipantInfo.
        :type: str
        """
        self._sms = sms

    @property
    def dept_name(self):
        """Gets the dept_name of this ParticipantInfo.

        部门名称。最大不超过96个字符。

        :return: The dept_name of this ParticipantInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ParticipantInfo.

        部门名称。最大不超过96个字符。

        :param dept_name: The dept_name of this ParticipantInfo.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ParticipantInfo.

        预订者的用户UUID。

        :return: The user_uuid of this ParticipantInfo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ParticipantInfo.

        预订者的用户UUID。

        :param user_uuid: The user_uuid of this ParticipantInfo.
        :type: str
        """
        self._user_uuid = user_uuid

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
        if not isinstance(other, ParticipantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other