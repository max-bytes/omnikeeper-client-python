# okclient
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 21.0.0-rc14
- Build package: org.openapitools.codegen.languages.PythonExperimentalClientCodegen

## Requirements.

Python &gt;&#x3D;3.9
v3.9 is needed so one can combine classmethod and property decorators to define
object schema properties as classes

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import okclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import okclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import okclient
from pprint import pprint
from okclient.api import ansible_inventory_scan_ingest_api
from okclient.model.ansible_inventory_scan_dto import AnsibleInventoryScanDTO
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
    api_instance = ansible_inventory_scan_ingest_api.AnsibleInventoryScanIngestApi(api_client)
    write_layer_id = "writeLayerID_example" # str | 
search_layer_ids = [
        "searchLayerIDs_example"
    ] # [str] | 
version = "version_example" # str | 
ansible_inventory_scan_dto = AnsibleInventoryScanDTO(
        setup_facts=dict(
            "key": "key_example",
        ),
        yum_installed=dict(),
        yum_repos=dict(),
        yum_updates=dict(),
    ) # AnsibleInventoryScanDTO | 

    try:
        api_instance.ansible_inventory_scan_ingest_ingest_ansible_inventory_scan(write_layer_idsearch_layer_idsversionansible_inventory_scan_dto)
    except okclient.ApiException as e:
        print("Exception when calling AnsibleInventoryScanIngestApi->ansible_inventory_scan_ingest_ingest_ansible_inventory_scan: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnsibleInventoryScanIngestApi* | [**ansible_inventory_scan_ingest_ingest_ansible_inventory_scan**](docs/AnsibleInventoryScanIngestApi.md#ansible_inventory_scan_ingest_ingest_ansible_inventory_scan) | **POST** /api/v{version}/Ingest/AnsibleInventoryScan | 
*AttributeValueImageApi* | [**attribute_value_image_get**](docs/AttributeValueImageApi.md#attribute_value_image_get) | **GET** /api/v{version}/AttributeValueImage | 
*AttributeValueImageApi* | [**attribute_value_image_post**](docs/AttributeValueImageApi.md#attribute_value_image_post) | **POST** /api/v{version}/AttributeValueImage | 
*AuthRedirectApi* | [**auth_redirect_index**](docs/AuthRedirectApi.md#auth_redirect_index) | **GET** /.well-known/openid-configuration | 
*CytoscapeApi* | [**cytoscape_trait_centric**](docs/CytoscapeApi.md#cytoscape_trait_centric) | **GET** /api/v{version}/Cytoscape/traitCentric | 
*GraphQLApi* | [**graph_ql_debug**](docs/GraphQLApi.md#graph_ql_debug) | **POST** /graphql-debug | 
*GraphQLApi* | [**graph_ql_get**](docs/GraphQLApi.md#graph_ql_get) | **GET** /graphql | 
*GraphQLApi* | [**graph_ql_index**](docs/GraphQLApi.md#graph_ql_index) | **POST** /graphql | 
*GraphvizDotApi* | [**graphviz_dot_layer_centric**](docs/GraphvizDotApi.md#graphviz_dot_layer_centric) | **GET** /api/v{version}/GraphvizDot/layerCentric | 
*GraphvizDotApi* | [**graphviz_dot_trait_centric**](docs/GraphvizDotApi.md#graphviz_dot_trait_centric) | **GET** /api/v{version}/GraphvizDot/traitCentric | 
*GridViewApi* | [**grid_view_add_context**](docs/GridViewApi.md#grid_view_add_context) | **POST** /api/v{version}/GridView/context | Adds new context
*GridViewApi* | [**grid_view_change_data**](docs/GridViewApi.md#grid_view_change_data) | **POST** /api/v{version}/GridView/contexts/{context}/change | Saves grid view row changes and returns change results
*GridViewApi* | [**grid_view_delete_context**](docs/GridViewApi.md#grid_view_delete_context) | **DELETE** /api/v{version}/GridView/context/{name} | Deletes specific context
*GridViewApi* | [**grid_view_edit_context**](docs/GridViewApi.md#grid_view_edit_context) | **PUT** /api/v{version}/GridView/context/{name} | Edits specific context
*GridViewApi* | [**grid_view_get_data**](docs/GridViewApi.md#grid_view_get_data) | **GET** /api/v{version}/GridView/contexts/{context}/data | Returns grid view data for specific context
*GridViewApi* | [**grid_view_get_grid_view_context**](docs/GridViewApi.md#grid_view_get_grid_view_context) | **GET** /api/v{version}/GridView/context/{name} | Returns a single context in full
*GridViewApi* | [**grid_view_get_grid_view_contexts**](docs/GridViewApi.md#grid_view_get_grid_view_contexts) | **GET** /api/v{version}/GridView/contexts | Returns a list of contexts for grid view.
*GridViewApi* | [**grid_view_get_schema**](docs/GridViewApi.md#grid_view_get_schema) | **GET** /api/v{version}/GridView/contexts/{context}/schema | Returns grid view schema for specific context
*ImportExportLayerApi* | [**import_export_layer_export_layer**](docs/ImportExportLayerApi.md#import_export_layer_export_layer) | **GET** /api/v{version}/ImportExportLayer/exportLayer | 
*ImportExportLayerApi* | [**import_export_layer_import_layer**](docs/ImportExportLayerApi.md#import_export_layer_import_layer) | **POST** /api/v{version}/ImportExportLayer/importLayer | 
*MetadataApi* | [**metadata_get_metadata**](docs/MetadataApi.md#metadata_get_metadata) | **GET** /api/odata/{context}/$metadata | 
*MetadataApi* | [**metadata_get_service_document**](docs/MetadataApi.md#metadata_get_service_document) | **GET** /api/odata/{context} | 
*OKPluginGenericJSONIngestApi* | [**manage_context_get_all_contexts**](docs/OKPluginGenericJSONIngestApi.md#manage_context_get_all_contexts) | **GET** /api/v{version}/ingest/genericJSON/manage/context | 
*OKPluginGenericJSONIngestApi* | [**manage_context_get_context**](docs/OKPluginGenericJSONIngestApi.md#manage_context_get_context) | **GET** /api/v{version}/ingest/genericJSON/manage/context/{id} | 
*OKPluginGenericJSONIngestApi* | [**manage_context_remove_context**](docs/OKPluginGenericJSONIngestApi.md#manage_context_remove_context) | **DELETE** /api/v{version}/ingest/genericJSON/manage/context/{id} | 
*OKPluginGenericJSONIngestApi* | [**manage_context_upsert_context**](docs/OKPluginGenericJSONIngestApi.md#manage_context_upsert_context) | **POST** /api/v{version}/ingest/genericJSON/manage/context | 
*OKPluginGenericJSONIngestApi* | [**passive_data_ingest**](docs/OKPluginGenericJSONIngestApi.md#passive_data_ingest) | **POST** /api/v{version}/ingest/genericJSON/data | 
*OKPluginGenericJSONIngestApi* | [**passive_files_ingest**](docs/OKPluginGenericJSONIngestApi.md#passive_files_ingest) | **POST** /api/v{version}/ingest/genericJSON/files | 
*OKPluginInsightDiscoveryIngestApi* | [**ingest_file_ingest**](docs/OKPluginInsightDiscoveryIngestApi.md#ingest_file_ingest) | **POST** /api/v{version}/ingest/insight-discovery/file | 
*RestartApplicationApi* | [**restart_application_restart**](docs/RestartApplicationApi.md#restart_application_restart) | **GET** /api/v{version}/RestartApplication/restart | 
*UsageStatsApi* | [**usage_stats_fetch**](docs/UsageStatsApi.md#usage_stats_fetch) | **GET** /api/v{version}/UsageStats/fetch | 

## Documentation For Models

 - [AbstractInboundIDMethod](docs/AbstractInboundIDMethod.md)
 - [AddContextRequest](docs/AddContextRequest.md)
 - [AnsibleInventoryScanDTO](docs/AnsibleInventoryScanDTO.md)
 - [AttributeValueDTO](docs/AttributeValueDTO.md)
 - [AttributeValueType](docs/AttributeValueType.md)
 - [ChangeDataCell](docs/ChangeDataCell.md)
 - [ChangeDataRequest](docs/ChangeDataRequest.md)
 - [EditContextRequest](docs/EditContextRequest.md)
 - [EdmContainerElementKind](docs/EdmContainerElementKind.md)
 - [EdmExpressionKind](docs/EdmExpressionKind.md)
 - [EdmSchemaElementKind](docs/EdmSchemaElementKind.md)
 - [EdmTypeKind](docs/EdmTypeKind.md)
 - [GenericInboundAttribute](docs/GenericInboundAttribute.md)
 - [GenericInboundCI](docs/GenericInboundCI.md)
 - [GenericInboundData](docs/GenericInboundData.md)
 - [GenericInboundRelation](docs/GenericInboundRelation.md)
 - [GraphQLQuery](docs/GraphQLQuery.md)
 - [GridViewColumn](docs/GridViewColumn.md)
 - [GridViewConfiguration](docs/GridViewConfiguration.md)
 - [IEdmEntityContainer](docs/IEdmEntityContainer.md)
 - [IEdmEntityContainerElement](docs/IEdmEntityContainerElement.md)
 - [IEdmExpression](docs/IEdmExpression.md)
 - [IEdmModel](docs/IEdmModel.md)
 - [IEdmSchemaElement](docs/IEdmSchemaElement.md)
 - [IEdmTerm](docs/IEdmTerm.md)
 - [IEdmType](docs/IEdmType.md)
 - [IEdmTypeReference](docs/IEdmTypeReference.md)
 - [IEdmVocabularyAnnotation](docs/IEdmVocabularyAnnotation.md)
 - [InboundIDMethodByAttribute](docs/InboundIDMethodByAttribute.md)
 - [InboundIDMethodByAttributeModifiers](docs/InboundIDMethodByAttributeModifiers.md)
 - [InboundIDMethodByByUnion](docs/InboundIDMethodByByUnion.md)
 - [InboundIDMethodByData](docs/InboundIDMethodByData.md)
 - [InboundIDMethodByIntersect](docs/InboundIDMethodByIntersect.md)
 - [InboundIDMethodByRelatedTempID](docs/InboundIDMethodByRelatedTempID.md)
 - [InboundIDMethodByTemporaryCIID](docs/InboundIDMethodByTemporaryCIID.md)
 - [NoFoundTargetCIHandling](docs/NoFoundTargetCIHandling.md)
 - [ODataEntitySetInfo](docs/ODataEntitySetInfo.md)
 - [ODataFunctionImportInfo](docs/ODataFunctionImportInfo.md)
 - [ODataServiceDocument](docs/ODataServiceDocument.md)
 - [ODataSingletonInfo](docs/ODataSingletonInfo.md)
 - [ODataTypeAnnotation](docs/ODataTypeAnnotation.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [SameTargetCIHandling](docs/SameTargetCIHandling.md)
 - [SameTempIDHandling](docs/SameTempIDHandling.md)
 - [SparseRow](docs/SparseRow.md)

## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A

 Authentication schemes defined for the API:
## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth-dev.mhx.at/auth/realms/acme/protocol/openid-connect/auth
- **Scopes**: N/A


## Author















## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in okclient.apis and okclient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from okclient.api.default_api import DefaultApi`
- `from okclient.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import okclient
from okclient.apis import *
from okclient.models import *
```
