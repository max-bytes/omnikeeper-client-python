# okclient.AnsibleInventoryScanIngestApi

All URIs are relative to *https://localhost:44378*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ansible_inventory_scan_ingest_ingest_ansible_inventory_scan**](AnsibleInventoryScanIngestApi.md#ansible_inventory_scan_ingest_ingest_ansible_inventory_scan) | **POST** /api/v{version}/Ingest/AnsibleInventoryScan | 


# **ansible_inventory_scan_ingest_ingest_ansible_inventory_scan**
> ansible_inventory_scan_ingest_ingest_ansible_inventory_scan(write_layer_id, search_layer_ids, version, ansible_inventory_scan_dto)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import ansible_inventory_scan_ingest_api
from okclient.model.ansible_inventory_scan_dto import AnsibleInventoryScanDTO
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:44378
# See configuration.py for a list of all supported configuration parameters.
configuration = okclient.Configuration(
    host = "https://localhost:44378"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = okclient.Configuration(
    host = "https://localhost:44378"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth2
configuration = okclient.Configuration(
    host = "https://localhost:44378"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with okclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible_inventory_scan_ingest_api.AnsibleInventoryScanIngestApi(api_client)
    write_layer_id = "writeLayerID_example" # str | 
    search_layer_ids = [
        "searchLayerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    ansible_inventory_scan_dto = AnsibleInventoryScanDTO(
        setup_facts={
            "key": "key_example",
        },
        yum_installed={
            "key": "key_example",
        },
        yum_repos={
            "key": "key_example",
        },
        yum_updates={
            "key": "key_example",
        },
    ) # AnsibleInventoryScanDTO | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ansible_inventory_scan_ingest_ingest_ansible_inventory_scan(write_layer_id, search_layer_ids, version, ansible_inventory_scan_dto)
    except okclient.ApiException as e:
        print("Exception when calling AnsibleInventoryScanIngestApi->ansible_inventory_scan_ingest_ingest_ansible_inventory_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **write_layer_id** | **str**|  |
 **search_layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **ansible_inventory_scan_dto** | [**AnsibleInventoryScanDTO**](AnsibleInventoryScanDTO.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/xml, text/plain, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

