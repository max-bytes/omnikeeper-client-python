# okclient.ImportExportLayerApi

All URIs are relative to *https://localhost:44378*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_export_layer_export_layer**](ImportExportLayerApi.md#import_export_layer_export_layer) | **GET** /api/v{version}/ImportExportLayer/exportLayer | 
[**import_export_layer_import_layer**](ImportExportLayerApi.md#import_export_layer_import_layer) | **POST** /api/v{version}/ImportExportLayer/importLayer | 


# **import_export_layer_export_layer**
> import_export_layer_export_layer(layer_id, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import import_export_layer_api
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
    api_instance = import_export_layer_api.ImportExportLayerApi(api_client)
    layer_id = "layerID_example" # str | 
    version = "version_example" # str | 
    ciids = [
        "ciids_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.import_export_layer_export_layer(layer_id, version)
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_export_layer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.import_export_layer_export_layer(layer_id, version, ciids=ciids)
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_export_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_id** | **str**|  |
 **version** | **str**|  |
 **ciids** | **[str]**|  | [optional]

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_export_layer_import_layer**
> import_export_layer_import_layer(version, files)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import import_export_layer_api
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
    api_instance = import_export_layer_api.ImportExportLayerApi(api_client)
    version = "version_example" # str | 
    files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] | 
    overwrite_layer_id = "overwriteLayerID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.import_export_layer_import_layer(version, files)
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_import_layer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.import_export_layer_import_layer(version, files, overwrite_layer_id=overwrite_layer_id)
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_import_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **files** | **[file_type]**|  |
 **overwrite_layer_id** | **str**|  | [optional]

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

