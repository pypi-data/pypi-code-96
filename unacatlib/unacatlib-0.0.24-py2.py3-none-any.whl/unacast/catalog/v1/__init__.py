# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/catalog/v1/query_service.proto, unacast/catalog/v1/catalog.proto, unacast/catalog/v1/catalog_service.proto, unacast/catalog/v1/export_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List, Optional

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class SearchMetricValuesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(3)
    track_total_hits_boolean: bool = betterproto.bool_field(4, group="track_total_hits")
    track_total_hits_integer: int = betterproto.int64_field(
        12, group="track_total_hits"
    )
    best_effort_query_when_not_allowed: bool = betterproto.bool_field(11)
    # Temporary fix to get random feature IDs, if this view sticks this should be
    # extracted into a separate API
    invert_sort_order: bool = betterproto.bool_field(9)
    # List of features by ID to limit the search to
    feature_filter: List[str] = betterproto.string_field(5)
    # Filter clause to limit the time period of the search
    observation_period_filter: "__metric_v1__.Period" = betterproto.message_field(6)
    # Filter clause to limit the search to certain Address Component Values.
    address_component_filter: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(7)
    # Filter clause to limit the search to certain Dimension Values.
    dimension_filter: List["__metric_v1__.DimensionFilter"] = betterproto.message_field(
        8
    )
    request_tags: Dict[str, str] = betterproto.map_field(
        13, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchMetricValuesResponse(betterproto.Message):
    values: List["__metric_v1__.MetricValue"] = betterproto.message_field(1)
    # All the filters applied to the request
    applied_filters: "QueryMetricFilters" = betterproto.message_field(2)
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchLayerFeaturesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)
    # List of features by ID to limit the search to
    feature_filter: List[str] = betterproto.string_field(5)
    # Filter clause to limit the search to certain Address Component Values.
    address_component_filter: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(7)
    track_total_hits: bool = betterproto.bool_field(10)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchLayerFeaturesResponse(betterproto.Message):
    features: List["__maps_v1__.Feature"] = betterproto.message_field(1)
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchAddressComponentValuesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    component: str = betterproto.string_field(3)
    query: str = betterproto.string_field(5)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchAddressComponentValuesResponse(betterproto.Message):
    address_component_values: List[
        "__maps_v1__.AddressComponentValue"
    ] = betterproto.message_field(1)
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchMetricReportRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(3)
    track_total_hits: bool = betterproto.bool_field(4)
    best_effort_query_when_not_allowed: bool = betterproto.bool_field(11)
    # List of features by ID to limit the search to
    feature_filter: List[str] = betterproto.string_field(5)
    # Filter clause to limit the time period of the search
    observation_period_filter: "__metric_v1__.Period" = betterproto.message_field(6)
    # Disable on demand costly aggregations
    disable_percentiles: bool = betterproto.bool_field(9)
    disable_cardinalities: bool = betterproto.bool_field(10)
    # Filter clause to limit the search to certain Address Component Values.
    address_component_filter: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(7)
    dimension_filter: List["__metric_v1__.DimensionFilter"] = betterproto.message_field(
        8
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryMetricFilters(betterproto.Message):
    period_filters: List["__metric_v1__.Period"] = betterproto.message_field(1)
    dimension_filters: List[
        "__metric_v1__.DimensionFilter"
    ] = betterproto.message_field(2)
    address_component_filters: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(3)
    feature_filters: List[str] = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchMetricReportResponse(betterproto.Message):
    report: "__metric_v1__.MetricReport" = betterproto.message_field(1)
    # All the filters applied to the request
    applied_filters: "QueryMetricFilters" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchDimensionValuesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    dimension_id: str = betterproto.string_field(2)
    query: str = betterproto.string_field(5)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SearchDimensionValuesResponse(betterproto.Message):
    dimension_values: List["__metric_v1__.DimensionValue"] = betterproto.message_field(
        1
    )
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Catalog(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetCatalogRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListCatalogsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListCatalogsResponse(betterproto.Message):
    catalogs: List["Catalog"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricResponse(betterproto.Message):
    metric: "__metric_v1__.Metric" = betterproto.message_field(1)
    complete_observation_period: "__metric_v1__.Period" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListMetricsRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)
    layer_filter: List[str] = betterproto.string_field(5)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListMetricsResponse(betterproto.Message):
    metrics: List["__metric_v1__.Metric"] = betterproto.message_field(1)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLayerRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLayerResponse(betterproto.Message):
    layer: "__maps_v1__.Layer" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryLayerRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)
    address_component_filter: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(5)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryLayerResponse(betterproto.Message):
    features: List["__maps_v1__.Feature"] = betterproto.message_field(4)
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateBigQueryExportRequest(betterproto.Message):
    metric_id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(3)
    filter: "QueryMetricFilters" = betterproto.message_field(5)
    big_query_config: "BigQueryConfig" = betterproto.message_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateBigQueryExportResponse(betterproto.Message):
    job_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BigQueryConfig(betterproto.Message):
    project_id: str = betterproto.string_field(1)
    dataset_id: str = betterproto.string_field(2)
    # List of features by ID to limit the search to
    table_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


class QueryServiceStub(betterproto.ServiceStub):
    """* This is the service used to query the Unacat"""

    async def search_metric_values(
        self,
        *,
        catalog_id: str = "",
        metric_id: str = "",
        billing_context: str = "",
        track_total_hits_boolean: bool = False,
        track_total_hits_integer: int = 0,
        best_effort_query_when_not_allowed: bool = False,
        invert_sort_order: bool = False,
        feature_filter: Optional[List[str]] = None,
        observation_period_filter: "__metric_v1__.Period" = None,
        address_component_filter: Optional[
            List["__maps_v1__.AddressComponentFilter"]
        ] = None,
        dimension_filter: Optional[List["__metric_v1__.DimensionFilter"]] = None,
        request_tags: Dict[str, str] = None,
        page_size: int = 0,
        page_token: str = "",
    ) -> "SearchMetricValuesResponse":
        feature_filter = feature_filter or []
        address_component_filter = address_component_filter or []
        dimension_filter = dimension_filter or []

        request = SearchMetricValuesRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_context = billing_context
        request.track_total_hits_boolean = track_total_hits_boolean
        request.track_total_hits_integer = track_total_hits_integer
        request.best_effort_query_when_not_allowed = best_effort_query_when_not_allowed
        request.invert_sort_order = invert_sort_order
        request.feature_filter = feature_filter
        if observation_period_filter is not None:
            request.observation_period_filter = observation_period_filter
        if address_component_filter is not None:
            request.address_component_filter = address_component_filter
        if dimension_filter is not None:
            request.dimension_filter = dimension_filter
        request.request_tags = request_tags
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.QueryService/SearchMetricValues",
            request,
            SearchMetricValuesResponse,
        )

    async def search_layer_features(
        self,
        *,
        catalog_id: str = "",
        layer_id: str = "",
        feature_filter: Optional[List[str]] = None,
        address_component_filter: Optional[
            List["__maps_v1__.AddressComponentFilter"]
        ] = None,
        track_total_hits: bool = False,
        page_size: int = 0,
        page_token: str = "",
    ) -> "SearchLayerFeaturesResponse":
        feature_filter = feature_filter or []
        address_component_filter = address_component_filter or []

        request = SearchLayerFeaturesRequest()
        request.catalog_id = catalog_id
        request.layer_id = layer_id
        request.feature_filter = feature_filter
        if address_component_filter is not None:
            request.address_component_filter = address_component_filter
        request.track_total_hits = track_total_hits
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.QueryService/SearchLayerFeatures",
            request,
            SearchLayerFeaturesResponse,
        )

    async def search_address_component_values(
        self,
        *,
        catalog_id: str = "",
        component: str = "",
        query: str = "",
        page_size: int = 0,
        page_token: str = "",
    ) -> "SearchAddressComponentValuesResponse":

        request = SearchAddressComponentValuesRequest()
        request.catalog_id = catalog_id
        request.component = component
        request.query = query
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.QueryService/SearchAddressComponentValues",
            request,
            SearchAddressComponentValuesResponse,
        )

    async def search_dimension_values(
        self,
        *,
        catalog_id: str = "",
        dimension_id: str = "",
        query: str = "",
        page_size: int = 0,
        page_token: str = "",
    ) -> "SearchDimensionValuesResponse":

        request = SearchDimensionValuesRequest()
        request.catalog_id = catalog_id
        request.dimension_id = dimension_id
        request.query = query
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.QueryService/SearchDimensionValues",
            request,
            SearchDimensionValuesResponse,
        )

    async def search_metric_report(
        self,
        *,
        catalog_id: str = "",
        metric_id: str = "",
        billing_context: str = "",
        track_total_hits: bool = False,
        best_effort_query_when_not_allowed: bool = False,
        feature_filter: Optional[List[str]] = None,
        observation_period_filter: "__metric_v1__.Period" = None,
        disable_percentiles: bool = False,
        disable_cardinalities: bool = False,
        address_component_filter: Optional[
            List["__maps_v1__.AddressComponentFilter"]
        ] = None,
        dimension_filter: Optional[List["__metric_v1__.DimensionFilter"]] = None,
    ) -> "SearchMetricReportResponse":
        feature_filter = feature_filter or []
        address_component_filter = address_component_filter or []
        dimension_filter = dimension_filter or []

        request = SearchMetricReportRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_context = billing_context
        request.track_total_hits = track_total_hits
        request.best_effort_query_when_not_allowed = best_effort_query_when_not_allowed
        request.feature_filter = feature_filter
        if observation_period_filter is not None:
            request.observation_period_filter = observation_period_filter
        request.disable_percentiles = disable_percentiles
        request.disable_cardinalities = disable_cardinalities
        if address_component_filter is not None:
            request.address_component_filter = address_component_filter
        if dimension_filter is not None:
            request.dimension_filter = dimension_filter

        return await self._unary_unary(
            "/unacast.catalog.v1.QueryService/SearchMetricReport",
            request,
            SearchMetricReportResponse,
        )


