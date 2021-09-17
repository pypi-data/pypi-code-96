"""
## Description
---
This command helps you get labels of a Logs Service.
Run `caeops logs get-labels --help` for more help.

## Synopsis
---
```
  get-labels
--name [value]
```

## Options
---

--name (string)

> Logs Service name

## Examples
---
To get labels of a Logs Service.

The following `logs get-labels` example gets labels of a Logs Service.

```
caeops logs get-labels --name=name 
```


## Output
---
Label details -> (Structure)

- **key** -> (string)  
Name  of the field
- **value** -> (string)  
Value of the field

"""

import json
from caeops.common.api_helper import (
    generate_error_response_text,
    parse_rest_api_response,
)
from caeops.utilities import validate_mandatory_fields
from caeops.common.validators import validate_tenant_in_session
import requests

from caeops.global_settings import ConfigKeys
from caeops.configurations import read
from caeops.utilities import CentralizedMetricsUrl, generate_auth_headers


def get_labels(payload, tenant_id):
    url = (
        CentralizedMetricsUrl
        + "/v1/tenants/"
        + tenant_id
        + "/logs/"
        + payload["name"]
        + "/labels"
    )
    res = requests.get(
        url=url, json=payload, headers=generate_auth_headers(ConfigKeys.ID_TOKEN)
    )
    # Parse and return the response
    return parse_rest_api_response(res)


def logs_get_labels(payload):
    # Read tenantid from config.ini and add it to the request if it is not null
    tenant_id = read(ConfigKeys.TENANT_ID)
    if not validate_tenant_in_session(tenant_id):
        exit(1)
    # Validate for mandatory fields
    validate_mandatory_fields(
        payload,
        ["name"],
    )
    try:
        response = get_labels(payload, tenant_id)
        print(json.dumps(response, indent=2))
        return response
    except KeyboardInterrupt:
        print("")
        return None
    except Exception as e:
        err_message = generate_error_response_text("get-labels")
        print(f"{err_message} : {(str(e))}")
        return None
