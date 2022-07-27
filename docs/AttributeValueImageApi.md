# okclient.AttributeValueImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_value_image_get**](AttributeValueImageApi.md#attribute_value_image_get) | **GET** /api/v{version}/AttributeValueImage | 
[**attribute_value_image_post**](AttributeValueImageApi.md#attribute_value_image_post) | **POST** /api/v{version}/AttributeValueImage | 

# **attribute_value_image_get**
> attribute_value_image_get(ciidattribute_namelayer_idsversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
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

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'ciid': "ciid_example",
        'attributeName': "attributeName_example",
        'layerIDs': [
        "layerIDs_example"
    ],
    }
    try:
        api_response = api_instance.attribute_value_image_get(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->attribute_value_image_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'ciid': "ciid_example",
        'attributeName': "attributeName_example",
        'layerIDs': [
        "layerIDs_example"
    ],
        'index': 0,
        'atTime': "1970-01-01T00:00:00.00Z",
    }
    try:
        api_response = api_instance.attribute_value_image_get(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->attribute_value_image_get: %s\n" % e)
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
ciid | CiidSchema | | 
attributeName | AttributeNameSchema | | 
layerIDs | LayerIDsSchema | | 
index | IndexSchema | | optional
atTime | AtTimeSchema | | optional


#### CiidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttributeNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LayerIDsSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

#### IndexSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 0

#### AtTimeSchema

Type | Description | Notes
------------- | ------------- | -------------
**datetime** |  | 

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

# **attribute_value_image_post**
> attribute_value_image_post(ciidattribute_namelayer_idversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
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

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'ciid': "ciid_example",
        'attributeName': "attributeName_example",
        'layerID': "layerID_example",
    }
    try:
        api_response = api_instance.attribute_value_image_post(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->attribute_value_image_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'ciid': "ciid_example",
        'attributeName': "attributeName_example",
        'layerID': "layerID_example",
        'forceArray': False,
    }
    body = dict(
        files=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        api_response = api_instance.attribute_value_image_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling AttributeValueImageApi->attribute_value_image_post: %s\n" % e)
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
ciid | CiidSchema | | 
attributeName | AttributeNameSchema | | 
layerID | LayerIDSchema | | 
forceArray | ForceArraySchema | | optional


#### CiidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttributeNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LayerIDSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ForceArraySchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

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

