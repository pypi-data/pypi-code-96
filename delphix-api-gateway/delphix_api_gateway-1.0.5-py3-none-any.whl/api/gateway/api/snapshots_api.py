"""
    Delphix API Gateway

    Delphix API Gateway API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from delphix.api.gateway.api_client import ApiClient, Endpoint as _Endpoint
from delphix.api.gateway.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from delphix.api.gateway.model.list_snaphots_response import ListSnaphotsResponse
from delphix.api.gateway.model.snapshot import Snapshot


class SnapshotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_snapshot_by_id(
            self,
            snapshot_id,
            **kwargs
        ):
            """Get a Snapshot by ID.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_snapshot_by_id(snapshot_id, async_req=True)
            >>> result = thread.get()

            Args:
                snapshot_id (str): The ID of the snaphost.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Snapshot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['snapshot_id'] = \
                snapshot_id
            return self.call_with_http_info(**kwargs)

        self.get_snapshot_by_id = _Endpoint(
            settings={
                'response_type': (Snapshot,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/snapshots/{snapshotId}',
                'operation_id': 'get_snapshot_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'snapshot_id',
                ],
                'required': [
                    'snapshot_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'snapshot_id',
                ]
            },
            root_map={
                'validations': {
                    ('snapshot_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'snapshot_id':
                        (str,),
                },
                'attribute_map': {
                    'snapshot_id': 'snapshotId',
                },
                'location_map': {
                    'snapshot_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_snapshot_by_id
        )

        def __get_snapshots(
            self,
            **kwargs
        ):
            """List Snapshots for a dSource or VDB.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_snapshots(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                dataset_id (str): The ID of the dSource or VDB for which to fetch Snapshots.. [optional]
                limit (int): Maximum number of objects to return per query. The value must be between 1 and 1000. Default is 100.. [optional] if omitted the server will use the default value of 100
                cursor (str): Cursor to fetch the next or previous page of results.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListSnaphotsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_snapshots = _Endpoint(
            settings={
                'response_type': (ListSnaphotsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/snapshots',
                'operation_id': 'get_snapshots',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dataset_id',
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'dataset_id',
                    'limit',
                    'cursor',
                ]
            },
            root_map={
                'validations': {
                    ('dataset_id',): {

                        'min_length': 1,
                    },
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('cursor',): {
                        'max_length': 4096,
                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dataset_id':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'dataset_id': 'dataset_id',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'dataset_id': 'query',
                    'limit': 'query',
                    'cursor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_snapshots
        )
