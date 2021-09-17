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


import abc
import datetime
import pathlib
from collections import namedtuple
import logging
import re
from typing import Any, Dict, Match, Optional, Type, TypeVar, Tuple

from google.api_core import client_options
from google.api_core import gapic_v1
from google.auth import credentials as auth_credentials
from google.cloud import storage

from google.cloud.aiplatform import compat
from google.cloud.aiplatform import constants
from google.cloud.aiplatform import initializer

from google.cloud.aiplatform.compat.services import (
    dataset_service_client_v1beta1,
    endpoint_service_client_v1beta1,
    job_service_client_v1beta1,
    model_service_client_v1beta1,
    pipeline_service_client_v1beta1,
    prediction_service_client_v1beta1,
    metadata_service_client_v1beta1,
    tensorboard_service_client_v1beta1,
)
from google.cloud.aiplatform.compat.services import (
    dataset_service_client_v1,
    endpoint_service_client_v1,
    job_service_client_v1,
    model_service_client_v1,
    pipeline_service_client_v1,
    prediction_service_client_v1,
)

from google.cloud.aiplatform.compat.types import (
    accelerator_type as gca_accelerator_type,
)

VertexAiServiceClient = TypeVar(
    "VertexAiServiceClient",
    # v1beta1
    dataset_service_client_v1beta1.DatasetServiceClient,
    endpoint_service_client_v1beta1.EndpointServiceClient,
    model_service_client_v1beta1.ModelServiceClient,
    prediction_service_client_v1beta1.PredictionServiceClient,
    pipeline_service_client_v1beta1.PipelineServiceClient,
    job_service_client_v1beta1.JobServiceClient,
    metadata_service_client_v1beta1.MetadataServiceClient,
    # v1
    dataset_service_client_v1.DatasetServiceClient,
    endpoint_service_client_v1.EndpointServiceClient,
    model_service_client_v1.ModelServiceClient,
    prediction_service_client_v1.PredictionServiceClient,
    pipeline_service_client_v1.PipelineServiceClient,
    job_service_client_v1.JobServiceClient,
)

RESOURCE_NAME_PATTERN = re.compile(
    r"^projects\/(?P<project>[\w-]+)\/locations\/(?P<location>[\w-]+)\/(?P<resource>[\w\-\/]+)\/(?P<id>[\w-]+)$"
)
RESOURCE_ID_PATTERN = re.compile(r"^[\w-]+$")

Fields = namedtuple("Fields", ["project", "location", "resource", "id"],)


def _match_to_fields(match: Match) -> Optional[Fields]:
    """Normalize RegEx groups from resource name pattern Match to class
    Fields."""
    if not match:
        return None

    return Fields(
        project=match["project"],
        location=match["location"],
        resource=match["resource"],
        id=match["id"],
    )


def validate_id(resource_id: str) -> bool:
    """Validate int64 resource ID number."""
    return bool(RESOURCE_ID_PATTERN.match(resource_id))


def extract_fields_from_resource_name(
    resource_name: str, resource_noun: Optional[str] = None
) -> Optional[Fields]:
    """Validates and returns extracted fields from a fully-qualified resource
    name. Returns None if name is invalid.

    Args:
        resource_name (str):
            Required. A fully-qualified Vertex AI resource name

        resource_noun (str):
            A resource noun to validate the resource name against.
            For example, you would pass "datasets" to validate
            "projects/123/locations/us-central1/datasets/456".
            In the case of deeper naming structures, e.g.,
            "projects/123/locations/us-central1/metadataStores/123/contexts/456",
            you would pass "metadataStores/123/contexts" as the resource_noun.
    Returns:
        fields (Fields):
            A named tuple containing four extracted fields from a resource name:
            project, location, resource, and id. These fields can be used for
            subsequent method calls in the SDK.
    """
    fields = _match_to_fields(RESOURCE_NAME_PATTERN.match(resource_name))

    if not fields:
        return None
    if resource_noun and fields.resource != resource_noun:
        return None

    return fields


