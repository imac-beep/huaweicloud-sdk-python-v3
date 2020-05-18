# coding: utf-8

import pprint
import re

import six


class ScalingGroups(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'scaling_group_name': 'str',
        'scaling_group_id': 'str',
        'scaling_group_status': 'str',
        'scaling_configuration_id': 'str',
        'scaling_configuration_name': 'str',
        'current_instance_number': 'int',
        'desire_instance_number': 'int',
        'min_instance_number': 'int',
        'max_instance_number': 'int',
        'cool_down_time': 'int',
        'lb_listener_id': 'str',
        'lbaas_listeners': 'list[LbaasListenersResult]',
        'available_zones': 'list[str]',
        'networks': 'list[Networks]',
        'security_groups': 'list[SecurityGroupsResult]',
        'create_time': 'datetime',
        'vpc_id': 'str',
        'detail': 'str',
        'is_scaling': 'bool',
        'health_periodic_audit_method': 'str',
        'health_periodic_audit_time': 'int',
        'health_periodic_audit_grace_period': 'int',
        'instance_terminate_policy': 'str',
        'notifications': 'list[str]',
        'delete_publicip': 'bool',
        'cloud_location_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'scaling_group_name': 'scaling_group_name',
        'scaling_group_id': 'scaling_group_id',
        'scaling_group_status': 'scaling_group_status',
        'scaling_configuration_id': 'scaling_configuration_id',
        'scaling_configuration_name': 'scaling_configuration_name',
        'current_instance_number': 'current_instance_number',
        'desire_instance_number': 'desire_instance_number',
        'min_instance_number': 'min_instance_number',
        'max_instance_number': 'max_instance_number',
        'cool_down_time': 'cool_down_time',
        'lb_listener_id': 'lb_listener_id',
        'lbaas_listeners': 'lbaas_listeners',
        'available_zones': 'available_zones',
        'networks': 'networks',
        'security_groups': 'security_groups',
        'create_time': 'create_time',
        'vpc_id': 'vpc_id',
        'detail': 'detail',
        'is_scaling': 'is_scaling',
        'health_periodic_audit_method': 'health_periodic_audit_method',
        'health_periodic_audit_time': 'health_periodic_audit_time',
        'health_periodic_audit_grace_period': 'health_periodic_audit_grace_period',
        'instance_terminate_policy': 'instance_terminate_policy',
        'notifications': 'notifications',
        'delete_publicip': 'delete_publicip',
        'cloud_location_id': 'cloud_location_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, scaling_group_name=None, scaling_group_id=None, scaling_group_status=None, scaling_configuration_id=None, scaling_configuration_name=None, current_instance_number=None, desire_instance_number=None, min_instance_number=None, max_instance_number=None, cool_down_time=None, lb_listener_id=None, lbaas_listeners=None, available_zones=None, networks=None, security_groups=None, create_time=None, vpc_id=None, detail=None, is_scaling=None, health_periodic_audit_method=None, health_periodic_audit_time=None, health_periodic_audit_grace_period=None, instance_terminate_policy=None, notifications=None, delete_publicip=None, cloud_location_id=None, enterprise_project_id=None):  # noqa: E501
        """ScalingGroups - a model defined in huaweicloud sdk"""

        self._scaling_group_name = None
        self._scaling_group_id = None
        self._scaling_group_status = None
        self._scaling_configuration_id = None
        self._scaling_configuration_name = None
        self._current_instance_number = None
        self._desire_instance_number = None
        self._min_instance_number = None
        self._max_instance_number = None
        self._cool_down_time = None
        self._lb_listener_id = None
        self._lbaas_listeners = None
        self._available_zones = None
        self._networks = None
        self._security_groups = None
        self._create_time = None
        self._vpc_id = None
        self._detail = None
        self._is_scaling = None
        self._health_periodic_audit_method = None
        self._health_periodic_audit_time = None
        self._health_periodic_audit_grace_period = None
        self._instance_terminate_policy = None
        self._notifications = None
        self._delete_publicip = None
        self._cloud_location_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_group_status is not None:
            self.scaling_group_status = scaling_group_status
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if current_instance_number is not None:
            self.current_instance_number = current_instance_number
        if desire_instance_number is not None:
            self.desire_instance_number = desire_instance_number
        if min_instance_number is not None:
            self.min_instance_number = min_instance_number
        if max_instance_number is not None:
            self.max_instance_number = max_instance_number
        if cool_down_time is not None:
            self.cool_down_time = cool_down_time
        if lb_listener_id is not None:
            self.lb_listener_id = lb_listener_id
        if lbaas_listeners is not None:
            self.lbaas_listeners = lbaas_listeners
        if available_zones is not None:
            self.available_zones = available_zones
        if networks is not None:
            self.networks = networks
        if security_groups is not None:
            self.security_groups = security_groups
        if create_time is not None:
            self.create_time = create_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if detail is not None:
            self.detail = detail
        if is_scaling is not None:
            self.is_scaling = is_scaling
        if health_periodic_audit_method is not None:
            self.health_periodic_audit_method = health_periodic_audit_method
        if health_periodic_audit_time is not None:
            self.health_periodic_audit_time = health_periodic_audit_time
        if health_periodic_audit_grace_period is not None:
            self.health_periodic_audit_grace_period = health_periodic_audit_grace_period
        if instance_terminate_policy is not None:
            self.instance_terminate_policy = instance_terminate_policy
        if notifications is not None:
            self.notifications = notifications
        if delete_publicip is not None:
            self.delete_publicip = delete_publicip
        if cloud_location_id is not None:
            self.cloud_location_id = cloud_location_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ScalingGroups.

        伸缩组名称。

        :return: The scaling_group_name of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ScalingGroups.

        伸缩组名称。

        :param scaling_group_name: The scaling_group_name of this ScalingGroups.
        :type: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingGroups.

        伸缩组ID。

        :return: The scaling_group_id of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingGroups.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ScalingGroups.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def scaling_group_status(self):
        """Gets the scaling_group_status of this ScalingGroups.

        伸缩组状态。

        :return: The scaling_group_status of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_group_status

    @scaling_group_status.setter
    def scaling_group_status(self, scaling_group_status):
        """Sets the scaling_group_status of this ScalingGroups.

        伸缩组状态。

        :param scaling_group_status: The scaling_group_status of this ScalingGroups.
        :type: str
        """
        self._scaling_group_status = scaling_group_status

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ScalingGroups.

        伸缩配置ID。

        :return: The scaling_configuration_id of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ScalingGroups.

        伸缩配置ID。

        :param scaling_configuration_id: The scaling_configuration_id of this ScalingGroups.
        :type: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ScalingGroups.

        伸缩配置名称。

        :return: The scaling_configuration_name of this ScalingGroups.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ScalingGroups.

        伸缩配置名称。

        :param scaling_configuration_name: The scaling_configuration_name of this ScalingGroups.
        :type: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def current_instance_number(self):
        """Gets the current_instance_number of this ScalingGroups.

        伸缩组中当前实例数。

        :return: The current_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._current_instance_number

    @current_instance_number.setter
    def current_instance_number(self, current_instance_number):
        """Sets the current_instance_number of this ScalingGroups.

        伸缩组中当前实例数。

        :param current_instance_number: The current_instance_number of this ScalingGroups.
        :type: int
        """
        self._current_instance_number = current_instance_number

    @property
    def desire_instance_number(self):
        """Gets the desire_instance_number of this ScalingGroups.

        伸缩组期望实例数。

        :return: The desire_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._desire_instance_number

    @desire_instance_number.setter
    def desire_instance_number(self, desire_instance_number):
        """Sets the desire_instance_number of this ScalingGroups.

        伸缩组期望实例数。

        :param desire_instance_number: The desire_instance_number of this ScalingGroups.
        :type: int
        """
        self._desire_instance_number = desire_instance_number

    @property
    def min_instance_number(self):
        """Gets the min_instance_number of this ScalingGroups.

        伸缩组最小实例数。

        :return: The min_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._min_instance_number

    @min_instance_number.setter
    def min_instance_number(self, min_instance_number):
        """Sets the min_instance_number of this ScalingGroups.

        伸缩组最小实例数。

        :param min_instance_number: The min_instance_number of this ScalingGroups.
        :type: int
        """
        self._min_instance_number = min_instance_number

    @property
    def max_instance_number(self):
        """Gets the max_instance_number of this ScalingGroups.

        伸缩组最大实例数

        :return: The max_instance_number of this ScalingGroups.
        :rtype: int
        """
        return self._max_instance_number

    @max_instance_number.setter
    def max_instance_number(self, max_instance_number):
        """Sets the max_instance_number of this ScalingGroups.

        伸缩组最大实例数

        :param max_instance_number: The max_instance_number of this ScalingGroups.
        :type: int
        """
        self._max_instance_number = max_instance_number

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this ScalingGroups.

        冷却时间，单位是秒。

        :return: The cool_down_time of this ScalingGroups.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this ScalingGroups.

        冷却时间，单位是秒。

        :param cool_down_time: The cool_down_time of this ScalingGroups.
        :type: int
        """
        self._cool_down_time = cool_down_time

    @property
    def lb_listener_id(self):
        """Gets the lb_listener_id of this ScalingGroups.

        经典型负载均衡监听器ID，多个负载均衡监听器ID以逗号分隔。

        :return: The lb_listener_id of this ScalingGroups.
        :rtype: str
        """
        return self._lb_listener_id

    @lb_listener_id.setter
    def lb_listener_id(self, lb_listener_id):
        """Sets the lb_listener_id of this ScalingGroups.

        经典型负载均衡监听器ID，多个负载均衡监听器ID以逗号分隔。

        :param lb_listener_id: The lb_listener_id of this ScalingGroups.
        :type: str
        """
        self._lb_listener_id = lb_listener_id

    @property
    def lbaas_listeners(self):
        """Gets the lbaas_listeners of this ScalingGroups.

        增强型负载均衡器信息，该参数为预留字段。

        :return: The lbaas_listeners of this ScalingGroups.
        :rtype: list[LbaasListenersResult]
        """
        return self._lbaas_listeners

    @lbaas_listeners.setter
    def lbaas_listeners(self, lbaas_listeners):
        """Sets the lbaas_listeners of this ScalingGroups.

        增强型负载均衡器信息，该参数为预留字段。

        :param lbaas_listeners: The lbaas_listeners of this ScalingGroups.
        :type: list[LbaasListenersResult]
        """
        self._lbaas_listeners = lbaas_listeners

    @property
    def available_zones(self):
        """Gets the available_zones of this ScalingGroups.

        可用分区信息

        :return: The available_zones of this ScalingGroups.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ScalingGroups.

        可用分区信息

        :param available_zones: The available_zones of this ScalingGroups.
        :type: list[str]
        """
        self._available_zones = available_zones

    @property
    def networks(self):
        """Gets the networks of this ScalingGroups.

        网络信息

        :return: The networks of this ScalingGroups.
        :rtype: list[Networks]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this ScalingGroups.

        网络信息

        :param networks: The networks of this ScalingGroups.
        :type: list[Networks]
        """
        self._networks = networks

    @property
    def security_groups(self):
        """Gets the security_groups of this ScalingGroups.

        安全组信息

        :return: The security_groups of this ScalingGroups.
        :rtype: list[SecurityGroupsResult]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ScalingGroups.

        安全组信息

        :param security_groups: The security_groups of this ScalingGroups.
        :type: list[SecurityGroupsResult]
        """
        self._security_groups = security_groups

    @property
    def create_time(self):
        """Gets the create_time of this ScalingGroups.

        创建伸缩组时间，遵循UTC时间。

        :return: The create_time of this ScalingGroups.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingGroups.

        创建伸缩组时间，遵循UTC时间。

        :param create_time: The create_time of this ScalingGroups.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ScalingGroups.

        伸缩组所在的VPC ID。

        :return: The vpc_id of this ScalingGroups.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ScalingGroups.

        伸缩组所在的VPC ID。

        :param vpc_id: The vpc_id of this ScalingGroups.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def detail(self):
        """Gets the detail of this ScalingGroups.

        伸缩组详情。

        :return: The detail of this ScalingGroups.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ScalingGroups.

        伸缩组详情。

        :param detail: The detail of this ScalingGroups.
        :type: str
        """
        self._detail = detail

    @property
    def is_scaling(self):
        """Gets the is_scaling of this ScalingGroups.

        伸缩组伸缩标志。

        :return: The is_scaling of this ScalingGroups.
        :rtype: bool
        """
        return self._is_scaling

    @is_scaling.setter
    def is_scaling(self, is_scaling):
        """Sets the is_scaling of this ScalingGroups.

        伸缩组伸缩标志。

        :param is_scaling: The is_scaling of this ScalingGroups.
        :type: bool
        """
        self._is_scaling = is_scaling

    @property
    def health_periodic_audit_method(self):
        """Gets the health_periodic_audit_method of this ScalingGroups.

        健康检查方式。

        :return: The health_periodic_audit_method of this ScalingGroups.
        :rtype: str
        """
        return self._health_periodic_audit_method

    @health_periodic_audit_method.setter
    def health_periodic_audit_method(self, health_periodic_audit_method):
        """Sets the health_periodic_audit_method of this ScalingGroups.

        健康检查方式。

        :param health_periodic_audit_method: The health_periodic_audit_method of this ScalingGroups.
        :type: str
        """
        self._health_periodic_audit_method = health_periodic_audit_method

    @property
    def health_periodic_audit_time(self):
        """Gets the health_periodic_audit_time of this ScalingGroups.

        健康检查的间隔时间。

        :return: The health_periodic_audit_time of this ScalingGroups.
        :rtype: int
        """
        return self._health_periodic_audit_time

    @health_periodic_audit_time.setter
    def health_periodic_audit_time(self, health_periodic_audit_time):
        """Sets the health_periodic_audit_time of this ScalingGroups.

        健康检查的间隔时间。

        :param health_periodic_audit_time: The health_periodic_audit_time of this ScalingGroups.
        :type: int
        """
        self._health_periodic_audit_time = health_periodic_audit_time

    @property
    def health_periodic_audit_grace_period(self):
        """Gets the health_periodic_audit_grace_period of this ScalingGroups.

        健康状况检查宽限期。

        :return: The health_periodic_audit_grace_period of this ScalingGroups.
        :rtype: int
        """
        return self._health_periodic_audit_grace_period

    @health_periodic_audit_grace_period.setter
    def health_periodic_audit_grace_period(self, health_periodic_audit_grace_period):
        """Sets the health_periodic_audit_grace_period of this ScalingGroups.

        健康状况检查宽限期。

        :param health_periodic_audit_grace_period: The health_periodic_audit_grace_period of this ScalingGroups.
        :type: int
        """
        self._health_periodic_audit_grace_period = health_periodic_audit_grace_period

    @property
    def instance_terminate_policy(self):
        """Gets the instance_terminate_policy of this ScalingGroups.

        移除策略。

        :return: The instance_terminate_policy of this ScalingGroups.
        :rtype: str
        """
        return self._instance_terminate_policy

    @instance_terminate_policy.setter
    def instance_terminate_policy(self, instance_terminate_policy):
        """Sets the instance_terminate_policy of this ScalingGroups.

        移除策略。

        :param instance_terminate_policy: The instance_terminate_policy of this ScalingGroups.
        :type: str
        """
        self._instance_terminate_policy = instance_terminate_policy

    @property
    def notifications(self):
        """Gets the notifications of this ScalingGroups.

        通知方式：EMAIL为发送邮件通知。

        :return: The notifications of this ScalingGroups.
        :rtype: list[str]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ScalingGroups.

        通知方式：EMAIL为发送邮件通知。

        :param notifications: The notifications of this ScalingGroups.
        :type: list[str]
        """
        self._notifications = notifications

    @property
    def delete_publicip(self):
        """Gets the delete_publicip of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的弹性IP。

        :return: The delete_publicip of this ScalingGroups.
        :rtype: bool
        """
        return self._delete_publicip

    @delete_publicip.setter
    def delete_publicip(self, delete_publicip):
        """Sets the delete_publicip of this ScalingGroups.

        删除云服务器是否删除云服务器绑定的弹性IP。

        :param delete_publicip: The delete_publicip of this ScalingGroups.
        :type: bool
        """
        self._delete_publicip = delete_publicip

    @property
    def cloud_location_id(self):
        """Gets the cloud_location_id of this ScalingGroups.

        该参数为预留字段

        :return: The cloud_location_id of this ScalingGroups.
        :rtype: str
        """
        return self._cloud_location_id

    @cloud_location_id.setter
    def cloud_location_id(self, cloud_location_id):
        """Sets the cloud_location_id of this ScalingGroups.

        该参数为预留字段

        :param cloud_location_id: The cloud_location_id of this ScalingGroups.
        :type: str
        """
        self._cloud_location_id = cloud_location_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ScalingGroups.

        企业项目ID

        :return: The enterprise_project_id of this ScalingGroups.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ScalingGroups.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ScalingGroups.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ScalingGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other