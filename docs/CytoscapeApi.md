# okclient.CytoscapeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cytoscape_trait_centric**](CytoscapeApi.md#cytoscape_trait_centric) | **GET** /api/v{version}/Cytoscape/traitCentric | 

# **cytoscape_trait_centric**
> cytoscape_trait_centric(layer_idsversion)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import okclient
from okclient.api import cytoscape_api
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
    api_instance = cytoscape_api.CytoscapeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'layerIDs': [
        "layerIDs_example"
    ],
    }
    try:
        api_response = api_instance.cytoscape_trait_centric(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling CytoscapeApi->cytoscape_trait_centric: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version': "version_example",
    }
    query_params = {
        'layerIDs': [
        "layerIDs_example"
    ],
        'traitIDs': [
        "traitIDs_example"
    ],
        'traitIDsRegex': "traitIDsRegex_example",
    }
    try:
        api_response = api_instance.cytoscape_trait_centric(
            path_params=path_params,
            query_params=query_params,
        )
    except okclient.ApiException as e:
        print("Exception when calling CytoscapeApi->cytoscape_trait_centric: %s\n" % e)
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
layerIDs | LayerIDsSchema | | 
traitIDs | TraitIDsSchema | | optional
traitIDsRegex | TraitIDsRegexSchema | | optional


#### LayerIDsSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

#### TraitIDsSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

#### TraitIDsRegexSchema

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

