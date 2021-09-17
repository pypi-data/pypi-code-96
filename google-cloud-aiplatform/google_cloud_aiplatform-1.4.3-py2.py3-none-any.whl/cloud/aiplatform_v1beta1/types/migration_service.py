# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.aiplatform_v1beta1.types import (
    migratable_resource as gca_migratable_resource,
)
from google.cloud.aiplatform_v1beta1.types import operation
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "SearchMigratableResourcesRequest",
        "SearchMigratableResourcesResponse",
        "BatchMigrateResourcesRequest",
        "MigrateResourceRequest",
        "BatchMigrateResourcesResponse",
        "MigrateResourceResponse",
        "BatchMigrateResourcesOperationMetadata",
    },
)


class SearchMigratableResourcesRequest(proto.Message):
    r"""Request message for
    [MigrationService.SearchMigratableResources][google.cloud.aiplatform.v1beta1.MigrationService.SearchMigratableResources].

    Attributes:
        parent (str):
            Required. The location that the migratable resources should
            be searched from. It's the Vertex AI location that the
            resources can be migrated to, not the resources' original
            location. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            The standard page size.
            The default and maximum value is 100.
        page_token (str):
            The standard page token.
        filter (str):
            A filter for your search. You can use the following types of
            filters:

            -  Resource type filters. The following strings filter for a
               specific type of
               [MigratableResource][google.cloud.aiplatform.v1beta1.MigratableResource]:

               -  ``ml_engine_model_version:*``
               -  ``automl_model:*``
               -  ``automl_dataset:*``
               -  ``data_labeling_dataset:*``

            -  "Migrated or not" filters. The following strings filter
               for resources that either have or have not already been
               migrated:

               -  ``last_migrate_time:*`` filters for migrated
                  resources.
               -  ``NOT last_migrate_time:*`` filters for not yet
                  migrated resources.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)


class SearchMigratableResourcesResponse(proto.Message):
    r"""Response message for
    [MigrationService.SearchMigratableResources][google.cloud.aiplatform.v1beta1.MigrationService.SearchMigratableResources].

    Attributes:
        migratable_resources (Sequence[google.cloud.aiplatform_v1beta1.types.MigratableResource]):
            All migratable resources that can be migrated
            to the location specified in the request.
        next_page_token (str):
            The standard next-page token. The migratable_resources may
            not fill page_size in SearchMigratableResourcesRequest even
            when there are subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    migratable_resources = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gca_migratable_resource.MigratableResource,
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class BatchMigrateResourcesRequest(proto.Message):
    r"""Request message for
    [MigrationService.BatchMigrateResources][google.cloud.aiplatform.v1beta1.MigrationService.BatchMigrateResources].

    Attributes:
        parent (str):
            Required. The location of the migrated resource will live
            in. Format: ``projects/{project}/locations/{location}``
        migrate_resource_requests (Sequence[google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest]):
            Required. The request messages specifying the
            resources to migrate. They must be in the same
            location as the destination. Up to 50 resources
            can be migrated in one batch.
    """

    parent = proto.Field(proto.STRING, number=1,)
    migrate_resource_requests = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MigrateResourceRequest",
    )


