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


class SourcesService(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """SourcesService - a operation defined in OpenAPI."""
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_sources_id(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sources_id(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sources_id_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sources_id_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def delete_sources_id_with_http_info(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sources_id_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sources_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in local_var_params or
                local_var_params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `delete_sources_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['sourceID'] = local_var_params['source_id']  # noqa: E501

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
            '/api/v2/sources/{sourceID}', 'DELETE',
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

    def get_sources(self, **kwargs):  # noqa: E501,D401,D403
        """Get all sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization name.
        :return: Sources
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sources_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sources_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sources_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Get all sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization name.
        :return: Sources
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['zap_trace_span', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sources" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501

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
            '/api/v2/sources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sources',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def get_sources_id(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sources_id_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sources_id_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def get_sources_id_with_http_info(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sources_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in local_var_params or
                local_var_params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_sources_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['sourceID'] = local_var_params['source_id']  # noqa: E501

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
            '/api/v2/sources/{sourceID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Source',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def get_sources_id_buckets(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get buckets in a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_buckets(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization name.
        :return: Buckets
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sources_id_buckets_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sources_id_buckets_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def get_sources_id_buckets_with_http_info(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get buckets in a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_buckets_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization name.
        :return: Buckets
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source_id', 'zap_trace_span', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sources_id_buckets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in local_var_params or
                local_var_params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_sources_id_buckets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['sourceID'] = local_var_params['source_id']  # noqa: E501

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501

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
            '/api/v2/sources/{sourceID}/buckets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Buckets',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def get_sources_id_health(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get the health of a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_health(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sources_id_health_with_http_info(source_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sources_id_health_with_http_info(source_id, **kwargs)  # noqa: E501
            return data

    def get_sources_id_health_with_http_info(self, source_id, **kwargs):  # noqa: E501,D401,D403
        """Get the health of a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_health_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sources_id_health" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in local_var_params or
                local_var_params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_sources_id_health`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['sourceID'] = local_var_params['source_id']  # noqa: E501

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
            '/api/v2/sources/{sourceID}/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthCheck',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def patch_sources_id(self, source_id, source, **kwargs):  # noqa: E501,D401,D403
        """Update a Source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sources_id(source_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param Source source: Source update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_sources_id_with_http_info(source_id, source, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_sources_id_with_http_info(source_id, source, **kwargs)  # noqa: E501
            return data

    def patch_sources_id_with_http_info(self, source_id, source, **kwargs):  # noqa: E501,D401,D403
        """Update a Source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sources_id_with_http_info(source_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param Source source: Source update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source_id', 'source', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_sources_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in local_var_params or
                local_var_params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `patch_sources_id`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in local_var_params or
                local_var_params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `patch_sources_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['sourceID'] = local_var_params['source_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'source' in local_var_params:
            body_params = local_var_params['source']
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
            '/api/v2/sources/{sourceID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Source',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def post_sources(self, source, **kwargs):  # noqa: E501,D401,D403
        """Create a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sources(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Source source: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_sources_with_http_info(source, **kwargs)  # noqa: E501
        else:
            (data) = self.post_sources_with_http_info(source, **kwargs)  # noqa: E501
            return data

    def post_sources_with_http_info(self, source, **kwargs):  # noqa: E501,D401,D403
        """Create a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sources_with_http_info(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Source source: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['source', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_sources" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in local_var_params or
                local_var_params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `post_sources`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'source' in local_var_params:
            body_params = local_var_params['source']
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
            '/api/v2/sources', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Source',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)
