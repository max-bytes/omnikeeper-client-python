# okclient.AnsibleInventoryScanIngestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_ansible_inventory_scan**](AnsibleInventoryScanIngestApi.md#ingest_ansible_inventory_scan) | **POST** /api/v{version}/Ingest/AnsibleInventoryScan | 


# **ingest_ansible_inventory_scan**
> ingest_ansible_inventory_scan(write_layer_id, search_layer_ids, version, ansible_inventory_scan_dto)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import ansible_inventory_scan_ingest_api
from okclient.model.ansible_inventory_scan_dto import AnsibleInventoryScanDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = okclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = okclient.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth2
configuration = okclient.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with okclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible_inventory_scan_ingest_api.AnsibleInventoryScanIngestApi(api_client)
    write_layer_id = 1 # int | 
    search_layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    ansible_inventory_scan_dto = AnsibleInventoryScanDTO(
        setup_facts={
            "key": {},
        },
        yum_installed={
            "key": {},
        },
        yum_repos={
            "key": {},
        },
        yum_updates={
            "key": {},
        },
    ) # AnsibleInventoryScanDTO | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest_ansible_inventory_scan(write_layer_id, search_layer_ids, version, ansible_inventory_scan_dto)
    except okclient.ApiException as e:
        print("Exception when calling AnsibleInventoryScanIngestApi->ingest_ansible_inventory_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **write_layer_id** | **int**|  |
 **search_layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **ansible_inventory_scan_dto** | [**AnsibleInventoryScanDTO**](AnsibleInventoryScanDTO.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

