"""
## Description
---
This command helps to update metrics analyzer's data sources.
Run `caeops metrics-analyzers update --help` for more help.

## Synopsis
---
```
  update
--name [value]
--data-sources [value]
```

## Options
---
--name (string)

> Name of the analyzer

--data-sources (string)

> Name of resource for which you want to update metrics analyzer

## Examples
---
To update data sources of a metrics analyzer.

The following `metrics-analyzers update` example updates data sources of a metrics analyzer.

```
caeops metrics-analyzers update --name=examplename --data-sources=[{metrics=example1},{metrics=example2}]
```


## Output
---
metrics analyzer details -> (structure)

- **serviceName** -> (string)  
Name of the metrics analyzer
- **serviceType** -> (string)  
Type of the resource (e.g metrics-analyzer)
- **groupName** -> (string)  
Name of the service group to which the Metrics analyzer is added
- **dataSources** -> (structure)  
List of the data sources and their type(e.g {"metrics":"example"})
- **createdAt** -> (long)  
Creation timestamp
- **updatedAt** -> (long)  
Last modified timestamp

"""

import json
from caeops.common.api_helper import generate_error_response_text
from caeops.utilities import validate_mandatory_fields

from caeops.common.api_helper import parse_rest_api_response
from caeops.common.labels_format import labels_format
from caeops.common.validators import validate_tenant_in_session
from caeops.utilities import generate_auth_headers
from caeops.configurations import read
from caeops.global_settings import ConfigKeys

import requests

from caeops.utilities import KubernetesProvisioningUrl


def update(payload, tenant_id):
    """This function calls the rest API to update metrics analyzer
    Parameters
    --------
    tenant_id : Id of tenant admin
    payload : it conatins details as entered by user

    Raises
    --------
    RuntimeError
        The response from server if the payload was incorrect
    """
    url = (
        KubernetesProvisioningUrl
        + "/v1/tenants/"
        + tenant_id
        + "/metrics-analyzers/"
        + payload["name"]
        + "/data-sources"
    )
    res = requests.put(
        url=url,
        json=payload or {},
        headers=generate_auth_headers(ConfigKeys.ID_TOKEN),
    )
    # Parse and return the response
    return parse_rest_api_response(res)


def metrics_analyzer_update(payload):
    """This function checks the validity of payload and invokes update function
    Parameters
    --------
    payload : it conatins details as entered by user
    """
    # validate tenant in session
    tenant_id = read(ConfigKeys.TENANT_ID)
    if not validate_tenant_in_session(tenant_id):
        exit(1)
    # Validate for mandatory fields
    validate_mandatory_fields(
        payload,
        ["name", "data-sources"],
    )
    try:
        # Convert data-source into json format
        new_data_sources = labels_format(payload["dataSources"])
        payload["dataSources"] = new_data_sources
        response = update(payload, tenant_id)
        print(json.dumps(response, indent=2))
        return response
    except KeyboardInterrupt:
        print("")
        return None
    except Exception as e:
        err_message = generate_error_response_text("update")
        print(f"{err_message} : {(str(e))}")
        return None
