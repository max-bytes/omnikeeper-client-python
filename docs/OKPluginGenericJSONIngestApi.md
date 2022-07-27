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
> [dict] manage_context_get_all_contexts(version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_context_get_all_contexts(version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_get_all_contexts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

**[dict]**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, text/plain, application/octet-stream, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_get_context**
> dict manage_context_get_context(id, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    id = "id_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_context_get_context(id, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_get_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **version** | **str**|  |

### Return type

**dict**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, text/plain, application/octet-stream, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_remove_context**
> bool manage_context_remove_context(id, version)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    id = "id_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_context_remove_context(id, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_remove_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **version** | **str**|  |

### Return type

**bool**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, text/plain, application/octet-stream, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_context_upsert_context**
> dict manage_context_upsert_context(version, body)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    version = "version_example" # str | 
    body = {} # dict | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.manage_context_upsert_context(version, body)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->manage_context_upsert_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **body** | **dict**|  |

### Return type

**dict**

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/xml, text/plain, text/json, application/*+json
 - **Accept**: application/json, application/xml, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, text/plain, application/octet-stream, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passive_data_ingest**
> passive_data_ingest(read_layer_ids, write_layer_id, version, generic_inbound_data)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    read_layer_ids = [
        "readLayerIDs_example",
    ] # [str] | 
    write_layer_id = "writeLayerID_example" # str | 
    version = "version_example" # str | 
    generic_inbound_data = GenericInboundData(
        cis=[
            GenericInboundCI(
                temp_id="temp_id_example",
                id_method=GenericInboundCIIdMethod(None),
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
                                "values_example",
                            ],
                        ),
                    ),
                ],
            ),
        ],
        relations=[
            GenericInboundRelation(
                _from="_from_example",
                predicate="predicate_example",
                to="to_example",
            ),
        ],
    ) # GenericInboundData | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.passive_data_ingest(read_layer_ids, write_layer_id, version, generic_inbound_data)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->passive_data_ingest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_layer_ids** | **[str]**|  |
 **write_layer_id** | **str**|  |
 **version** | **str**|  |
 **generic_inbound_data** | [**GenericInboundData**](GenericInboundData.md)|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/xml, text/plain, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passive_files_ingest**
> passive_files_ingest(context, version, files)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
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
    context = "context_example" # str | 
    version = "version_example" # str | 
    files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.passive_files_ingest(context, version, files)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->passive_files_ingest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  |
 **version** | **str**|  |
 **files** | **[file_type]**|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

