from __future__ import annotations

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from gql import gql, Client
from graphql import DocumentNode
from gql.transport.requests import RequestsHTTPTransport
import requests
from webcolors import hex_to_rgb
import json
import uuid
from pythonjsonlogger import jsonlogger
import logging
from gql.transport.requests import log as requests_logger
from deprecated import deprecated

import omnikeeper_client as okc
import omnikeeper_client.typing as okc_typing

# HACK: gql is VERY verbose, even on log level INFO; therefore we manually set the log level for the transport to a higher level
# see https://gql.readthedocs.io/en/stable/advanced/logging.html#disabling-logs
requests_logger.setLevel(logging.WARNING)

from typing import (
    Any,
    Dict,
    Optional, Union
)

def create_logger(level: int):
    logger = logging.getLogger()
    logger.setLevel(level)

    # clean up existing stuff
    list(map(logger.removeHandler, logger.handlers))
    list(map(logger.removeFilter, logger.filters))

    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = jsonlogger.JsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

@deprecated(category=FutureWarning, reason="please use OkApiClient() to access Omnikeeper, you should not need any access tokens")
def get_access_token(config: dict) -> str:
    okclient = okc.OkApiClient(
        backend_url=config['omnikeeper_url'],
        client_id=config['client_id'],
        username=config['username'],
        password=config['password'],
    )

    if okclient._oash is not None:
        return okclient._oash.get_accesstoken()
    else:
        return None

@deprecated(category=FutureWarning, reason="please use OkApiClient() to access Omnikeeper, you should not need a raw gql Client but if really needed, use  OkApiClient()._get_graphql_client()")
def create_graphql_client(url: str, access_token: Optional[str] = None) -> Client:
    headers={}
    if access_token is not None:
        headers['Authorization'] = "Bearer %s" % access_token
    transport = RequestsHTTPTransport(url=url, headers=headers, verify=True)
    # transport = AIOHTTPTransport(url=url, headers={'Authorization': "Bearer %s" % access_token})
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

@deprecated(category=FutureWarning, reason="please use OkApiClient().execute_graphql() instead")
def execute_graphql(client: Client, query: Union[str, DocumentNode], variables: Optional[Dict[str, Any]] = None):
    prepared_query = gql(query) if query is str else query
    data = client.execute(prepared_query, variable_values=variables)
    return data

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def create_layer(client: Client, layer_id: str) -> bool:
    query = gql("""
    mutation ($id: String!) {
        manage_createLayer(id: $id) {
            id
        }
    }""")
    execute_graphql(client, query, variables=dict(id=layer_id))
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def truncate_layer(client: Client, layer_id: str) -> bool:
    query = gql("""
    mutation ($id: String!) {
        manage_truncateLayer(id: $id)
    }
    """)
    execute_graphql(client, query, variables=dict(id=layer_id))
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def hexString2RGBColor(hex: str) -> int:
    return okc.hexString2RGBColor(hex)

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def upsert_layerdata(client: Client, layer_id: str, description: str, argbColor: int) -> bool:
    query = gql("""
    mutation ($id: String!, $description: String!, $color: Int!) {
        manage_upsertLayerData(
            layer: {id: $id, description: $description, state: ACTIVE, color: $color, generators: []}
        ) {
            id
        }
    }""")
    execute_graphql(client, query, variables=dict(id=layer_id, description=description, color=argbColor))
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.typing.attributevalue_to_pythonvalue() instead")
def graphQL_merged_attribute_value_to_simple_value(attribute_value: Dict[str, Any]) -> Any:
    return okc_typing.attributevalue_to_pythonvalue(attribute_value)

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.typing.attributes_to_dict() instead")
def graphQL_merged_attributes_to_simple_attributes(merged_attributes: list[Dict[str, Any]]) -> Dict[str, Any]:
    return okc_typing.attributes_to_dict(merged_attributes)

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def get_ci_attributes(client: Client, layer_ids: list[str], ciids: Optional[list[uuid.UUID]] = None) -> Dict[uuid.UUID, Any]:
    query = gql("""
    query ($layers: [String]!, $ciids: [Guid]) {
        cis(layers: $layers, ciids: $ciids) {
            id
            mergedAttributes {
                attribute {
                    name
                    value {
                        type
                        isArray
                        values
                    }
                }
            }
        }
    }""")
    result = execute_graphql(client, query, variables=dict(layers=layer_ids, ciids=list(map(lambda ciid: str(ciid), ciids))))

    cis = {ci['id']:graphQL_merged_attributes_to_simple_attributes(ci['mergedAttributes']) for ci in result['cis']}
    
    return cis

def build_graphQL_InsertCIAttributeInputType(ciid: uuid.UUID, name: str, value: Any, type: str = "TEXT", isArray: bool = False) -> dict[str, Any]:
    return dict(ci=str(ciid), name=name, value=dict(type=type, isArray=isArray, values=[value]))

# @deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
# TODO next
def mutate_cis(client: Client, write_layer_id: str, read_layer_ids: list[str], attribute_inserts: list[dict[str, Any]]) -> bool:
    query = gql("""
    mutation ($writeLayer: String!, $readLayers: [String]!, $insertAttributes: [InsertCIAttributeInputType], $removeAttributes: [RemoveCIAttributeInputType], $insertRelations: [InsertRelationInputType], $removeRelations: [RemoveRelationInputType]) {
        mutateCIs(
            writeLayer: $writeLayer
            readLayers: $readLayers
            insertAttributes: $insertAttributes
            removeAttributes: $removeAttributes
            insertRelations: $insertRelations
            removeRelations: $removeRelations
        ) {
            affectedCIs {
                id
            }
        }
    }""")
    result = execute_graphql(client, query, variables=dict(
        writeLayer=write_layer_id, readLayers=read_layer_ids, insertAttributes=attribute_inserts
        ))
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead")
def create_ci(client: Client, ci_name: str, layer_id_for_ci_name: str) -> uuid.UUID:
    query = gql("""
    mutation($name: String!, $layerIDForName: String!) {
        createCIs(cis: [{name: $name, layerIDForName: $layerIDForName}]) {
            ciids
        }
    }""")
    result = execute_graphql(client, query, variables=dict(
        name=ci_name, layerIDForName=layer_id_for_ci_name
        ))
    return uuid.UUID(result["createCIs"]['ciids'][0])
