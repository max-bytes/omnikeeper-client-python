# okclient.OKPluginGenericJSONIngestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_context**](OKPluginGenericJSONIngestApi.md#add_new_context) | **POST** /api/v{version}/ingest/genericJSON/manage/context | 
[**get_all_contexts**](OKPluginGenericJSONIngestApi.md#get_all_contexts) | **GET** /api/v{version}/ingest/genericJSON/manage/context | 
[**get_context_by_name**](OKPluginGenericJSONIngestApi.md#get_context_by_name) | **GET** /api/v{version}/ingest/genericJSON/manage/context/{name} | 
[**ingest**](OKPluginGenericJSONIngestApi.md#ingest) | **POST** /api/v{version}/ingest/genericJSON/files | 
[**remove_context**](OKPluginGenericJSONIngestApi.md#remove_context) | **DELETE** /api/v{version}/ingest/genericJSON/manage/context/{name} | 


# **add_new_context**
> add_new_context(version, context)



### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import time
import okclient
from okclient.api import ok_plugin_generic_json_ingest_api
from okclient.model.context import Context
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
    context = Context(
        name="name_example",
        extract_config={},
        transform_config={},
        load_config=ILoadConfig(
        ),
    ) # Context | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_new_context(version, context)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->add_new_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **context** | [**Context**](Context.md)|  |

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

# **get_all_contexts**
> get_all_contexts(version)



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
        api_instance.get_all_contexts(version)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->get_all_contexts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context_by_name**
> get_context_by_name(name, version)



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
    name = "name_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_context_by_name(name, version)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->get_context_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **version** | **str**|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest**
> ingest(context, version, files)



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
    files = open('/path/to/file', 'rb') # [file_type] | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest(context, version, files)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->ingest: %s\n" % e)
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

# **remove_context**
> remove_context(name, version)



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
    name = "name_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_context(name, version)
    except okclient.ApiException as e:
        print("Exception when calling OKPluginGenericJSONIngestApi->remove_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **version** | **str**|  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

