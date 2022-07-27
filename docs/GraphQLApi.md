# okclient.GraphQLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_ql_debug**](GraphQLApi.md#graph_ql_debug) | **POST** /graphql-debug | 
[**graph_ql_get**](GraphQLApi.md#graph_ql_get) | **GET** /graphql | 
[**graph_ql_index**](GraphQLApi.md#graph_ql_index) | **POST** /graphql | 

# **graph_ql_debug**
> graph_ql_debug()



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import graph_ql_api
from okclient.model.graph_ql_query import GraphQLQuery
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
    api_instance = graph_ql_api.GraphQLApi(api_client)

    # example passing only optional values
    body = GraphQLQuery(
        operation_name="operation_name_example",
        query="query_example",
        variables=dict(
            "key": None,
        ),
    )
    try:
        api_response = api_instance.graph_ql_debug(
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling GraphQLApi->graph_ql_debug: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


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

# **graph_ql_get**
> graph_ql_get()



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import graph_ql_api
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
    api_instance = graph_ql_api.GraphQLApi(api_client)

    # example passing only optional values
    query_params = {
        'operationName': "operationName_example",
        'query': "query_example",
        'variables': dict(
        "key": None,
    ),
    }
    try:
        api_response = api_instance.graph_ql_get(
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling GraphQLApi->graph_ql_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
operationName | OperationNameSchema | | optional
query | QuerySchema | | optional
variables | VariablesSchema | | optional


#### OperationNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### QuerySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### VariablesSchema

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

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

# **graph_ql_index**
> graph_ql_index()



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import graph_ql_api
from okclient.model.graph_ql_query import GraphQLQuery
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
    api_instance = graph_ql_api.GraphQLApi(api_client)

    # example passing only optional values
    body = GraphQLQuery(
        operation_name="operation_name_example",
        query="query_example",
        variables=dict(
            "key": None,
        ),
    )
    try:
        api_response = api_instance.graph_ql_index(
            body=body,
        )
    except okclient.ApiException as e:
        print("Exception when calling GraphQLApi->graph_ql_index: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadataminimal, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatafull, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse, SchemaForRequestBodyApplicationJsonodataMetadatanone, SchemaForRequestBodyApplicationJsonodataStreamingtrue, SchemaForRequestBodyApplicationJsonodataStreamingfalse, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextPlain, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadataminimal
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatafull
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataMetadatanone
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingtrue
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJsonodataStreamingfalse
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphQLQuery**](GraphQLQuery.md) |  | 


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

