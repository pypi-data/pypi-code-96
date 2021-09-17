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


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1", manifest={"DeployedIndexRef",},
)


class DeployedIndexRef(proto.Message):
    r"""Points to a DeployedIndex.
    Attributes:
        index_endpoint (str):
            Immutable. A resource name of the
            IndexEndpoint.
        deployed_index_id (str):
            Immutable. The ID of the DeployedIndex in the
            above IndexEndpoint.
    """

    index_endpoint = proto.Field(proto.STRING, number=1,)
    deployed_index_id = proto.Field(proto.STRING, number=2,)


__all__ = tuple(sorted(__protobuf__.manifest))
