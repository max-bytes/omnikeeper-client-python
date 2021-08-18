# okclient.LayerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_layers**](LayerApi.md#get_all_layers) | **GET** /api/v{version}/Layer/getAllLayers | list of all layers
[**get_layer_by_name**](LayerApi.md#get_layer_by_name) | **GET** /api/v{version}/Layer/getLayerByName | get a layer by name
[**get_layers_by_name**](LayerApi.md#get_layers_by_name) | **GET** /api/v{version}/Layer/getLayersByName | get layers by name


# **get_all_layers**
> [LayerDTO] get_all_layers(version)

list of all layers

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import layer_api
from okclient.model.layer_dto import LayerDTO
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
    api_instance = layer_api.LayerApi(api_client)
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # list of all layers
        api_response = api_instance.get_all_layers(version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling LayerApi->get_all_layers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

[**[LayerDTO]**](LayerDTO.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer_by_name**
> LayerDTO get_layer_by_name(layer_name, version)

get a layer by name

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import layer_api
from okclient.model.layer_dto import LayerDTO
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
    api_instance = layer_api.LayerApi(api_client)
    layer_name = "layerName_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # get a layer by name
        api_response = api_instance.get_layer_by_name(layer_name, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling LayerApi->get_layer_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**|  |
 **version** | **str**|  |

### Return type

[**LayerDTO**](LayerDTO.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layers_by_name**
> [LayerDTO] get_layers_by_name(layer_names, version)

get layers by name

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import layer_api
from okclient.model.layer_dto import LayerDTO
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
    api_instance = layer_api.LayerApi(api_client)
    layer_names = [
        "layerNames_example",
    ] # [str] | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # get layers by name
        api_response = api_instance.get_layers_by_name(layer_names, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling LayerApi->get_layers_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_names** | **[str]**|  |
 **version** | **str**|  |

### Return type

[**[LayerDTO]**](LayerDTO.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

