# okclient.OKPluginGenericJSONIngestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manage_context_get_all_contexts**](OKPluginGenericJSONIngestApi.md#manage_context_get_all_contexts) | **GET** /api/v{version}/ingest/genericJSON/manage/context | 
[**manage_context_get_context**](OKPluginGenericJSONIngestApi.md#manage_context_get_context) | **GET** /api/v{version}/ingest/genericJSON/manage/context/{id} | 
[**manage_context_remove_context**](OKPluginGenericJSONIngestApi.md#manage_context_remove_context) | **DELETE** /api/v{version}/ingest/genericJSON/manage/context/{id} | 
[**manage_context_upsert_context**](OKPluginGenericJSONIngestApi.md#manage_context_upsert_context) | **POST** /api/v{version}/ingest/genericJSON/manage/context | 
[**passive_data_ingest**](OKPluginGenericJSONIngestApi.md#passive_data_ingest) | **POST** /api/v{version}/ingest/genericJSON/data | 
[**passive_files_ingest**](OKPluginGenericJSONIngestApi.md#passive_files_ingest) | **POST** /api/v{version}/ingest/genericJSON/files | 

# **manage_context_get_all_contexts**
> [object] manage_context_get_all_contexts(version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    try:
        api_response = api_instance.manage_context_get_all_contexts(
            path_params=path_params,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_get_all_contexts: %s\n" % e)
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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationXml

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyApplicationOctetStream

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 

#### SchemaFor200ResponseBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**[object]** |  | 


**[object]**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_get_context**
> {str: typing.Any} manage_context_get_context(idversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.manage_context_get_context(
            path_params=path_params,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_get_context: %s\n" % e)
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
id | IdSchema | | 
version | VersionSchema | | 

#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationXml

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationOctetStream

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 


**{str: typing.Any}**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_remove_context**
> bool manage_context_remove_context(idversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.manage_context_remove_context(
            path_params=path_params,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_remove_context: %s\n" % e)
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
id | IdSchema | | 
version | VersionSchema | | 

#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationXml

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyApplicationOctetStream

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### SchemaFor200ResponseBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 


**bool**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_upsert_context**
> {str: typing.Any} manage_context_upsert_context(versionbody)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    body = dict()
    try:
        api_response = api_instance.manage_context_upsert_context(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_upsert_context: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadataminimal

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatafull

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataMetadatanone

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJsonodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationXml

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaForRequestBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

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
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatafull, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor200ResponseBodyApplicationJsonodataMetadatanone, SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationOctetStream, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationXml

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadataminimal

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatafull

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataMetadatanone

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingtrue

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationJsonodataStreamingfalse

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyApplicationOctetStream

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 

#### SchemaFor200ResponseBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**{str: typing.Any}** |  | 


**{str: typing.Any}**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passive_data_ingest**
> passive_data_ingest(read_layer_idswrite_layer_idversiongeneric_inbound_data)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
from okclient.model.generic_inbound_data import GenericInboundData
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'readLayerIDs': [
        "readLayerIDs_example"
    ],
        'writeLayerID': "writeLayerID_example",
    }
    body = GenericInboundData(
        cis=[
            GenericInboundCI(
                temp_id="temp_id_example",
                id_method=None,
                same_temp_id_handling=SameTempIDHandling("DropAndWarn"),
                same_target_ci_handling=SameTargetCIHandling("Error"),
                no_found_target_ci_handling=NoFoundTargetCIHandling("CreateNew"),
                attributes=[
                    GenericInboundAttribute(
                        name="name_example",
                        value=AttributeValueDTO(
                            type=AttributeValueType("Text"),
                            is_array=True,
                            values=[
                                "values_example"
                            ],
                        ),
                    )
                ],
            )
        ],
        relations=[
            GenericInboundRelation(
                _from="_from_example",
                predicate="predicate_example",
                to="to_example",
            )
        ],
    )
    try:
        api_response = api_instance.passive_data_ingest(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->passive_data_ingest: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GenericInboundData**](GenericInboundData.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
readLayerIDs | ReadLayerIDsSchema | | 
writeLayerID | WriteLayerIDSchema | | 


#### ReadLayerIDsSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

#### WriteLayerIDSchema

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

# **passive_files_ingest**
> passive_files_ingest(contextversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
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
    api_instance = ok_plugin_generic_json_ingest_api.OKPluginGenericJSONIngestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'context': "context_example",
    }
    try:
        api_response = api_instance.passive_files_ingest(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->passive_files_ingest: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'context': "context_example",
    }
    body = dict(
        files=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        api_response = api_instance.passive_files_ingest(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->passive_files_ingest: %s\n" % e)
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
context | ContextSchema | | 


#### ContextSchema

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