class CatalogServiceStub(betterproto.ServiceStub):
    """* This is the service used to query the Unacat"""

    async def list_catalogs(self) -> "ListCatalogsResponse":

        request = ListCatalogsRequest()

        return await self._unary_unary(
            "/unacast.catalog.v1.CatalogService/ListCatalogs",
            request,
            ListCatalogsResponse,
        )

    async def get_metric(
        self, *, catalog_id: str = "", metric_id: str = "", billing_context: str = ""
    ) -> "GetMetricResponse":

        request = GetMetricRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_context = billing_context

        return await self._unary_unary(
            "/unacast.catalog.v1.CatalogService/GetMetric", request, GetMetricResponse
        )

    async def list_metrics(
        self,
        *,
        catalog_id: str = "",
        billing_context: str = "",
        layer_filter: Optional[List[str]] = None,
        page_size: int = 0,
        page_token: str = "",
    ) -> "ListMetricsResponse":
        layer_filter = layer_filter or []

        request = ListMetricsRequest()
        request.catalog_id = catalog_id
        request.billing_context = billing_context
        request.layer_filter = layer_filter
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.CatalogService/ListMetrics",
            request,
            ListMetricsResponse,
        )

    async def get_layer(
        self, *, catalog_id: str = "", layer_id: str = ""
    ) -> "GetLayerResponse":

        request = GetLayerRequest()
        request.catalog_id = catalog_id
        request.layer_id = layer_id

        return await self._unary_unary(
            "/unacast.catalog.v1.CatalogService/GetLayer", request, GetLayerResponse
        )

    async def query_layer(
        self,
        *,
        catalog_id: str = "",
        layer_id: str = "",
        address_component_filter: Optional[
            List["__maps_v1__.AddressComponentFilter"]
        ] = None,
        page_size: int = 0,
        page_token: str = "",
    ) -> "QueryLayerResponse":
        address_component_filter = address_component_filter or []

        request = QueryLayerRequest()
        request.catalog_id = catalog_id
        request.layer_id = layer_id
        if address_component_filter is not None:
            request.address_component_filter = address_component_filter
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.catalog.v1.CatalogService/QueryLayer", request, QueryLayerResponse
        )


class ExportServiceStub(betterproto.ServiceStub):
    """* This is the service used to query the Unacat"""

    async def create_big_query_export(
        self,
        *,
        metric_id: str = "",
        catalog_id: str = "",
        billing_context: str = "",
        filter: "QueryMetricFilters" = None,
        big_query_config: "BigQueryConfig" = None,
    ) -> "CreateBigQueryExportResponse":

        request = CreateBigQueryExportRequest()
        request.metric_id = metric_id
        request.catalog_id = catalog_id
        request.billing_context = billing_context
        if filter is not None:
            request.filter = filter
        if big_query_config is not None:
            request.big_query_config = big_query_config

        return await self._unary_unary(
            "/unacast.catalog.v1.ExportService/CreateBigQueryExport",
            request,
            CreateBigQueryExportResponse,
        )


from ...maps import v1 as __maps_v1__
from ...metric import v1 as __metric_v1__