class MigrateResourceRequest(proto.Message):
    r"""Config of migrating one resource from automl.googleapis.com,
    datalabeling.googleapis.com and ml.googleapis.com to Vertex AI.

    Attributes:
        migrate_ml_engine_model_version_config (google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest.MigrateMlEngineModelVersionConfig):
            Config for migrating Version in
            ml.googleapis.com to Vertex AI's Model.
        migrate_automl_model_config (google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest.MigrateAutomlModelConfig):
            Config for migrating Model in
            automl.googleapis.com to Vertex AI's Model.
        migrate_automl_dataset_config (google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest.MigrateAutomlDatasetConfig):
            Config for migrating Dataset in
            automl.googleapis.com to Vertex AI's Dataset.
        migrate_data_labeling_dataset_config (google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest.MigrateDataLabelingDatasetConfig):
            Config for migrating Dataset in
            datalabeling.googleapis.com to Vertex AI's
            Dataset.
    """

    class MigrateMlEngineModelVersionConfig(proto.Message):
        r"""Config for migrating version in ml.googleapis.com to Vertex
        AI's Model.

        Attributes:
            endpoint (str):
                Required. The ml.googleapis.com endpoint that this model
                version should be migrated from. Example values:

                -  ml.googleapis.com

                -  us-centrall-ml.googleapis.com

                -  europe-west4-ml.googleapis.com

                -  asia-east1-ml.googleapis.com
            model_version (str):
                Required. Full resource name of ml engine model version.
                Format:
                ``projects/{project}/models/{model}/versions/{version}``.
            model_display_name (str):
                Required. Display name of the model in Vertex
                AI. System will pick a display name if
                unspecified.
        """

        endpoint = proto.Field(proto.STRING, number=1,)
        model_version = proto.Field(proto.STRING, number=2,)
        model_display_name = proto.Field(proto.STRING, number=3,)

    class MigrateAutomlModelConfig(proto.Message):
        r"""Config for migrating Model in automl.googleapis.com to Vertex
        AI's Model.

        Attributes:
            model (str):
                Required. Full resource name of automl Model. Format:
                ``projects/{project}/locations/{location}/models/{model}``.
            model_display_name (str):
                Optional. Display name of the model in Vertex
                AI. System will pick a display name if
                unspecified.
        """

        model = proto.Field(proto.STRING, number=1,)
        model_display_name = proto.Field(proto.STRING, number=2,)

    class MigrateAutomlDatasetConfig(proto.Message):
        r"""Config for migrating Dataset in automl.googleapis.com to
        Vertex AI's Dataset.

        Attributes:
            dataset (str):
                Required. Full resource name of automl Dataset. Format:
                ``projects/{project}/locations/{location}/datasets/{dataset}``.
            dataset_display_name (str):
                Required. Display name of the Dataset in
                Vertex AI. System will pick a display name if
                unspecified.
        """

        dataset = proto.Field(proto.STRING, number=1,)
        dataset_display_name = proto.Field(proto.STRING, number=2,)

    class MigrateDataLabelingDatasetConfig(proto.Message):
        r"""Config for migrating Dataset in datalabeling.googleapis.com
        to Vertex AI's Dataset.

        Attributes:
            dataset (str):
                Required. Full resource name of data labeling Dataset.
                Format: ``projects/{project}/datasets/{dataset}``.
            dataset_display_name (str):
                Optional. Display name of the Dataset in
                Vertex AI. System will pick a display name if
                unspecified.
            migrate_data_labeling_annotated_dataset_configs (Sequence[google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfig]):
                Optional. Configs for migrating
                AnnotatedDataset in datalabeling.googleapis.com
                to Vertex AI's SavedQuery. The specified
                AnnotatedDatasets have to belong to the
                datalabeling Dataset.
        """

        class MigrateDataLabelingAnnotatedDatasetConfig(proto.Message):
            r"""Config for migrating AnnotatedDataset in
            datalabeling.googleapis.com to Vertex AI's SavedQuery.

            Attributes:
                annotated_dataset (str):
                    Required. Full resource name of data labeling
                    AnnotatedDataset. Format:
                    ``projects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}``.
            """

            annotated_dataset = proto.Field(proto.STRING, number=1,)

        dataset = proto.Field(proto.STRING, number=1,)
        dataset_display_name = proto.Field(proto.STRING, number=2,)
        migrate_data_labeling_annotated_dataset_configs = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfig",
        )

    migrate_ml_engine_model_version_config = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="request",
        message=MigrateMlEngineModelVersionConfig,
    )
    migrate_automl_model_config = proto.Field(
        proto.MESSAGE, number=2, oneof="request", message=MigrateAutomlModelConfig,
    )
    migrate_automl_dataset_config = proto.Field(
        proto.MESSAGE, number=3, oneof="request", message=MigrateAutomlDatasetConfig,
    )
    migrate_data_labeling_dataset_config = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="request",
        message=MigrateDataLabelingDatasetConfig,
    )


class BatchMigrateResourcesResponse(proto.Message):
    r"""Response message for
    [MigrationService.BatchMigrateResources][google.cloud.aiplatform.v1beta1.MigrationService.BatchMigrateResources].

    Attributes:
        migrate_resource_responses (Sequence[google.cloud.aiplatform_v1beta1.types.MigrateResourceResponse]):
            Successfully migrated resources.
    """

    migrate_resource_responses = proto.RepeatedField(
        proto.MESSAGE, number=1, message="MigrateResourceResponse",
    )


class MigrateResourceResponse(proto.Message):
    r"""Describes a successfully migrated resource.
    Attributes:
        dataset (str):
            Migrated Dataset's resource name.
        model (str):
            Migrated Model's resource name.
        migratable_resource (google.cloud.aiplatform_v1beta1.types.MigratableResource):
            Before migration, the identifier in
            ml.googleapis.com, automl.googleapis.com or
            datalabeling.googleapis.com.
    """

    dataset = proto.Field(proto.STRING, number=1, oneof="migrated_resource",)
    model = proto.Field(proto.STRING, number=2, oneof="migrated_resource",)
    migratable_resource = proto.Field(
        proto.MESSAGE, number=3, message=gca_migratable_resource.MigratableResource,
    )


class BatchMigrateResourcesOperationMetadata(proto.Message):
    r"""Runtime operation information for
    [MigrationService.BatchMigrateResources][google.cloud.aiplatform.v1beta1.MigrationService.BatchMigrateResources].

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            The common part of the operation metadata.
        partial_results (Sequence[google.cloud.aiplatform_v1beta1.types.BatchMigrateResourcesOperationMetadata.PartialResult]):
            Partial results that reflect the latest
            migration operation progress.
    """

    class PartialResult(proto.Message):
        r"""Represents a partial result in batch migration operation for one
        [MigrateResourceRequest][google.cloud.aiplatform.v1beta1.MigrateResourceRequest].

        Attributes:
            error (google.rpc.status_pb2.Status):
                The error result of the migration request in
                case of failure.
            model (str):
                Migrated model resource name.
            dataset (str):
                Migrated dataset resource name.
            request (google.cloud.aiplatform_v1beta1.types.MigrateResourceRequest):
                It's the same as the value in
                [MigrateResourceRequest.migrate_resource_requests][].
        """

        error = proto.Field(
            proto.MESSAGE, number=2, oneof="result", message=status_pb2.Status,
        )
        model = proto.Field(proto.STRING, number=3, oneof="result",)
        dataset = proto.Field(proto.STRING, number=4, oneof="result",)
        request = proto.Field(
            proto.MESSAGE, number=1, message="MigrateResourceRequest",
        )

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )
    partial_results = proto.RepeatedField(
        proto.MESSAGE, number=2, message=PartialResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
