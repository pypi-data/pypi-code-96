import logging
from typing import List, Optional

from requests import Response

from cognite.well_model.client._api_client import APIClient
from cognite.well_model.client.api.api_base import BaseAPI
from cognite.well_model.client.api.merge_rules.wells import WellMergeRulesAPI
from cognite.well_model.client.models.resource_list import WellList
from cognite.well_model.client.utils._identifier_list import identifier_items, identifier_items_single
from cognite.well_model.client.utils.multi_request import cursor_multi_request
from cognite.well_model.models import (
    AssetSource,
    DateRange,
    DeleteWells,
    DistanceRange,
    IdentifierItems,
    PolygonFilter,
    Well,
    WellFilter,
    WellFilterRequest,
    WellIngestion,
    WellIngestionItems,
    WellItems,
    WellMeasurementFilter,
    WellNdsFilter,
    WellNptFilter,
    WellSearch,
    WellTrajectoryFilter,
)

logger = logging.getLogger(__name__)


class WellsAPI(BaseAPI):
    def __init__(self, client: APIClient):
        super().__init__(client)
        self.merge_rules = WellMergeRulesAPI(client)

    def ingest(self, ingestions: List[WellIngestion]) -> WellList:
        path = self._get_path("/wells")
        json = WellIngestionItems(items=ingestions).json()
        response: Response = self.client.post(path, json)
        well_items: WellItems = WellItems.parse_obj(response.json())
        items: List[Well] = well_items.items
        return WellList(items)

    def delete(self, well_sources: List[AssetSource]):
        path = self._get_path("/wells/delete")
        json = DeleteWells(items=well_sources).json()
        self.client.post(path, json)

    # guranteed to be non-empty list
    def _retrieve_multiple(self, identifiers: IdentifierItems) -> List[Well]:
        path: str = self._get_path("/wells/byids")
        response: Response = self.client.post(url_path=path, json=identifiers.json())
        wells: List[Well] = WellItems.parse_raw(response.text).items
        return wells

    def retrieve(self, asset_external_id: Optional[str] = None, matching_id: Optional[str] = None) -> Well:
        """
        Get well by asset external id or matching id

        @param asset_external_id: Well asset external id
        @param matching_id: Well matching id
        @return: Well object
        """
        identifiers = identifier_items_single(asset_external_id, matching_id)
        return self._retrieve_multiple(identifiers)[0]

    def retrieve_multiple(
        self, asset_external_ids: Optional[List[str]] = None, matching_ids: Optional[List[str]] = None
    ) -> WellList:
        """
        Get wells by a list of asset external ids and matching ids

        @param asset_external_ids: list of well asset external ids
        @param matching_ids: List of well matching ids
        """
        identifiers = identifier_items(asset_external_ids, matching_ids)
        return WellList(self._retrieve_multiple(identifiers))

    def list(
        self,
        string_matching: Optional[str] = None,
        quadrants: Optional[List[str]] = None,
        blocks: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        operators: Optional[List[str]] = None,
        sources: Optional[List[str]] = None,
        water_depth: Optional[DistanceRange] = None,
        spud_date: Optional[DateRange] = None,
        well_types: Optional[List[str]] = None,
        licenses: Optional[List[str]] = None,
        trajectories: Optional[WellTrajectoryFilter] = None,
        measurements: Optional[WellMeasurementFilter] = None,
        npt: Optional[WellNptFilter] = None,
        nds: Optional[WellNdsFilter] = None,
        polygon: Optional[PolygonFilter] = None,
        output_crs: Optional[str] = None,
        limit=100,
    ) -> WellList:
        """
        Get wells that matches the filter

        @param string_matching - string to fuzzy match on description and name
        @param quadrants - list of quadrants to find wells within
        @param blocks - list of blocks to find wells within
        @param fields - list of fields to find wells within
        @param operators - list of well operators to filter on
        @param sources - list of source system names
        @param water_depth - TODO
        @param spud_date - TODO
        @param licenses - list of well licenses
        @param well_types - list of well types, for example exploration
        @param trajectories - filter wells which have trajectory between certain depths
        @param measurements - filter wells which have measurements between certain depths in their logs
        @param npt - filter wells on Npt
        @param nds - filter wells on Nds
        @param polygon - geographic area to find wells within
        @param output_crs - crs for the returned well head
        @param limit - number of well objects to fetch
        @return: WellItems object
        """

        def request(cursor):
            search = WellSearch(query=string_matching) if string_matching else None
            well_filter = WellFilterRequest(
                filter=WellFilter(
                    quadrants=quadrants,
                    blocks=blocks,
                    fields=fields,
                    operators=operators,
                    well_types=well_types,
                    licenses=licenses,
                    sources=sources,
                    water_depth=water_depth,
                    spud_date=spud_date,
                    trajectories=trajectories,
                    measurements=measurements,
                    polygon=polygon,
                    npt=npt,
                    nds=nds,
                ),
                search=search,
                output_crs=output_crs,
                cursor=cursor,
            )
            path: str = self._get_path("/wells/list")
            response: Response = self.client.post(url_path=path, json=well_filter.json())
            well_items_data: WellItems = WellItems.parse_raw(response.text)
            return well_items_data

        items = cursor_multi_request(
            get_cursor=self._get_cursor, get_items=self._get_items, limit=limit, request=request
        )
        return WellList(items)

    @staticmethod
    def _get_items(well_items: WellItems) -> List[Well]:
        items: List[Well] = well_items.items  # For mypy
        return items

    @staticmethod
    def _get_cursor(well_items: WellItems) -> Optional[str]:
        next_cursor: Optional[str] = well_items.next_cursor  # For mypy
        return next_cursor
