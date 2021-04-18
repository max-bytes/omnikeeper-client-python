# okclient.CIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ciids**](CIApi.md#get_all_ciids) | **GET** /api/v{version}/CI/getAllCIIDs | list of all CI-IDs
[**get_ciby_id**](CIApi.md#get_ciby_id) | **GET** /api/v{version}/CI/getCIByID | single CI by CI-ID
[**get_cis_by_id**](CIApi.md#get_cis_by_id) | **GET** /api/v{version}/CI/getCIsByID | multiple CIs by CI-ID  !Watch out for the query URL getting too long because of a lot of CIIDs!  TODO: consider using POST


# **get_all_ciids**
> [str] get_all_ciids(version)

list of all CI-IDs

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import ci_api
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
    api_instance = ci_api.CIApi(api_client)
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # list of all CI-IDs
        api_response = api_instance.get_all_ciids(version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling CIApi->get_all_ciids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

**[str]**

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

# **get_ciby_id**
> CIDTO get_ciby_id(layer_ids, ciid, version)

single CI by CI-ID

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import ci_api
from okclient.model.cidto import CIDTO
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
    api_instance = ci_api.CIApi(api_client)
    layer_ids = [
        1,
    ] # [int] | Specifies which layers contribute to the result, and in which order
    ciid = "CIID_example" # str | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Specify datetime, for which point in time to get the data; leave empty to use current time (https://www.newtonsoft.com/json/help/html/DatesInJSON.htm) (optional)

    # example passing only required values which don't have defaults set
    try:
        # single CI by CI-ID
        api_response = api_instance.get_ciby_id(layer_ids, ciid, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling CIApi->get_ciby_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # single CI by CI-ID
        api_response = api_instance.get_ciby_id(layer_ids, ciid, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling CIApi->get_ciby_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[int]**| Specifies which layers contribute to the result, and in which order |
 **ciid** | **str**|  |
 **version** | **str**|  |
 **at_time** | **datetime**| Specify datetime, for which point in time to get the data; leave empty to use current time (https://www.newtonsoft.com/json/help/html/DatesInJSON.htm) | [optional]

### Return type

[**CIDTO**](CIDTO.md)

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

# **get_cis_by_id**
> [CIDTO] get_cis_by_id(layer_ids, ciids, version)

multiple CIs by CI-ID  !Watch out for the query URL getting too long because of a lot of CIIDs!  TODO: consider using POST

### Example

* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):
```python
import time
import okclient
from okclient.api import ci_api
from okclient.model.cidto import CIDTO
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
    api_instance = ci_api.CIApi(api_client)
    layer_ids = [
        1,
    ] # [int] | Specifies which layers contribute to the result, and in which order
    ciids = [
        "CIIDs_example",
    ] # [str] | 
    version = "version_example" # str | 
    at_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Specify datetime, for which point in time to get the data; leave empty to use current time (https://www.newtonsoft.com/json/help/html/DatesInJSON.htm) (optional)

    # example passing only required values which don't have defaults set
    try:
        # multiple CIs by CI-ID  !Watch out for the query URL getting too long because of a lot of CIIDs!  TODO: consider using POST
        api_response = api_instance.get_cis_by_id(layer_ids, ciids, version)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling CIApi->get_cis_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # multiple CIs by CI-ID  !Watch out for the query URL getting too long because of a lot of CIIDs!  TODO: consider using POST
        api_response = api_instance.get_cis_by_id(layer_ids, ciids, version, at_time=at_time)
        pprint(api_response)
    except okclient.ApiException as e:
        print("Exception when calling CIApi->get_cis_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_ids** | **[int]**| Specifies which layers contribute to the result, and in which order |
 **ciids** | **[str]**|  |
 **version** | **str**|  |
 **at_time** | **datetime**| Specify datetime, for which point in time to get the data; leave empty to use current time (https://www.newtonsoft.com/json/help/html/DatesInJSON.htm) | [optional]

### Return type

[**[CIDTO]**](CIDTO.md)

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

