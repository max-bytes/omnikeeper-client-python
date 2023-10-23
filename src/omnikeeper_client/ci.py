import omnikeeper_client as okc
import omnikeeper_client.typing as okc_typing
import omnikeeper_client.util as okc_util

from gql import gql
from gql.transport.exceptions import (
    TransportQueryError,
)

import uuid

from typing import (
    Dict,
    List,
    Any,
    Optional,
)


# TODO mcsuk: how to create a ci without _name?
# TODO mcsuk: create ci with client side given uuid
def create_ci(ok_api_client: okc.OkApiClient, ci_name: str, layer_id_for_ci_name: str) -> uuid.UUID:
    """creates a ci with _name attribute in specifed layer. 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    ci_name : str
        name of the ci, means _name attribute

    layer_id_for_ci_name : str
        id of layer to store _name attribute

    Returns
    -------
    uuid.UUID
        uuid of inserted CI or None if something fails
    """

    query = gql("""
    mutation($name: String!, $layerIDForName: String!) {
        createCIs(cis: [{name: $name, layerIDForName: $layerIDForName}]) {
            ciids
        }
    }""")
    
    try:
        result = ok_api_client.execute_graphql(query, variables=dict(
                name=ci_name, layerIDForName=layer_id_for_ci_name
        ))
        return uuid.UUID(result["createCIs"]['ciids'][0])
    except TransportQueryError as e:
        return None

def mutate_ci(ok_api_client: okc.OkApiClient, write_layer_id: str, ciid : uuid.UUID, attribute_upserts: Dict[str, Any]) -> bool:
    return mutate_cis(ok_api_client, write_layer_id, {ciid: attribute_upserts})

def mutate_cis(ok_api_client: okc.OkApiClient, write_layer_id: str, attribute_upserts: Dict[str, Dict[str, Any]]) -> bool:
    # TODO doc

    insertAttributes = []
    for ciid, attributes in attribute_upserts.items():
        # TODO add hinting
        insertAttributes += okc_typing.dict_to_attributes(ciid, attributes)

    # print(okc_util.json_pretty(insertAttributes))

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
    
    try:
        
        result = ok_api_client.execute_graphql(query, variables=dict(
            writeLayer=write_layer_id, readLayers=[write_layer_id], insertAttributes=insertAttributes
        ))

        return result
    
    except TransportQueryError as e:
        print(e)
        return False  

# TODO write wrapper function to get attribs of one ci in Dict, Any form
# def get_attributes_of_ci(..., ciid):
#     return get_attributes_of_cis()[ciid]

def get_attributes_of_cis(ok_api_client: okc.OkApiClient, layer_ids: List[str], ciids: Optional[List[uuid.UUID]] = None) -> Dict[uuid.UUID, Dict]:
    """creates a layer by specifying layer_id. 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    layer_ids : List[str]
        ids of layers to include in attributes from

    ciids : Optional[List[uuid.UUID]]
        ciids to fetch, if omitted return all CIs

    Returns
    -------
    Dict[uuid.UUID, Dict]
        dictionary of CIs with dict of attributes
    """



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
   
    try:
        ciids_query = None
        if ciids is not None:
            ciids_query = list(map(lambda ciid: str(ciid), ciids))
        
        result = ok_api_client.execute_graphql(query, variables=dict(layers=layer_ids, ciids=ciids_query))

        cis = {ci['id']: 
               okc_typing.attributes_to_dict(ci['mergedAttributes']) 

               for ci in result['cis']}

        return cis
    
    except TransportQueryError as e:
        return False    