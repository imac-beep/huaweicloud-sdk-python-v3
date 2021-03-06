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


class LiveAPIAsyncClient(Client):
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
        super(LiveAPIAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_record_config_async(self, request):
        """创建录制配置

        创建录制配置接口

        :param CreateRecordConfigRequest request
        :return: CreateRecordConfigResponse
        """
        return self.create_record_config_with_http_info(request)

    def create_record_config_with_http_info(self, request):
        """创建录制配置

        创建录制配置接口

        :param CreateRecordConfigRequest request
        :return: CreateRecordConfigResponse
        """

        all_params = ['create_record_config_request_body']
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRecordConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_stream_forbidden_async(self, request):
        """禁止直播推流

        禁止直播推流

        :param CreateStreamForbiddenRequest request
        :return: CreateStreamForbiddenResponse
        """
        return self.create_stream_forbidden_with_http_info(request)

    def create_stream_forbidden_with_http_info(self, request):
        """禁止直播推流

        禁止直播推流

        :param CreateStreamForbiddenRequest request
        :return: CreateStreamForbiddenResponse
        """

        all_params = ['create_stream_forbidden_request_body', 'specify_project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'specify_project' in local_var_params:
            query_params.append(('specify_project', local_var_params['specify_project']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateStreamForbiddenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_transcodings_template_async(self, request):
        """创建直播转码模板

        创建直播转码模板

        :param CreateTranscodingsTemplateRequest request
        :return: CreateTranscodingsTemplateResponse
        """
        return self.create_transcodings_template_with_http_info(request)

    def create_transcodings_template_with_http_info(self, request):
        """创建直播转码模板

        创建直播转码模板

        :param CreateTranscodingsTemplateRequest request
        :return: CreateTranscodingsTemplateResponse
        """

        all_params = ['create_transcodings_template_request_body']
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTranscodingsTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_record_config_async(self, request):
        """删除录制配置

        删除录制配置接口

        :param DeleteRecordConfigRequest request
        :return: DeleteRecordConfigResponse
        """
        return self.delete_record_config_with_http_info(request)

    def delete_record_config_with_http_info(self, request):
        """删除录制配置

        删除录制配置接口

        :param DeleteRecordConfigRequest request
        :return: DeleteRecordConfigResponse
        """

        all_params = ['domain', 'app_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRecordConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_stream_forbidden_async(self, request):
        """禁推恢复

        恢复直播推流接口

        :param DeleteStreamForbiddenRequest request
        :return: DeleteStreamForbiddenResponse
        """
        return self.delete_stream_forbidden_with_http_info(request)

    def delete_stream_forbidden_with_http_info(self, request):
        """禁推恢复

        恢复直播推流接口

        :param DeleteStreamForbiddenRequest request
        :return: DeleteStreamForbiddenResponse
        """

        all_params = ['domain', 'app_name', 'stream_name', 'specify_project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'specify_project' in local_var_params:
            query_params.append(('specify_project', local_var_params['specify_project']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteStreamForbiddenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_transcodings_template_async(self, request):
        """删除直播转码模板

        删除直播转码模板

        :param DeleteTranscodingsTemplateRequest request
        :return: DeleteTranscodingsTemplateResponse
        """
        return self.delete_transcodings_template_with_http_info(request)

    def delete_transcodings_template_with_http_info(self, request):
        """删除直播转码模板

        删除直播转码模板

        :param DeleteTranscodingsTemplateRequest request
        :return: DeleteTranscodingsTemplateResponse
        """

        all_params = ['domain', 'app_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTranscodingsTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_record_configs_async(self, request):
        """查询录制配置

        查询录制配置接口

        :param ListRecordConfigsRequest request
        :return: ListRecordConfigsResponse
        """
        return self.list_record_configs_with_http_info(request)

    def list_record_configs_with_http_info(self, request):
        """查询录制配置

        查询录制配置接口

        :param ListRecordConfigsRequest request
        :return: ListRecordConfigsResponse
        """

        all_params = ['domain', 'app_name', 'stream_name', 'page', 'size', 'record_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'record_type' in local_var_params:
            query_params.append(('record_type', local_var_params['record_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecordConfigsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_stream_forbidden_async(self, request):
        """查询禁止直播推流列表

        查询禁播黑名单列表

        :param ListStreamForbiddenRequest request
        :return: ListStreamForbiddenResponse
        """
        return self.list_stream_forbidden_with_http_info(request)

    def list_stream_forbidden_with_http_info(self, request):
        """查询禁止直播推流列表

        查询禁播黑名单列表

        :param ListStreamForbiddenRequest request
        :return: ListStreamForbiddenResponse
        """

        all_params = ['domain', 'specify_project', 'app_name', 'stream_name', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'specify_project' in local_var_params:
            query_params.append(('specify_project', local_var_params['specify_project']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStreamForbiddenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_bandwidth_async(self, request):
        """查询直播加速的带宽数据

        查询直播加速的播流域名网络带宽监控数据

        :param ShowBandwidthRequest request
        :return: ShowBandwidthResponse
        """
        return self.show_bandwidth_with_http_info(request)

    def show_bandwidth_with_http_info(self, request):
        """查询直播加速的带宽数据

        查询直播加速的播流域名网络带宽监控数据

        :param ShowBandwidthRequest request
        :return: ShowBandwidthResponse
        """

        all_params = ['domain', 'start_time', 'end_time', 'step']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/bandwidth',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBandwidthResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_online_users_async(self, request):
        """查询直播播放在线人数

        查询加速的直播播放在线人数

        :param ShowOnlineUsersRequest request
        :return: ShowOnlineUsersResponse
        """
        return self.show_online_users_with_http_info(request)

    def show_online_users_with_http_info(self, request):
        """查询直播播放在线人数

        查询加速的直播播放在线人数

        :param ShowOnlineUsersRequest request
        :return: ShowOnlineUsersResponse
        """

        all_params = ['domain', 'app_name', 'stream_name', 'start_time', 'end_time', 'step']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOnlineUsersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_traffic_async(self, request):
        """查询直播加速的流量数据

        查询直播加速的播流域名网络流量监控数据

        :param ShowTrafficRequest request
        :return: ShowTrafficResponse
        """
        return self.show_traffic_with_http_info(request)

    def show_traffic_with_http_info(self, request):
        """查询直播加速的流量数据

        查询直播加速的播流域名网络流量监控数据

        :param ShowTrafficRequest request
        :return: ShowTrafficResponse
        """

        all_params = ['domain', 'start_time', 'end_time', 'step']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/traffic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTrafficResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_transcodings_template_async(self, request):
        """查询直播转码模板

        查询直播转码模板

        :param ShowTranscodingsTemplateRequest request
        :return: ShowTranscodingsTemplateResponse
        """
        return self.show_transcodings_template_with_http_info(request)

    def show_transcodings_template_with_http_info(self, request):
        """查询直播转码模板

        查询直播转码模板

        :param ShowTranscodingsTemplateRequest request
        :return: ShowTranscodingsTemplateResponse
        """

        all_params = ['domain', 'app_name', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTranscodingsTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_stream_forbidden_async(self, request):
        """修改禁推属性

        修改禁推属性

        :param UpdateStreamForbiddenRequest request
        :return: UpdateStreamForbiddenResponse
        """
        return self.update_stream_forbidden_with_http_info(request)

    def update_stream_forbidden_with_http_info(self, request):
        """修改禁推属性

        修改禁推属性

        :param UpdateStreamForbiddenRequest request
        :return: UpdateStreamForbiddenResponse
        """

        all_params = ['update_stream_forbidden_request_body', 'specify_project']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'specify_project' in local_var_params:
            query_params.append(('specify_project', local_var_params['specify_project']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateStreamForbiddenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_transcodings_template_async(self, request):
        """配置直播转码模板

        修改直播转码模板

        :param UpdateTranscodingsTemplateRequest request
        :return: UpdateTranscodingsTemplateResponse
        """
        return self.update_transcodings_template_with_http_info(request)

    def update_transcodings_template_with_http_info(self, request):
        """配置直播转码模板

        修改直播转码模板

        :param UpdateTranscodingsTemplateRequest request
        :return: UpdateTranscodingsTemplateResponse
        """

        all_params = ['update_transcodings_template_request_body']
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTranscodingsTemplateResponse',
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