def full_resource_name(
    resource_name: str,
    resource_noun: str,
    project: Optional[str] = None,
    location: Optional[str] = None,
) -> str:
    """Returns fully qualified resource name.

    Args:
        resource_name (str):
            Required. A fully-qualified Vertex AI resource name or
            resource ID.
        resource_noun (str):
            A resource noun to validate the resource name against.
            For example, you would pass "datasets" to validate
            "projects/123/locations/us-central1/datasets/456".
            In the case of deeper naming structures, e.g.,
            "projects/123/locations/us-central1/metadataStores/123/contexts/456",
            you would pass "metadataStores/123/contexts" as the resource_noun.
        project (str):
            Optional project to retrieve resource_noun from. If not set, project
            set in aiplatform.init will be used.
        location (str):
            Optional location to retrieve resource_noun from. If not set, location
            set in aiplatform.init will be used.

    Returns:
        resource_name (str):
            A fully-qualified Vertex AI resource name.

    Raises:
        ValueError:
            If resource name, resource ID or project ID not provided.
    """
    validate_resource_noun(resource_noun)
    # Fully qualified resource name, e.g., "projects/.../locations/.../datasets/12345" or
    # "projects/.../locations/.../metadataStores/.../contexts/12345"
    valid_name = extract_fields_from_resource_name(
        resource_name=resource_name, resource_noun=resource_noun
    )

    user_project = project or initializer.global_config.project
    user_location = location or initializer.global_config.location

    # Partial resource name (i.e. "12345") with known project and location
    if (
        not valid_name
        and validate_project(user_project)
        and validate_region(user_location)
        and validate_id(resource_name)
    ):
        resource_name = f"projects/{user_project}/locations/{user_location}/{resource_noun}/{resource_name}"
    # Invalid resource_name parameter
    elif not valid_name:
        raise ValueError(f"Please provide a valid {resource_noun[:-1]} name or ID")

    return resource_name


# TODO(b/172286889) validate resource noun
def validate_resource_noun(resource_noun: str) -> bool:
    """Validates resource noun.

    Args:
        resource_noun: resource noun to validate
    Returns:
        bool: True if no errors raised
    Raises:
        ValueError: If resource noun not supported.
    """
    if resource_noun:
        return True
    raise ValueError("Please provide a valid resource noun")


# TODO(b/172288287) validate project
def validate_project(project: str) -> bool:
    """Validates project.

    Args:
        project: project to validate
    Returns:
        bool: True if no errors raised
    Raises:
        ValueError: If project does not exist.
    """
    if project:
        return True
    raise ValueError("Please provide a valid project ID")


# TODO(b/172932277) verify display name only contains utf-8 chars
def validate_display_name(display_name: str):
    """Verify display name is at most 128 chars.

    Args:
        display_name: display name to verify
    Raises:
        ValueError: display name is longer than 128 characters
    """
    if len(display_name) > 128:
        raise ValueError("Display name needs to be less than 128 characters.")


def validate_labels(labels: Dict[str, str]):
    """Validate labels.

    Args:
        labels: labels to verify
    Raises:
        ValueError: if labels is not a mapping of string key value pairs.
    """
    for k, v in labels.items():
        if not isinstance(k, str) or not isinstance(v, str):
            raise ValueError(
                "Expect labels to be a mapping of string key value pairs. "
                'Got "{}".'.format(labels)
            )


def validate_region(region: str) -> bool:
    """Validates region against supported regions.

    Args:
        region: region to validate
    Returns:
        bool: True if no errors raised
    Raises:
        ValueError: If region is not in supported regions.
    """
    if not region:
        raise ValueError(
            f"Please provide a region, select from {constants.SUPPORTED_REGIONS}"
        )

    region = region.lower()
    if region not in constants.SUPPORTED_REGIONS:
        raise ValueError(
            f"Unsupported region for Vertex AI, select from {constants.SUPPORTED_REGIONS}"
        )

    return True


def validate_accelerator_type(accelerator_type: str) -> bool:
    """Validates user provided accelerator_type string for training and
    prediction.

    Args:
        accelerator_type (str):
            Represents a hardware accelerator type.
    Returns:
        bool: True if valid accelerator_type
    Raises:
        ValueError if accelerator type is invalid.
    """
    if accelerator_type not in gca_accelerator_type.AcceleratorType._member_names_:
        raise ValueError(
            f"Given accelerator_type `{accelerator_type}` invalid. "
            f"Choose one of {gca_accelerator_type.AcceleratorType._member_names_}"
        )
    return True


