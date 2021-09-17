# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class SecretsService(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """SecretsService - a operation defined in OpenAPI."""
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_orgs_id_secrets(self, org_id, **kwargs):  # noqa: E501,D401,D403
        """List all secret keys for an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_orgs_id_secrets(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: SecretKeysResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_orgs_id_secrets_with_http_info(org_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_orgs_id_secrets_with_http_info(org_id, **kwargs)  # noqa: E501
            return data

    def get_orgs_id_secrets_with_http_info(self, org_id, **kwargs):  # noqa: E501,D401,D403
        """List all secret keys for an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_orgs_id_secrets_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: SecretKeysResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['org_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orgs_id_secrets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `get_orgs_id_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['orgID'] = local_var_params['org_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/orgs/{orgID}/secrets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SecretKeysResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def patch_orgs_id_secrets(self, org_id, request_body, **kwargs):  # noqa: E501,D401,D403
        """Update secrets in an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_orgs_id_secrets(org_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param dict(str, str) request_body: Secret key value pairs to update/add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_orgs_id_secrets_with_http_info(org_id, request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_orgs_id_secrets_with_http_info(org_id, request_body, **kwargs)  # noqa: E501
            return data

    def patch_orgs_id_secrets_with_http_info(self, org_id, request_body, **kwargs):  # noqa: E501,D401,D403
        """Update secrets in an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_orgs_id_secrets_with_http_info(org_id, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param dict(str, str) request_body: Secret key value pairs to update/add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['org_id', 'request_body', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_orgs_id_secrets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `patch_orgs_id_secrets`")  # noqa: E501
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `patch_orgs_id_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['orgID'] = local_var_params['org_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/orgs/{orgID}/secrets', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def post_orgs_id_secrets(self, org_id, secret_keys, **kwargs):  # noqa: E501,D401,D403
        """Delete secrets from an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_orgs_id_secrets(org_id, secret_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param SecretKeys secret_keys: Secret key to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_orgs_id_secrets_with_http_info(org_id, secret_keys, **kwargs)  # noqa: E501
        else:
            (data) = self.post_orgs_id_secrets_with_http_info(org_id, secret_keys, **kwargs)  # noqa: E501
            return data

    def post_orgs_id_secrets_with_http_info(self, org_id, secret_keys, **kwargs):  # noqa: E501,D401,D403
        """Delete secrets from an organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_orgs_id_secrets_with_http_info(org_id, secret_keys, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param SecretKeys secret_keys: Secret key to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['org_id', 'secret_keys', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_orgs_id_secrets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `post_orgs_id_secrets`")  # noqa: E501
        # verify the required parameter 'secret_keys' is set
        if ('secret_keys' not in local_var_params or
                local_var_params['secret_keys'] is None):
            raise ValueError("Missing the required parameter `secret_keys` when calling `post_orgs_id_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['orgID'] = local_var_params['org_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'secret_keys' in local_var_params:
            body_params = local_var_params['secret_keys']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/orgs/{orgID}/secrets/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)
