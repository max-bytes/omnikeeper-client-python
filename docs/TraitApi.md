# okclient.TraitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_effective_traits_for_trait_name**](TraitApi.md#get_effective_traits_for_trait_name) | **GET** /api/v{version}/Trait/getEffectiveTraitsForTraitName | 


# **get_effective_traits_for_trait_name**
> {str: (EffectiveTraitDTO,)} get_effective_traits_for_trait_name(layer_ids, trait_name, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import trait_api
from okclient.model.effective_trait_dto import EffectiveTraitDTO
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
    api_instance = trait_api.TraitApi(api_client)
    layer_ids = [
        1,
    ] # [int] | 
    trait_name = "traitName_example" # str | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_effective_traits_for_trait_name(layer_ids, trait_name, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling TraitApi->get_effective_traits_for_trait_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_effective_traits_for_trait_name(layer_ids, trait_name, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling TraitApi->get_effective_traits_for_trait_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[int]**|  |
 **trait_name** | **str**|  |
 **version** | **str**|  |
 **at_time** | **datetime**|  | [optional]

### Return type

[**{str: (EffectiveTraitDTO,)}**](EffectiveTraitDTO.md)

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

