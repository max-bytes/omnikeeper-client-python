# okclient.AttributeValueImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AttributeValueImageApi.md#get) | **GET** /api/v{version}/AttributeValueImage | 
[**post**](AttributeValueImageApi.md#post) | **POST** /api/v{version}/AttributeValueImage | 


# **get**
> get(ciid, attribute_name, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_value_image_api
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
    api_instance = attribute_value_image_api.AttributeValueImageApi(api_client)
    ciid = "ciid_example" # str | 
    attribute_name = "attributeName_example" # str | 
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    index = 0 # int |  (optional) if omitted the server will use the default value of 0
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get(ciid, attribute_name, layer_ids, version)
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get(ciid, attribute_name, layer_ids, version, index=index, at_time=at_time)
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ciid** | **str**|  |
 **attribute_name** | **str**|  |
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **index** | **int**|  | [optional] if omitted the server will use the default value of 0
 **at_time** | **datetime**|  | [optional]

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

# **post**
> post(ciid, attribute_name, layer_id, version, files)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_value_image_api
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
    api_instance = attribute_value_image_api.AttributeValueImageApi(api_client)
    ciid = "ciid_example" # str | 
    attribute_name = "attributeName_example" # str | 
    layer_id = "layerID_example" # str | 
    version = "version_example" # str | 
    files = open('/path/to/file', 'rb') # [file_type] | 
    force_array = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_instance.post(ciid, attribute_name, layer_id, version, files)
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post(ciid, attribute_name, layer_id, version, files, force_array=force_array)
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ciid** | **str**|  |
 **attribute_name** | **str**|  |
 **layer_id** | **str**|  |
 **version** | **str**|  |
 **files** | **[file_type]**|  |
 **force_array** | **bool**|  | [optional] if omitted the server will use the default value of False

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

