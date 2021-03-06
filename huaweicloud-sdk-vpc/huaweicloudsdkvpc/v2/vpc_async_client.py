# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class VpcAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(VpcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def accept_vpc_peering_async(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。

        :param AcceptVpcPeeringRequest request
        :return: AcceptVpcPeeringResponse
        """
        return self.accept_vpc_peering_with_http_info(request)

    def accept_vpc_peering_with_http_info(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。

        :param AcceptVpcPeeringRequest request
        :return: AcceptVpcPeeringResponse
        """

        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}/accept',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AcceptVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_port_async(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: CreatePortResponse
        """
        return self.create_port_with_http_info(request)

    def create_port_with_http_info(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: CreatePortResponse
        """

        all_params = ['port']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_security_group_async(self, request):
        """创建安全组

        创建安全组。

        :param CreateSecurityGroupRequest request
        :return: CreateSecurityGroupResponse
        """
        return self.create_security_group_with_http_info(request)

    def create_security_group_with_http_info(self, request):
        """创建安全组

        创建安全组。

        :param CreateSecurityGroupRequest request
        :return: CreateSecurityGroupResponse
        """

        all_params = ['security_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_security_group_rule_async(self, request):
        """创建安全组规则

        创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: CreateSecurityGroupRuleResponse
        """
        return self.create_security_group_rule_with_http_info(request)

    def create_security_group_rule_with_http_info(self, request):
        """创建安全组规则

        创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: CreateSecurityGroupRuleResponse
        """

        all_params = ['security_group_rule']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_subnet_async(self, request):
        """创建子网

        创建子网。

        :param CreateSubnetRequest request
        :return: CreateSubnetResponse
        """
        return self.create_subnet_with_http_info(request)

    def create_subnet_with_http_info(self, request):
        """创建子网

        创建子网。

        :param CreateSubnetRequest request
        :return: CreateSubnetResponse
        """

        all_params = ['subnet']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vpc_peering_async(self, request):
        """创建对等连接

        创建对等连接。

        :param CreateVpcPeeringRequest request
        :return: CreateVpcPeeringResponse
        """
        return self.create_vpc_peering_with_http_info(request)

    def create_vpc_peering_with_http_info(self, request):
        """创建对等连接

        创建对等连接。

        :param CreateVpcPeeringRequest request
        :return: CreateVpcPeeringResponse
        """

        all_params = ['peering']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_port_async(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: DeletePortResponse
        """
        return self.delete_port_with_http_info(request)

    def delete_port_with_http_info(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: DeletePortResponse
        """

        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_security_group_async(self, request):
        """删除安全组

        删除安全组。

        :param DeleteSecurityGroupRequest request
        :return: DeleteSecurityGroupResponse
        """
        return self.delete_security_group_with_http_info(request)

    def delete_security_group_with_http_info(self, request):
        """删除安全组

        删除安全组。

        :param DeleteSecurityGroupRequest request
        :return: DeleteSecurityGroupResponse
        """

        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-groups/{security_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_security_group_rule_async(self, request):
        """删除安全组规则

        删除安全组规则。

        :param DeleteSecurityGroupRuleRequest request
        :return: DeleteSecurityGroupRuleResponse
        """
        return self.delete_security_group_rule_with_http_info(request)

    def delete_security_group_rule_with_http_info(self, request):
        """删除安全组规则

        删除安全组规则。

        :param DeleteSecurityGroupRuleRequest request
        :return: DeleteSecurityGroupRuleResponse
        """

        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules/{security_group_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_subnet_async(self, request):
        """删除子网

        删除子网

        :param DeleteSubnetRequest request
        :return: DeleteSubnetResponse
        """
        return self.delete_subnet_with_http_info(request)

    def delete_subnet_with_http_info(self, request):
        """删除子网

        删除子网

        :param DeleteSubnetRequest request
        :return: DeleteSubnetResponse
        """

        all_params = ['vpc_id', 'subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vpc_peering_async(self, request):
        """删除对等连接

        删除对等连接。 可以在在本端或对端任何一端删除对等连接。

        :param DeleteVpcPeeringRequest request
        :return: DeleteVpcPeeringResponse
        """
        return self.delete_vpc_peering_with_http_info(request)

    def delete_vpc_peering_with_http_info(self, request):
        """删除对等连接

        删除对等连接。 可以在在本端或对端任何一端删除对等连接。

        :param DeleteVpcPeeringRequest request
        :return: DeleteVpcPeeringResponse
        """

        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ports_async(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。

        :param ListPortsRequest request
        :return: ListPortsResponse
        """
        return self.list_ports_with_http_info(request)

    def list_ports_with_http_info(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。

        :param ListPortsRequest request
        :return: ListPortsResponse
        """

        all_params = ['name', 'id', 'limit', 'admin_state_up', 'network_id', 'mac_address', 'device_id', 'device_owner', 'status', 'marker', 'fixed_ips', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPortsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_security_group_rules_async(self, request):
        """查询安全组规则列表

        查询安全组规则列表。

        :param ListSecurityGroupRulesRequest request
        :return: ListSecurityGroupRulesResponse
        """
        return self.list_security_group_rules_with_http_info(request)

    def list_security_group_rules_with_http_info(self, request):
        """查询安全组规则列表

        查询安全组规则列表。

        :param ListSecurityGroupRulesRequest request
        :return: ListSecurityGroupRulesResponse
        """

        all_params = ['marker', 'limit', 'security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupRulesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_security_groups_async(self, request):
        """查询安全组列表

        查询安全组列表

        :param ListSecurityGroupsRequest request
        :return: ListSecurityGroupsResponse
        """
        return self.list_security_groups_with_http_info(request)

    def list_security_groups_with_http_info(self, request):
        """查询安全组列表

        查询安全组列表

        :param ListSecurityGroupsRequest request
        :return: ListSecurityGroupsResponse
        """

        all_params = ['limit', 'marker', 'vpc_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_subnets_async(self, request):
        """查询子网列表

        查询子网列表

        :param ListSubnetsRequest request
        :return: ListSubnetsResponse
        """
        return self.list_subnets_with_http_info(request)

    def list_subnets_with_http_info(self, request):
        """查询子网列表

        查询子网列表

        :param ListSubnetsRequest request
        :return: ListSubnetsResponse
        """

        all_params = ['limit', 'marker', 'vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubnetsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_vpc_peerings_async(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。

        :param ListVpcPeeringsRequest request
        :return: ListVpcPeeringsResponse
        """
        return self.list_vpc_peerings_with_http_info(request)

    def list_vpc_peerings_with_http_info(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。

        :param ListVpcPeeringsRequest request
        :return: ListVpcPeeringsResponse
        """

        all_params = ['limit', 'marker', 'id', 'name', 'status', 'tenant_id', 'vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcPeeringsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reject_vpc_peering_async(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。

        :param RejectVpcPeeringRequest request
        :return: RejectVpcPeeringResponse
        """
        return self.reject_vpc_peering_with_http_info(request)

    def reject_vpc_peering_with_http_info(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。

        :param RejectVpcPeeringRequest request
        :return: RejectVpcPeeringResponse
        """

        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}/reject',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RejectVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_port_async(self, request):
        """查询端口

        查询单个端口详情。

        :param ShowPortRequest request
        :return: ShowPortResponse
        """
        return self.show_port_with_http_info(request)

    def show_port_with_http_info(self, request):
        """查询端口

        查询单个端口详情。

        :param ShowPortRequest request
        :return: ShowPortResponse
        """

        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quota_async(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """

        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_security_group_async(self, request):
        """查询安全组

        查询单个安全组详情。

        :param ShowSecurityGroupRequest request
        :return: ShowSecurityGroupResponse
        """
        return self.show_security_group_with_http_info(request)

    def show_security_group_with_http_info(self, request):
        """查询安全组

        查询单个安全组详情。

        :param ShowSecurityGroupRequest request
        :return: ShowSecurityGroupResponse
        """

        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-groups/{security_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_security_group_rule_async(self, request):
        """查询安全组规则

        查询单个安全组规则详情

        :param ShowSecurityGroupRuleRequest request
        :return: ShowSecurityGroupRuleResponse
        """
        return self.show_security_group_rule_with_http_info(request)

    def show_security_group_rule_with_http_info(self, request):
        """查询安全组规则

        查询单个安全组规则详情

        :param ShowSecurityGroupRuleRequest request
        :return: ShowSecurityGroupRuleResponse
        """

        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules/{security_group_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_subnet_async(self, request):
        """查询子网

        查询子网详情。

        :param ShowSubnetRequest request
        :return: ShowSubnetResponse
        """
        return self.show_subnet_with_http_info(request)

    def show_subnet_with_http_info(self, request):
        """查询子网

        查询子网详情。

        :param ShowSubnetRequest request
        :return: ShowSubnetResponse
        """

        all_params = ['subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets/{subnet_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vpc_peering_async(self, request):
        """查询对等连接

        查询对等连接详情。

        :param ShowVpcPeeringRequest request
        :return: ShowVpcPeeringResponse
        """
        return self.show_vpc_peering_with_http_info(request)

    def show_vpc_peering_with_http_info(self, request):
        """查询对等连接

        查询对等连接详情。

        :param ShowVpcPeeringRequest request
        :return: ShowVpcPeeringResponse
        """

        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_port_async(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: UpdatePortResponse
        """
        return self.update_port_with_http_info(request)

    def update_port_with_http_info(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: UpdatePortResponse
        """

        all_params = ['port_id', 'port']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_subnet_async(self, request):
        """更新子网

        更新子网。

        :param UpdateSubnetRequest request
        :return: UpdateSubnetResponse
        """
        return self.update_subnet_with_http_info(request)

    def update_subnet_with_http_info(self, request):
        """更新子网

        更新子网。

        :param UpdateSubnetRequest request
        :return: UpdateSubnetResponse
        """

        all_params = ['vpc_id', 'subnet_id', 'subnet']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vpc_peering_async(self, request):
        """更新对等连接

        更新对等连接。

        :param UpdateVpcPeeringRequest request
        :return: UpdateVpcPeeringResponse
        """
        return self.update_vpc_peering_with_http_info(request)

    def update_vpc_peering_with_http_info(self, request):
        """更新对等连接

        更新对等连接。

        :param UpdateVpcPeeringRequest request
        :return: UpdateVpcPeeringResponse
        """

        all_params = ['peering_id', 'peering']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_privateip_async(self, request):
        """申请私有IP

        申请私有IP。

        :param CreatePrivateipRequest request
        :return: CreatePrivateipResponse
        """
        return self.create_privateip_with_http_info(request)

    def create_privateip_with_http_info(self, request):
        """申请私有IP

        申请私有IP。

        :param CreatePrivateipRequest request
        :return: CreatePrivateipResponse
        """

        all_params = ['privateips']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/privateips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrivateipResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_privateip_async(self, request):
        """删除私有IP

        删除私有IP。

        :param DeletePrivateipRequest request
        :return: DeletePrivateipResponse
        """
        return self.delete_privateip_with_http_info(request)

    def delete_privateip_with_http_info(self, request):
        """删除私有IP

        删除私有IP。

        :param DeletePrivateipRequest request
        :return: DeletePrivateipResponse
        """

        all_params = ['privateip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/privateips/{privateip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePrivateipResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_privateips_async(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。

        :param ListPrivateipsRequest request
        :return: ListPrivateipsResponse
        """
        return self.list_privateips_with_http_info(request)

    def list_privateips_with_http_info(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。

        :param ListPrivateipsRequest request
        :return: ListPrivateipsResponse
        """

        all_params = ['subnet_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets/{subnet_id}/privateips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPrivateipsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_network_ip_availabilities_async(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IPv4地址使用情况。 包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。  > 须知  - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。 - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。 - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。

        :param ShowNetworkIpAvailabilitiesRequest request
        :return: ShowNetworkIpAvailabilitiesResponse
        """
        return self.show_network_ip_availabilities_with_http_info(request)

    def show_network_ip_availabilities_with_http_info(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IPv4地址使用情况。 包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。  > 须知  - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。 - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。 - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。

        :param ShowNetworkIpAvailabilitiesRequest request
        :return: ShowNetworkIpAvailabilitiesResponse
        """

        all_params = ['network_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/network-ip-availabilities/{network_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNetworkIpAvailabilitiesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_privateip_async(self, request):
        """查询私有IP

        指定ID查询私有IP。

        :param ShowPrivateipRequest request
        :return: ShowPrivateipResponse
        """
        return self.show_privateip_with_http_info(request)

    def show_privateip_with_http_info(self, request):
        """查询私有IP

        指定ID查询私有IP。

        :param ShowPrivateipRequest request
        :return: ShowPrivateipResponse
        """

        all_params = ['privateip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/privateips/{privateip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPrivateipResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vpc_async(self, request):
        """创建VPC

        创建虚拟私有云。

        :param CreateVpcRequest request
        :return: CreateVpcResponse
        """
        return self.create_vpc_with_http_info(request)

    def create_vpc_with_http_info(self, request):
        """创建VPC

        创建虚拟私有云。

        :param CreateVpcRequest request
        :return: CreateVpcResponse
        """

        all_params = ['vpc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vpc_route_async(self, request):
        """创建VPC路由

        创建路由

        :param CreateVpcRouteRequest request
        :return: CreateVpcRouteResponse
        """
        return self.create_vpc_route_with_http_info(request)

    def create_vpc_route_with_http_info(self, request):
        """创建VPC路由

        创建路由

        :param CreateVpcRouteRequest request
        :return: CreateVpcRouteResponse
        """

        all_params = ['route']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcRouteResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vpc_async(self, request):
        """删除VPC

        删除虚拟私有云。

        :param DeleteVpcRequest request
        :return: DeleteVpcResponse
        """
        return self.delete_vpc_with_http_info(request)

    def delete_vpc_with_http_info(self, request):
        """删除VPC

        删除虚拟私有云。

        :param DeleteVpcRequest request
        :return: DeleteVpcResponse
        """

        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vpc_route_async(self, request):
        """删除VPC路由

        删除路由

        :param DeleteVpcRouteRequest request
        :return: DeleteVpcRouteResponse
        """
        return self.delete_vpc_route_with_http_info(request)

    def delete_vpc_route_with_http_info(self, request):
        """删除VPC路由

        删除路由

        :param DeleteVpcRouteRequest request
        :return: DeleteVpcRouteResponse
        """

        all_params = ['route_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes/{route_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVpcRouteResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_vpc_routes_async(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。

        :param ListVpcRoutesRequest request
        :return: ListVpcRoutesResponse
        """
        return self.list_vpc_routes_with_http_info(request)

    def list_vpc_routes_with_http_info(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。

        :param ListVpcRoutesRequest request
        :return: ListVpcRoutesResponse
        """

        all_params = ['limit', 'marker', 'id', 'type', 'vpc_id', 'destination', 'tenant_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcRoutesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_vpcs_async(self, request):
        """查询VPC列表

        查询虚拟私有云列表。

        :param ListVpcsRequest request
        :return: ListVpcsResponse
        """
        return self.list_vpcs_with_http_info(request)

    def list_vpcs_with_http_info(self, request):
        """查询VPC列表

        查询虚拟私有云列表。

        :param ListVpcsRequest request
        :return: ListVpcsResponse
        """

        all_params = ['limit', 'marker', 'id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vpc_async(self, request):
        """查询VPC

        查询虚拟私有云。

        :param ShowVpcRequest request
        :return: ShowVpcResponse
        """
        return self.show_vpc_with_http_info(request)

    def show_vpc_with_http_info(self, request):
        """查询VPC

        查询虚拟私有云。

        :param ShowVpcRequest request
        :return: ShowVpcResponse
        """

        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vpc_route_async(self, request):
        """查询VPC路由

        查询路由详情

        :param ShowVpcRouteRequest request
        :return: ShowVpcRouteResponse
        """
        return self.show_vpc_route_with_http_info(request)

    def show_vpc_route_with_http_info(self, request):
        """查询VPC路由

        查询路由详情

        :param ShowVpcRouteRequest request
        :return: ShowVpcRouteResponse
        """

        all_params = ['route_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes/{route_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcRouteResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vpc_async(self, request):
        """更新VPC

        更新虚拟私有云。

        :param UpdateVpcRequest request
        :return: UpdateVpcResponse
        """
        return self.update_vpc_with_http_info(request)

    def update_vpc_with_http_info(self, request):
        """更新VPC

        更新虚拟私有云。

        :param UpdateVpcRequest request
        :return: UpdateVpcResponse
        """

        all_params = ['vpc_id', 'vpc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
