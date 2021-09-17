# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/scorecard/v1/scorecard_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


class NormStrategy(betterproto.Enum):
    UNSPECIFIED = 0
    MIN_MAX = 1
    QUANTILE = 2


@dataclass(eq=False, repr=False)
class CreateScoresRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)
    filter: "__catalog_v1__.QueryMetricFilters" = betterproto.message_field(5)
    config: "ScoreConfig" = betterproto.message_field(6)
    high_scores_size: int = betterproto.int32_field(10)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateScoresResponse(betterproto.Message):
    high_scores: List["FeatureScore"] = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListValuesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)
    cadence: "__metric_v1__.Cadence" = betterproto.enum_field(3)
    billing_context: str = betterproto.string_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListValuesResponse(betterproto.Message):
    values: List["ScorableValue"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ScorableValue(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    value: "__metric_v1__.ValueSpec" = betterproto.message_field(3)
    metric_display_name: str = betterproto.string_field(5)
    metric_description: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ScoreConfig(betterproto.Message):
    values: List["ValueScoreConfig"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValueScoreConfig(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    value_name: str = betterproto.string_field(3)
    weight: int = betterproto.int32_field(5)
    norm_strategy: "NormStrategy" = betterproto.enum_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class FeatureScore(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)
    feature_id: str = betterproto.string_field(3)
    observation_start_date_string: str = betterproto.string_field(4)
    total_score: int = betterproto.int32_field(7)
    sub_scores: List["SubScore"] = betterproto.message_field(8)
    feature_display_name: str = betterproto.string_field(10)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SubScore(betterproto.Message):
    metric_id: str = betterproto.string_field(1)
    value_name: str = betterproto.string_field(2)
    num_value: float = betterproto.float_field(4)
    norm_value: float = betterproto.float_field(5)
    quantile_value: float = betterproto.float_field(6)
    weighted_value: float = betterproto.float_field(7)
    norm_strategy: "NormStrategy" = betterproto.enum_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


class ScoreCardServiceStub(betterproto.ServiceStub):
    """* This is the service for Scorecard"""

    async def create_scores(
        self,
        *,
        catalog_id: str = "",
        billing_context: str = "",
        filter: "__catalog_v1__.QueryMetricFilters" = None,
        config: "ScoreConfig" = None,
        high_scores_size: int = 0,
    ) -> "CreateScoresResponse":

        request = CreateScoresRequest()
        request.catalog_id = catalog_id
        request.billing_context = billing_context
        if filter is not None:
            request.filter = filter
        if config is not None:
            request.config = config
        request.high_scores_size = high_scores_size

        return await self._unary_unary(
            "/unacast.scorecard.v1.ScoreCardService/CreateScores",
            request,
            CreateScoresResponse,
        )

    async def list_values(
        self,
        *,
        catalog_id: str = "",
        layer_id: str = "",
        cadence: "__metric_v1__.Cadence" = None,
        billing_context: str = "",
    ) -> "ListValuesResponse":

        request = ListValuesRequest()
        request.catalog_id = catalog_id
        request.layer_id = layer_id
        request.cadence = cadence
        request.billing_context = billing_context

        return await self._unary_unary(
            "/unacast.scorecard.v1.ScoreCardService/ListValues",
            request,
            ListValuesResponse,
        )


from ...catalog import v1 as __catalog_v1__
from ...metric import v1 as __metric_v1__