def extract_bucket_and_prefix_from_gcs_path(gcs_path: str) -> Tuple[str, Optional[str]]:
    """Given a complete GCS path, return the bucket name and prefix as a tuple.

    Example Usage:

        bucket, prefix = extract_bucket_and_prefix_from_gcs_path(
            "gs://example-bucket/path/to/folder"
        )

        # bucket = "example-bucket"
        # prefix = "path/to/folder"

    Args:
        gcs_path (str):
            Required. A full path to a Google Cloud Storage folder or resource.
            Can optionally include "gs://" prefix or end in a trailing slash "/".

    Returns:
        Tuple[str, Optional[str]]
            A (bucket, prefix) pair from provided GCS path. If a prefix is not
            present, a None will be returned in its place.
    """
    if gcs_path.startswith("gs://"):
        gcs_path = gcs_path[5:]
    if gcs_path.endswith("/"):
        gcs_path = gcs_path[:-1]

    gcs_parts = gcs_path.split("/", 1)
    gcs_bucket = gcs_parts[0]
    gcs_blob_prefix = None if len(gcs_parts) == 1 else gcs_parts[1]

    return (gcs_bucket, gcs_blob_prefix)


class ClientWithOverride:
    class WrappedClient:
        """Wrapper class for client that creates client at API invocation
        time."""

        def __init__(
            self,
            client_class: Type[VertexAiServiceClient],
            client_options: client_options.ClientOptions,
            client_info: gapic_v1.client_info.ClientInfo,
            credentials: Optional[auth_credentials.Credentials] = None,
        ):
            """Stores parameters needed to instantiate client.

            Args:
                client_class (VertexAiServiceClient):
                    Required. Class of the client to use.
                client_options (client_options.ClientOptions):
                    Required. Client options to pass to client.
                client_info (gapic_v1.client_info.ClientInfo):
                    Required. Client info to pass to client.
                credentials (auth_credentials.credentials):
                    Optional. Client credentials to pass to client.
            """

            self._client_class = client_class
            self._credentials = credentials
            self._client_options = client_options
            self._client_info = client_info

        def __getattr__(self, name: str) -> Any:
            """Instantiates client and returns attribute of the client."""
            temporary_client = self._client_class(
                credentials=self._credentials,
                client_options=self._client_options,
                client_info=self._client_info,
            )
            return getattr(temporary_client, name)

    @property
    @abc.abstractmethod
    def _is_temporary(self) -> bool:
        pass

    @property
    @classmethod
    @abc.abstractmethod
    def _default_version(self) -> str:
        pass

    @property
    @classmethod
    @abc.abstractmethod
    def _version_map(self) -> Tuple:
        pass

    def __init__(
        self,
        client_options: client_options.ClientOptions,
        client_info: gapic_v1.client_info.ClientInfo,
        credentials: Optional[auth_credentials.Credentials] = None,
    ):
        """Stores parameters needed to instantiate client.

        Args:
            client_options (client_options.ClientOptions):
                Required. Client options to pass to client.
            client_info (gapic_v1.client_info.ClientInfo):
                Required. Client info to pass to client.
            credentials (auth_credentials.credentials):
                Optional. Client credentials to pass to client.
        """

        self._clients = {
            version: self.WrappedClient(
                client_class=client_class,
                client_options=client_options,
                client_info=client_info,
                credentials=credentials,
            )
            if self._is_temporary
            else client_class(
                client_options=client_options,
                client_info=client_info,
                credentials=credentials,
            )
            for version, client_class in self._version_map
        }

    def __getattr__(self, name: str) -> Any:
        """Instantiates client and returns attribute of the client."""
        return getattr(self._clients[self._default_version], name)

    def select_version(self, version: str) -> VertexAiServiceClient:
        return self._clients[version]


class DatasetClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, dataset_service_client_v1.DatasetServiceClient),
        (compat.V1BETA1, dataset_service_client_v1beta1.DatasetServiceClient),
    )


class EndpointClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, endpoint_service_client_v1.EndpointServiceClient),
        (compat.V1BETA1, endpoint_service_client_v1beta1.EndpointServiceClient),
    )


class JobClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, job_service_client_v1.JobServiceClient),
        (compat.V1BETA1, job_service_client_v1beta1.JobServiceClient),
    )


class ModelClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, model_service_client_v1.ModelServiceClient),
        (compat.V1BETA1, model_service_client_v1beta1.ModelServiceClient),
    )


class PipelineClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, pipeline_service_client_v1.PipelineServiceClient),
        (compat.V1BETA1, pipeline_service_client_v1beta1.PipelineServiceClient),
    )


class PipelineJobClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.V1BETA1
    _version_map = (
        (compat.V1BETA1, pipeline_service_client_v1beta1.PipelineServiceClient),
    )


class PredictionClientWithOverride(ClientWithOverride):
    _is_temporary = False
    _default_version = compat.DEFAULT_VERSION
    _version_map = (
        (compat.V1, prediction_service_client_v1.PredictionServiceClient),
        (compat.V1BETA1, prediction_service_client_v1beta1.PredictionServiceClient),
    )


class MetadataClientWithOverride(ClientWithOverride):
    _is_temporary = True
    _default_version = compat.V1BETA1
    _version_map = (
        (compat.V1BETA1, metadata_service_client_v1beta1.MetadataServiceClient),
    )


class TensorboardClientWithOverride(ClientWithOverride):
    _is_temporary = False
    _default_version = compat.V1BETA1
    _version_map = (
        (compat.V1BETA1, tensorboard_service_client_v1beta1.TensorboardServiceClient),
    )


VertexAiServiceClientWithOverride = TypeVar(
    "VertexAiServiceClientWithOverride",
    DatasetClientWithOverride,
    EndpointClientWithOverride,
    JobClientWithOverride,
    ModelClientWithOverride,
    PipelineClientWithOverride,
    PipelineJobClientWithOverride,
    PredictionClientWithOverride,
    MetadataClientWithOverride,
    TensorboardClientWithOverride,
)


class LoggingFilter(logging.Filter):
    def __init__(self, warning_level: int):
        self._warning_level = warning_level

    def filter(self, record):
        return record.levelname == self._warning_level


def _timestamped_gcs_dir(root_gcs_path: str, dir_name_prefix: str) -> str:
    """Composes a timestamped GCS directory.

    Args:
        root_gcs_path: GCS path to put the timestamped directory.
        dir_name_prefix: Prefix to add the timestamped directory.
    Returns:
        Timestamped gcs directory path in root_gcs_path.
    """
    timestamp = datetime.datetime.now().isoformat(sep="-", timespec="milliseconds")
    dir_name = "-".join([dir_name_prefix, timestamp])
    if root_gcs_path.endswith("/"):
        root_gcs_path = root_gcs_path[:-1]
    gcs_path = "/".join([root_gcs_path, dir_name])
    if not gcs_path.startswith("gs://"):
        return "gs://" + gcs_path
    return gcs_path


def _timestamped_copy_to_gcs(
    local_file_path: str,
    gcs_dir: str,
    project: Optional[str] = None,
    credentials: Optional[auth_credentials.Credentials] = None,
) -> str:
    """Copies a local file to a GCS path.

    The file copied to GCS is the name of the local file prepended with an
    "aiplatform-{timestamp}-" string.

    Args:
        local_file_path (str): Required. Local file to copy to GCS.
        gcs_dir (str):
            Required. The GCS directory to copy to.
        project (str):
            Project that contains the staging bucket. Default will be used if not
            provided. Model Builder callers should pass this in.
        credentials (auth_credentials.Credentials):
            Custom credentials to use with bucket. Model Builder callers should pass
            this in.
    Returns:
        gcs_path (str): The path of the copied file in gcs.
    """

    gcs_bucket, gcs_blob_prefix = extract_bucket_and_prefix_from_gcs_path(gcs_dir)

    local_file_name = pathlib.Path(local_file_path).name
    timestamp = datetime.datetime.now().isoformat(sep="-", timespec="milliseconds")
    blob_path = "-".join(["aiplatform", timestamp, local_file_name])

    if gcs_blob_prefix:
        blob_path = "/".join([gcs_blob_prefix, blob_path])

    # TODO(b/171202993) add user agent
    client = storage.Client(project=project, credentials=credentials)
    bucket = client.bucket(gcs_bucket)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_file_path)

    gcs_path = "".join(["gs://", "/".join([blob.bucket.name, blob.name])])
    return gcs_path
