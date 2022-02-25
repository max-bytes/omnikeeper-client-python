# okclient.AttributeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_replace_attributes_in_layer**](AttributeApi.md#bulk_replace_attributes_in_layer) | **POST** /api/v{version}/Attribute/bulkReplaceAttributesInLayer | bulk replace all attributes in specified layer
[**find_merged_attributes_by_name**](AttributeApi.md#find_merged_attributes_by_name) | **GET** /api/v{version}/Attribute/findMergedAttributesByName | 
[**get_merged_attribute**](AttributeApi.md#get_merged_attribute) | **GET** /api/v{version}/Attribute/getMergedAttribute | 
[**get_merged_attributes**](AttributeApi.md#get_merged_attributes) | **GET** /api/v{version}/Attribute/getMergedAttributes | 
[**get_merged_attributes_with_name**](AttributeApi.md#get_merged_attributes_with_name) | **GET** /api/v{version}/Attribute/getMergedAttributesWithName | 


# **bulk_replace_attributes_in_layer**
> bulk_replace_attributes_in_layer(version, bulk_ci_attribute_layer_scope_dto)

bulk replace all attributes in specified layer

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_api
from okclient.model.bulk_ci_attribute_layer_scope_dto import BulkCIAttributeLayerScopeDTO
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
    api_instance = attribute_api.AttributeApi(api_client)
    version = "version_example" # str | 
    bulk_ci_attribute_layer_scope_dto = BulkCIAttributeLayerScopeDTO(
        name_prefix="name_prefix_example",
        layer_id="layer_id_example",
        fragments=[
            FragmentDTO(
                name="name_example",
                value=AttributeValueDTO(
                    type=AttributeValueType("Text"),
                    is_array=True,
                    values=[
                        "values_example",
                    ],
                ),
                ciid="ciid_example",
            ),
        ],
    ) # BulkCIAttributeLayerScopeDTO | 

    # example passing only required values which don't have defaults set
    try:
        # bulk replace all attributes in specified layer
        api_instance.bulk_replace_attributes_in_layer(version, bulk_ci_attribute_layer_scope_dto)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->bulk_replace_attributes_in_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **bulk_ci_attribute_layer_scope_dto** | [**BulkCIAttributeLayerScopeDTO**](BulkCIAttributeLayerScopeDTO.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_merged_attributes_by_name**
> [CIAttributeDTO] find_merged_attributes_by_name(regex, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_api
from okclient.model.ci_attribute_dto import CIAttributeDTO
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
    api_instance = attribute_api.AttributeApi(api_client)
    regex = "regex_example" # str | 
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    ciids = [
        "ciids_example",
    ] # [str] |  (optional)
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.find_merged_attributes_by_name(regex, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->find_merged_attributes_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.find_merged_attributes_by_name(regex, layer_ids, version, ciids=ciids, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->find_merged_attributes_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regex** | **str**|  |
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **ciids** | **[str]**|  | [optional]
 **at_time** | **datetime**|  | [optional]

### Return type

[**[CIAttributeDTO]**](CIAttributeDTO.md)

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

# **get_merged_attribute**
> CIAttributeDTO get_merged_attribute(ciid, name, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_api
from okclient.model.ci_attribute_dto import CIAttributeDTO
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
    api_instance = attribute_api.AttributeApi(api_client)
    ciid = "ciid_example" # str | 
    name = "name_example" # str | 
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_merged_attribute(ciid, name, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attribute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_merged_attribute(ciid, name, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ciid** | **str**|  |
 **name** | **str**|  |
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **at_time** | **datetime**|  | [optional]

### Return type

[**CIAttributeDTO**](CIAttributeDTO.md)

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

# **get_merged_attributes**
> [CIAttributeDTO] get_merged_attributes(ciids, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_api
from okclient.model.ci_attribute_dto import CIAttributeDTO
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
    api_instance = attribute_api.AttributeApi(api_client)
    ciids = [
        "ciids_example",
    ] # [str] | 
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_merged_attributes(ciids, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attributes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_merged_attributes(ciids, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ciids** | **[str]**|  |
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **at_time** | **datetime**|  | [optional]

### Return type

[**[CIAttributeDTO]**](CIAttributeDTO.md)

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

# **get_merged_attributes_with_name**
> [CIAttributeDTO] get_merged_attributes_with_name(name, layer_ids, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import attribute_api
from okclient.model.ci_attribute_dto import CIAttributeDTO
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
    api_instance = attribute_api.AttributeApi(api_client)
    name = "name_example" # str | 
    layer_ids = [
        "layerIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # 
        api_response = api_instance.get_merged_attributes_with_name(name, layer_ids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attributes_with_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # 
        api_response = api_instance.get_merged_attributes_with_name(name, layer_ids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling AttributeApi->get_merged_attributes_with_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **layer_ids** | **[str]**|  |
 **version** | **str**|  |
 **at_time** | **datetime**|  | [optional]

### Return type

[**[CIAttributeDTO]**](CIAttributeDTO.md)

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

