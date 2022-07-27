# okclient.GraphvizDotApi

All URIs are relative to *https://localhost:44378*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graphviz_dot_layer_centric**](GraphvizDotApi.md#graphviz_dot_layer_centric) | **GET** /api/v{version}/GraphvizDot/layerCentric | 
[**graphviz_dot_trait_centric**](GraphvizDotApi.md#graphviz_dot_trait_centric) | **GET** /api/v{version}/GraphvizDot/traitCentric | 


# **graphviz_dot_layer_centric**
> graphviz_dot_layer_centric(layer_ids, _from, to, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import graphviz_dot_api
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
    api_instance = graphviz_dot_api.GraphvizDotApi(api_client)
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.graphviz_dot_layer_centric(layer_ids, _from, to, version)
    except okclient.ApiException as e:
        print("Exception when calling GraphvizDotApi->graphviz_dot_layer_centric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[str]**|  |
 **_from** | **datetime**|  |
 **to** | **datetime**|  |
 **version** | **str**|  |

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

# **graphviz_dot_trait_centric**
> graphviz_dot_trait_centric(layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import graphviz_dot_api
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
    api_instance = graphviz_dot_api.GraphvizDotApi(api_client)
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    trait_ids = [
        "traitIDs_example",
    ] # [str] |  (optional)
    trait_ids_regex = "traitIDsRegex_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.graphviz_dot_trait_centric(layer_ids, version)
    except okclient.ApiException as e:
        print("Exception when calling GraphvizDotApi->graphviz_dot_trait_centric: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.graphviz_dot_trait_centric(layer_ids, version, trait_ids=trait_ids, trait_ids_regex=trait_ids_regex)
    except okclient.ApiException as e:
        print("Exception when calling GraphvizDotApi->graphviz_dot_trait_centric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **trait_ids** | **[str]**|  | [optional]
 **trait_ids_regex** | **str**|  | [optional]

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

