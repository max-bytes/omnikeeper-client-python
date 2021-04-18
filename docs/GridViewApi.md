# okclient.GridViewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_context**](GridViewApi.md#add_context) | **POST** /api/v{version}/GridView/context | Adds new context
[**change_data**](GridViewApi.md#change_data) | **POST** /api/v{version}/GridView/contexts/{context}/change | Saves grid view row changes and returns change results
[**delete_context**](GridViewApi.md#delete_context) | **DELETE** /api/v{version}/GridView/context/{name} | Deletes specific context
[**edit_context**](GridViewApi.md#edit_context) | **PUT** /api/v{version}/GridView/context/{name} | Edits specific context
[**get_context**](GridViewApi.md#get_context) | **GET** /api/v{version}/GridView/context/{name} | Returns a single context in full
[**get_contexts**](GridViewApi.md#get_contexts) | **GET** /api/v{version}/GridView/contexts | Returns a list of contexts for grid view.
[**get_data**](GridViewApi.md#get_data) | **GET** /api/v{version}/GridView/contexts/{context}/data | Returns grid view data for specific context
[**get_schema**](GridViewApi.md#get_schema) | **GET** /api/v{version}/GridView/contexts/{context}/schema | Returns grid view schema for specific context


# **add_context**
> add_context(version)

Adds new context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    version = "version_example" # str | 
    add_context_request = AddContextRequest(
        name="name_example",
        speaking_name="speaking_name_example",
        description="description_example",
        configuration=GridViewConfiguration(
            show_ciid_column=True,
            write_layer=1,
            read_layerset=[
                1,
            ],
            columns=[
                GridViewColumn(
                    source_attribute_name="source_attribute_name_example",
                    column_description="column_description_example",
                    value_type=AttributeValueType("Text"),
                    write_layer=1,
                ),
            ],
            trait="trait_example",
        ),
    ) # AddContextRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds new context
        api_instance.add_context(version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->add_context: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds new context
        api_instance.add_context(version, add_context_request=add_context_request)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->add_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |
 **add_context_request** | [**AddContextRequest**](AddContextRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created context |  -  |
**400** | If creating context fails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_data**
> change_data(context, version)

Saves grid view row changes and returns change results

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    context = "context_example" # str | 
    version = "version_example" # str | 
    change_data_request = ChangeDataRequest(
        sparse_rows=[
            SparseRow(
                ciid="ciid_example",
                cells=[
                    ChangeDataCell(
                        name="name_example",
                        value=AttributeValueDTO(
                            type=AttributeValueType("Text"),
                            is_array=True,
                            values=[
                                "values_example",
                            ],
                        ),
                        changeable=True,
                    ),
                ],
            ),
        ],
    ) # ChangeDataRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Saves grid view row changes and returns change results
        api_instance.change_data(context, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->change_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Saves grid view row changes and returns change results
        api_instance.change_data(context, version, change_data_request=change_data_request)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->change_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  |
 **version** | **str**|  |
 **change_data_request** | [**ChangeDataRequest**](ChangeDataRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If request is successful |  -  |
**400** | Bad Request |  -  |
**404** | If saving changes fails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_context**
> delete_context(name, version)

Deletes specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    name = "name_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes specific context
        api_instance.delete_context(name, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->delete_context: %s\n" % e)
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
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If request is successful |  -  |
**400** | If editing the context fails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_context**
> edit_context(name, version)

Edits specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    name = "name_example" # str | 
    version = "version_example" # str | 
    edit_context_request = EditContextRequest(
        speaking_name="speaking_name_example",
        description="description_example",
        configuration=GridViewConfiguration(
            show_ciid_column=True,
            write_layer=1,
            read_layerset=[
                1,
            ],
            columns=[
                GridViewColumn(
                    source_attribute_name="source_attribute_name_example",
                    column_description="column_description_example",
                    value_type=AttributeValueType("Text"),
                    write_layer=1,
                ),
            ],
            trait="trait_example",
        ),
    ) # EditContextRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edits specific context
        api_instance.edit_context(name, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->edit_context: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edits specific context
        api_instance.edit_context(name, version, edit_context_request=edit_context_request)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->edit_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **version** | **str**|  |
 **edit_context_request** | [**EditContextRequest**](EditContextRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/odata, text/plain, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If request is successful |  -  |
**400** | If editing the context fails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context**
> get_context(name, version)

Returns a single context in full

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    name = "name_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a single context in full
        api_instance.get_context(name, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->get_context: %s\n" % e)
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
**400** | If the name was not found or any other error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contexts**
> get_contexts(version)

Returns a list of contexts for grid view.

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of contexts for grid view.
        api_instance.get_contexts(version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->get_contexts: %s\n" % e)
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

# **get_data**
> get_data(context, version)

Returns grid view data for specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    context = "context_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns grid view data for specific context
        api_instance.get_data(context, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->get_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  |
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
**200** | If request is successful |  -  |
**400** | If trait is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema**
> get_schema(context, version)

Returns grid view schema for specific context

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
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
    context = "context_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns grid view schema for specific context
        api_instance.get_schema(context, version)
    except okclient.ApiException as e:
        print("Exception when calling GridViewApi->get_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  |
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

