# okclient.ImportExportLayerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_export_layer_export_layer**](ImportExportLayerApi.md#import_export_layer_export_layer) | **GET** /api/v{version}/ImportExportLayer/exportLayer | 
[**import_export_layer_import_layer**](ImportExportLayerApi.md#import_export_layer_import_layer) | **POST** /api/v{version}/ImportExportLayer/importLayer | 

# **import_export_layer_export_layer**
> import_export_layer_export_layer(layer_idversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import import_export_layer_api
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
    api_instance = import_export_layer_api.ImportExportLayerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'layerID': "layerID_example",
    }
    try:
        api_response = api_instance.import_export_layer_export_layer(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_export_layer: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'layerID': "layerID_example",
        'ciids': [
        "ciids_example"
    ],
    }
    try:
        api_response = api_instance.import_export_layer_export_layer(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_export_layer: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
layerID | LayerIDSchema | | 
ciids | CiidsSchema | | optional


#### LayerIDSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### CiidsSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 

#### VersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_export_layer_import_layer**
> import_export_layer_import_layer(version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import import_export_layer_api
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
    api_instance = import_export_layer_api.ImportExportLayerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.import_export_layer_import_layer(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_import_layer: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'overwriteLayerID': "overwriteLayerID_example",
    }
    body = dict(
        files=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        api_response = api_instance.import_export_layer_import_layer(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling ImportExportLayerApi->import_export_layer_import_layer: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyMultipartFormData

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **[file_type]** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
overwriteLayerID | OverwriteLayerIDSchema | | optional


#### OverwriteLayerIDSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 

#### VersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Success

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

