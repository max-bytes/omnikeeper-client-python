# okclient.ActiveDirectoryXMLIngestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_xml**](ActiveDirectoryXMLIngestApi.md#ingest_xml) | **POST** /api/v{version}/Ingest/AD-XML | 


# **ingest_xml**
> ingest_xml(version, write_layer_id, search_layer_ids, files)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import active_directory_xml_ingest_api
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
    api_instance = active_directory_xml_ingest_api.ActiveDirectoryXMLIngestApi(api_client)
    version = "version_example" # str | 
    write_layer_id = 1 # int | 
    search_layer_ids = 1 # [int] | 
    files = open('/path/to/file', 'rb') # [file_type] | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest_xml(version, write_layer_id, search_layer_ids, files)
    except okclient.ApiException as e:
        print("Exception when calling ActiveDirectoryXMLIngestApi->ingest_xml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **write_layer_id** | **int**|  |
 **search_layer_ids** | **[int]**|  |
 **files** | **[file_type]**|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

