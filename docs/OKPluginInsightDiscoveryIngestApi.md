# okclient.OKPluginInsightDiscoveryIngestApi

All URIs are relative to *https://localhost:44378*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_file_ingest**](OKPluginInsightDiscoveryIngestApi.md#ingest_file_ingest) | **POST** /api/v{version}/ingest/insight-discovery/file | 


# **ingest_file_ingest**
> ingest_file_ingest(context, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import ok_plugin_insight_discovery_ingest_api
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
    api_instance = ok_plugin_insight_discovery_ingest_api.OKPluginInsightDiscoveryIngestApi(api_client)
    context = "context_example" # str | 
    version = "version_example" # str | 
    content_type = "content_type_example" # str |  (optional)
    content_disposition = "content_disposition_example" # str |  (optional)
    length = 1 # int |  (optional)
    name = "name_example" # str |  (optional)
    file_name = "file_name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest_file_ingest(context, version)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginInsightDiscoveryIngestApi->ingest_file_ingest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.ingest_file_ingest(context, version, content_type=content_type, content_disposition=content_disposition, length=length, name=name, file_name=file_name)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginInsightDiscoveryIngestApi->ingest_file_ingest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  |
 **version** | **str**|  |
 **content_type** | **str**|  | [optional]
 **content_disposition** | **str**|  | [optional]
 **length** | **int**|  | [optional]
 **name** | **str**|  | [optional]
 **file_name** | **str**|  | [optional]

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

