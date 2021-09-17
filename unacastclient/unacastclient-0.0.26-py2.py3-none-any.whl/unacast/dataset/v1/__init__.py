# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/dataset/v1/dataset_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class CreateDatasetRequest(betterproto.Message):
    spec: "DatasetSpec" = betterproto.message_field(1)
    given_id: str = betterproto.string_field(2)
    catalog_id: str = betterproto.string_field(3)
    display_name: str = betterproto.string_field(7)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Dataset(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(5)
    spec: "DatasetSpec" = betterproto.message_field(13)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DatasetSpec(betterproto.Message):
    layer_id: str = betterproto.string_field(1)
    cadence: "__metric_v1__.Cadence" = betterproto.enum_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


class DatasetServiceStub(betterproto.ServiceStub):
    """* This is the service used to interact with the dataset"""

    async def create_dataset(
        self,
        *,
        spec: "DatasetSpec" = None,
        given_id: str = "",
        catalog_id: str = "",
        display_name: str = "",
    ) -> "Dataset":

        request = CreateDatasetRequest()
        if spec is not None:
            request.spec = spec
        request.given_id = given_id
        request.catalog_id = catalog_id
        request.display_name = display_name

        return await self._unary_unary(
            "/unacast.dataset.v1.DatasetService/CreateDataset", request, Dataset
        )


from ...metric import v1 as __metric_v1__
