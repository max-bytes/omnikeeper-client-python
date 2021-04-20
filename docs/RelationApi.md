# okclient.RelationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_merged_relations**](RelationApi.md#get_all_merged_relations) | **GET** /api/v{version}/Relation/getAllMergedRelations | 
[**get_merged_relation**](RelationApi.md#get_merged_relation) | **GET** /api/v{version}/Relation/getMergedRelation | 
[**get_merged_relations_from_or_to_ci**](RelationApi.md#get_merged_relations_from_or_to_ci) | **GET** /api/v{version}/Relation/getMergedRelationsFromOrToCI | 
[**get_merged_relations_outgoing_from_ci**](RelationApi.md#get_merged_relations_outgoing_from_ci) | **GET** /api/v{version}/Relation/getMergedRelationsOutgoingFromCI | 
[**get_merged_relations_with_predicate**](RelationApi.md#get_merged_relations_with_predicate) | **GET** /api/v{version}/Relation/getMergedRelationsWithPredicate | 


# **get_all_merged_relations**
> [RelationDTO] get_all_merged_relations(layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import relation_api
from okclient.model.relation_dto import RelationDTO
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
    api_instance = relation_api.RelationApi(api_client)
    layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_merged_relations(layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_all_merged_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_merged_relations(layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_all_merged_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **at_time** | **datetime, none_type**|  | [optional]

### Return type

[**[RelationDTO]**](RelationDTO.md)

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

# **get_merged_relation**
> RelationDTO get_merged_relation(from_ciid, to_ciid, predicate_id, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import relation_api
from okclient.model.relation_dto import RelationDTO
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
    api_instance = relation_api.RelationApi(api_client)
    from_ciid = "fromCIID_example" # str | 
    to_ciid = "toCIID_example" # str | 
    predicate_id = "predicateID_example" # str | 
    layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_merged_relation(from_ciid, to_ciid, predicate_id, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_merged_relation(from_ciid, to_ciid, predicate_id, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_ciid** | **str**|  |
 **to_ciid** | **str**|  |
 **predicate_id** | **str**|  |
 **layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **at_time** | **datetime, none_type**|  | [optional]

### Return type

[**RelationDTO**](RelationDTO.md)

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

# **get_merged_relations_from_or_to_ci**
> [RelationDTO] get_merged_relations_from_or_to_ci(ciid, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import relation_api
from okclient.model.relation_dto import RelationDTO
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
    api_instance = relation_api.RelationApi(api_client)
    ciid = "ciid_example" # str | 
    layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_merged_relations_from_or_to_ci(ciid, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_from_or_to_ci: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_merged_relations_from_or_to_ci(ciid, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_from_or_to_ci: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ciid** | **str**|  |
 **layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **at_time** | **datetime, none_type**|  | [optional]

### Return type

[**[RelationDTO]**](RelationDTO.md)

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

# **get_merged_relations_outgoing_from_ci**
> [RelationDTO] get_merged_relations_outgoing_from_ci(from_ciid, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import relation_api
from okclient.model.relation_dto import RelationDTO
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
    api_instance = relation_api.RelationApi(api_client)
    from_ciid = "fromCIID_example" # str | 
    layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_merged_relations_outgoing_from_ci(from_ciid, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_outgoing_from_ci: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_merged_relations_outgoing_from_ci(from_ciid, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_outgoing_from_ci: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_ciid** | **str**|  |
 **layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **at_time** | **datetime, none_type**|  | [optional]

### Return type

[**[RelationDTO]**](RelationDTO.md)

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

# **get_merged_relations_with_predicate**
> [RelationDTO] get_merged_relations_with_predicate(predicate_id, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import relation_api
from okclient.model.relation_dto import RelationDTO
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
    api_instance = relation_api.RelationApi(api_client)
    predicate_id = "predicateID_example" # str | 
    layer_ids = [
        1,
    ] # [int] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_merged_relations_with_predicate(predicate_id, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_with_predicate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_merged_relations_with_predicate(predicate_id, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling RelationApi->get_merged_relations_with_predicate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predicate_id** | **str**|  |
 **layer_ids** | **[int]**|  |
 **version** | **str**|  |
 **at_time** | **datetime, none_type**|  | [optional]

### Return type

[**[RelationDTO]**](RelationDTO.md)

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

