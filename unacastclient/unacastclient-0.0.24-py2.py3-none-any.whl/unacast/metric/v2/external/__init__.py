# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/metric/v2/external/dimension.proto, unacast/metric/v2/external/metric_value.proto, unacast/metric/v2/external/metric_report.proto, unacast/metric/v2/external/lens.proto, unacast/metric/v2/external/metric.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class Cadence(betterproto.Enum):
    CADENCE_UNSPECIFIED = 0
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    QUARTERLY = 4
    YEARLY = 5


class ValueKind(betterproto.Enum):
    KIND_UNSPECIFIED = 0
    NUMBER = 1
    COUNT = 2
    CATEGORY = 3


class LifecycleStage(betterproto.Enum):
    UNSPECIFIED = 0
    PROTOTYPE = 3
    RELEASE_CANDIDATE = 6
    STABLE = 9
    DEPRECATED = 12
    ARCHIVED = 15
    DELETED = 18


@dataclass(eq=False, repr=False)
class Dimension(betterproto.Message):
    name: str = betterproto.string_field(4)
    dimension_id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(5)
    description: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionValue(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    dimension_id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    value: str = betterproto.string_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    display_name: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionFilter(betterproto.Message):
    dimension_id: str = betterproto.string_field(1)
    values: List[str] = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MapFeatureRef(betterproto.Message):
    layer_id: str = betterproto.string_field(1)
    feature_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValue(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    metric_id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    observation_period: "Period" = betterproto.message_field(3)
    # @exclude @inject_tag: `bigquery:"display_name"`
    map_feature_v2: "___maps_v2_external__.Feature" = betterproto.message_field(9)
    related_map_feature: "___maps_v2_external__.Feature" = betterproto.message_field(5)
    dimensions: List["DimensionValue"] = betterproto.message_field(6)
    supporting_values: List["MetricValueValue"] = betterproto.message_field(7)
    value: "MetricValueValue" = betterproto.message_field(2)
    flags: List["MetricValueFlag"] = betterproto.message_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValueValue(betterproto.Message):
    name: str = betterproto.string_field(1)
    unit: str = betterproto.string_field(2)
    number: float = betterproto.float_field(9, group="value")
    count: int = betterproto.int64_field(10, group="value")
    category: str = betterproto.string_field(11, group="value")

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValueFlag(betterproto.Message):
    code: str = betterproto.string_field(1)
    display_name: str = betterproto.string_field(2)
    detail: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Period(betterproto.Message):
    start: "___unatype__.Date" = betterproto.message_field(1)
    end: "___unatype__.Date" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricReport(betterproto.Message):
    observation_period: "Period" = betterproto.message_field(3)
    total_size: int = betterproto.int32_field(4)
    address_components: List["AddressComponentReport"] = betterproto.message_field(5)
    value_p1: float = betterproto.float_field(6)
    value_p5: float = betterproto.float_field(7)
    value_p25: float = betterproto.float_field(8)
    value_p50: float = betterproto.float_field(9)
    value_p75: float = betterproto.float_field(10)
    value_p95: float = betterproto.float_field(11)
    value_p99: float = betterproto.float_field(12)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddressComponentReport(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    component: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    cardinality: int = betterproto.int32_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    short_name: str = betterproto.string_field(3)
    display_name: str = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Lens(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    metric_id: str = betterproto.string_field(3)
    billing_account_id: str = betterproto.string_field(4)
    creator_email: str = betterproto.string_field(5)
    lens_filters: "LensFilters" = betterproto.message_field(6)
    display_name: str = betterproto.string_field(10)
    description: str = betterproto.string_field(11)
    update_time_string: str = betterproto.string_field(13)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class LensFilters(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    period_filters: List["Period"] = betterproto.message_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    dimension_filters: List["DimensionFilter"] = betterproto.message_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    address_component_filters: List[
        "___maps_v2_external__.AddressComponentFilter"
    ] = betterproto.message_field(3)
    feature_filters: List[str] = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Metric(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(3)
    description: str = betterproto.string_field(4)
    metric_versions: List["MetricVersion"] = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricVersion(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    catalog_id: str = betterproto.string_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    lifecycle_stage: "LifecycleStage" = betterproto.enum_field(9)
    version: "VersionSpec" = betterproto.message_field(18)
    spec: "MetricSpec" = betterproto.message_field(5)
    layer_id: str = betterproto.string_field(6)
    layer: "___maps_v2_external__.Layer" = betterproto.message_field(8)
    related_layer_id: str = betterproto.string_field(12)
    related_layer: "___maps_v2_external__.Layer" = betterproto.message_field(13)
    dimensions: List["Dimension"] = betterproto.message_field(7)
    name: str = betterproto.string_field(10)
    listing: str = betterproto.string_field(11)
    report: "MetricReport" = betterproto.message_field(14)
    your_subscription: "___subscription_v2_external__.SubscriptionStatus" = (
        betterproto.message_field(15)
    )
    your_lens: "Lens" = betterproto.message_field(17)
    description: str = betterproto.string_field(16)
    index_update_time: str = betterproto.string_field(20)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricSpec(betterproto.Message):
    layer_id: str = betterproto.string_field(1)
    related_layer_id: str = betterproto.string_field(2)
    cadence: "Cadence" = betterproto.enum_field(4)
    dimensions: List["DimensionSpec"] = betterproto.message_field(5)
    values: List["ValueSpec"] = betterproto.message_field(7)
    value_kind: "ValueKind" = betterproto.enum_field(3)
    unit: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class VersionSpec(betterproto.Message):
    version: str = betterproto.string_field(1)
    release_notes: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionSpec(betterproto.Message):
    dimension_id: str = betterproto.string_field(1)
    default_value: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValueSpec(betterproto.Message):
    name: str = betterproto.string_field(1)
    value_kind: "ValueKind" = betterproto.enum_field(2)
    unit: str = betterproto.string_field(3)
    display_name: str = betterproto.string_field(4)
    description: str = betterproto.string_field(5)
    supporting_value: bool = betterproto.bool_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Value(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


from .... import unatype as ___unatype__
from ....maps.v2 import external as ___maps_v2_external__
from ....subscription.v2 import external as ___subscription_v2_external__
