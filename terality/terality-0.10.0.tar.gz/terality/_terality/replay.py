from functools import partial

from common_client_scheduler.exceptions import TeralityInternalError
from terality._terality.encoding.decoder import decode
from common_client_scheduler.requests_responses import ComputationResponse
from terality_serde.recursive_apply import apply_async_func_on_object_recursively
from terality._terality.globals import global_client


def replay(bucket: str, key: str):
    """Helper to replay an API call stored in a S3 dump file.

    This function is internal to Terality, and is exposed here to help Terality engineers investigate CI
    and production failures.
    """
    response = global_client().poll_for_answer("replay", (bucket, key))

    if not isinstance(response, ComputationResponse):
        raise TeralityInternalError(
            f"Received unexpected response type (expected ComputationResponse): {response}"
        )

    result = response.result
    result = apply_async_func_on_object_recursively(
        result, partial(decode, global_client().get_aws_credentials())
    )
    return result
