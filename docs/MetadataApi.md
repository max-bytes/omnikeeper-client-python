# okclient.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_get_metadata**](MetadataApi.md#metadata_get_metadata) | **GET** /api/odata/{context}/$metadata | 
[**metadata_get_service_document**](MetadataApi.md#metadata_get_service_document) | **GET** /api/odata/{context} | 

# **metadata_get_metadata**
> IEdmModel metadata_get_metadata(context)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import metadata_api
from okclient.model.i_edm_model import IEdmModel
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
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'context': "context_example",
    }
    try:
        api_response = api_instance.metadata_get_metadata(
            path_params=path_params,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling MetadataApi->metadata_get_metadata: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
context | ContextSchema | | 

#### ContextSchema

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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IEdmModel**](IEdmModel.md) |  | 



[**IEdmModel**](IEdmModel.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get_service_document**
> ODataServiceDocument metadata_get_service_document(context)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import metadata_api
from okclient.model.o_data_service_document import ODataServiceDocument
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
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'context': "context_example",
    }
    try:
        api_response = api_instance.metadata_get_service_document(
            path_params=path_params,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling MetadataApi->metadata_get_service_document: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
context | ContextSchema | | 

#### ContextSchema

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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ODataServiceDocument**](ODataServiceDocument.md) |  | 



[**ODataServiceDocument**](ODataServiceDocument.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

