# okclient.GridViewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grid_view_add_context**](GridViewApi.md#grid_view_add_context) | **POST** /api/v{version}/GridView/context | Adds new context
[**grid_view_change_data**](GridViewApi.md#grid_view_change_data) | **POST** /api/v{version}/GridView/contexts/{context}/change | Saves grid view row changes and returns change results
[**grid_view_delete_context**](GridViewApi.md#grid_view_delete_context) | **DELETE** /api/v{version}/GridView/context/{name} | Deletes specific context
[**grid_view_edit_context**](GridViewApi.md#grid_view_edit_context) | **PUT** /api/v{version}/GridView/context/{name} | Edits specific context
[**grid_view_get_data**](GridViewApi.md#grid_view_get_data) | **GET** /api/v{version}/GridView/contexts/{context}/data | Returns grid view data for specific context
[**grid_view_get_grid_view_context**](GridViewApi.md#grid_view_get_grid_view_context) | **GET** /api/v{version}/GridView/context/{name} | Returns a single context in full
[**grid_view_get_grid_view_contexts**](GridViewApi.md#grid_view_get_grid_view_contexts) | **GET** /api/v{version}/GridView/contexts | Returns a list of contexts for grid view.
[**grid_view_get_schema**](GridViewApi.md#grid_view_get_schema) | **GET** /api/v{version}/GridView/contexts/{context}/schema | Returns grid view schema for specific context

# **grid_view_add_context**
> grid_view_add_context(version)

Adds new context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
from okclient.model.add_context_request import AddContextRequest
from okclient.model.problem_details import ProblemDetails
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    try:
        # Adds new context
        api_response = api_instance.grid_view_add_context(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_add_context: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    body = AddContextRequest(
        id="id_example",
        speaking_name="speaking_name_example",
        description="description_example",
        configuration=GridViewConfiguration(
            show_ciid_column=True,
            write_layer="write_layer_example",
            read_layerset=[
                "read_layerset_example"
            ],
            columns=[
                GridViewColumn(
                    source_attribute_name="source_attribute_name_example",
                    source_attribute_path=[],
                    column_description="column_description_example",
                    value_type=AttributeValueType("Text"),
                    write_layer="write_layer_example",
                )
            ],
            trait="trait_example",
        ),
    )
    try:
        # Adds new context
        api_response = api_instance.grid_view_add_context(
            path_params=path_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_add_context: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddContextRequest**](AddContextRequest.md) |  | 


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
201 | ApiResponseFor201 | Returns the newly created context
400 | ApiResponseFor400 | If creating context fails

#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatafull, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatanone, SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationOctetStream, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_change_data**
> grid_view_change_data(contextversion)

Saves grid view row changes and returns change results

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
from okclient.model.problem_details import ProblemDetails
from okclient.model.change_data_request import ChangeDataRequest
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'context': "context_example",
        'version': "version_example",
    }
    try:
        # Saves grid view row changes and returns change results
        api_response = api_instance.grid_view_change_data(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_change_data: %s\n" % e)

    # example passing only optional values
    path_params = {
        'context': "context_example",
        'version': "version_example",
    }
    body = ChangeDataRequest(
        sparse_rows=[
            SparseRow(
                ciid="ciid_example",
                cells=[
                    ChangeDataCell(
                        id="id_example",
                        value=AttributeValueDTO(
                            type=AttributeValueType("Text"),
                            is_array=True,
                            values=[
                                "values_example"
                            ],
                        ),
                        changeable=True,
                    )
                ],
            )
        ],
    )
    try:
        # Saves grid view row changes and returns change results
        api_response = api_instance.grid_view_change_data(
            path_params=path_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_change_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangeDataRequest**](ChangeDataRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
context | ContextSchema | | 
version | VersionSchema | | 

#### ContextSchema

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
200 | ApiResponseFor200 | If request is successful
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | If saving changes fails

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatafull, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatanone, SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationOctetStream, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_delete_context**
> grid_view_delete_context(nameversion)

Deletes specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
from okclient.model.problem_details import ProblemDetails
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'version': "version_example",
    }
    try:
        # Deletes specific context
        api_response = api_instance.grid_view_delete_context(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_delete_context: %s\n" % e)
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
name | NameSchema | | 
version | VersionSchema | | 

#### NameSchema

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
200 | ApiResponseFor200 | If request is successful
400 | ApiResponseFor400 | If editing the context fails

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatafull, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatanone, SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationOctetStream, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_edit_context**
> grid_view_edit_context(nameversion)

Edits specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
from okclient.model.edit_context_request import EditContextRequest
from okclient.model.problem_details import ProblemDetails
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'version': "version_example",
    }
    try:
        # Edits specific context
        api_response = api_instance.grid_view_edit_context(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_edit_context: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'version': "version_example",
    }
    body = EditContextRequest(
        speaking_name="speaking_name_example",
        description="description_example",
        configuration=GridViewConfiguration(
            show_ciid_column=True,
            write_layer="write_layer_example",
            read_layerset=[
                "read_layerset_example"
            ],
            columns=[
                GridViewColumn(
                    source_attribute_name="source_attribute_name_example",
                    source_attribute_path=[],
                    column_description="column_description_example",
                    value_type=AttributeValueType("Text"),
                    write_layer="write_layer_example",
                )
            ],
            trait="trait_example",
        ),
    )
    try:
        # Edits specific context
        api_response = api_instance.grid_view_edit_context(
            path_params=path_params,
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_edit_context: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;minimal;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;minimal', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;full;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;full', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;true', 'application/json;odata.metadata&#x3D;none;odata.streaming&#x3D;false', 'application/json;odata.metadata&#x3D;none', 'application/json;odata.streaming&#x3D;true', 'application/json;odata.streaming&#x3D;false', 'text/plain', 'application/octet-stream', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditContextRequest**](EditContextRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
version | VersionSchema | | 

#### NameSchema

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
200 | ApiResponseFor200 | If request is successful
400 | ApiResponseFor400 | If editing the context fails

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatafull, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaFor400ResponseBodyApplicationJsonodataMetadatanone, SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue, SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse, SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationOctetStream, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_get_data**
> grid_view_get_data(contextversion)

Returns grid view data for specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'context': "context_example",
        'version': "version_example",
    }
    try:
        # Returns grid view data for specific context
        api_response = api_instance.grid_view_get_data(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_get_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
context | ContextSchema | | 
version | VersionSchema | | 

#### ContextSchema

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
200 | ApiResponseFor200 | If request is successful
400 | ApiResponseFor400 | If trait is not found

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_get_grid_view_context**
> grid_view_get_grid_view_context(nameversion)

Returns a single context in full

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'version': "version_example",
    }
    try:
        # Returns a single context in full
        api_response = api_instance.grid_view_get_grid_view_context(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_get_grid_view_context: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
version | VersionSchema | | 

#### NameSchema

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
400 | ApiResponseFor400 | If the name was not found or any other error occurred

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_get_grid_view_contexts**
> grid_view_get_grid_view_contexts(version)

Returns a list of contexts for grid view.

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    try:
        # Returns a list of contexts for grid view.
        api_response = api_instance.grid_view_get_grid_view_contexts(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_get_grid_view_contexts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
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
body | Unset | body was not defined |
headers | Unset | headers were not defined |


void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grid_view_get_schema**
> grid_view_get_schema(contextversion)

Returns grid view schema for specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import grid_view_api
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
    api_instance = grid_view_api.GridViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'context': "context_example",
        'version': "version_example",
    }
    try:
        # Returns grid view schema for specific context
        api_response = api_instance.grid_view_get_schema(
            path_params=path_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->grid_view_get_schema: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
context | ContextSchema | | 
version | VersionSchema | | 

#### ContextSchema

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
200 | ApiResponseFor200 | 

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

