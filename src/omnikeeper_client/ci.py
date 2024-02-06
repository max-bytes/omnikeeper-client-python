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


def create_ci(ok_api_client: okc.OkApiClient, ci_name: Optional[str] = None, layer_id_for_ci_name: Optional[str] = None, ciid: Optional[uuid.UUID] = None) -> uuid.UUID:
    """creates a ci with _name attribute in specifed layer. 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    ci_name : Optional[str]
        name of the ci, means _name attribute

    layer_id_for_ci_name : Optional[str]
        id of layer to store _name attribute

    ciid: Optional[uuid.UUID]
        optional client-provided ciid 

    Returns
    -------
    uuid.UUID
        uuid of inserted CI or None if something fails
    """

    query = gql("""
    mutation($name: String, $layerIDForName: String, $ciid: Guid) {
        createCIs(cis: [{name: $name, layerIDForName: $layerIDForName, ciid: $ciid}]) {
            ciids
        }
    }""")
    
    result = ok_api_client.execute_graphql(query, variables=dict(
            name=ci_name, layerIDForName=layer_id_for_ci_name, ciid=ciid
    ))
    return uuid.UUID(result["createCIs"]['ciids'][0])

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

def get_attributes_of_ci(ok_api_client: okc.OkApiClient, layer_ids: List[str], ciid: uuid.UUID) -> Dict:
    """fetches all attributes of a single ci

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    layer_ids : List[str]
        ids of layers to include in attributes from

    ciid : uuid.UUID
        ciid to fetch

    Returns
    -------
    Dict
        dict of attributes, empty dict if ci contains no attributes
    """
        
    return get_attributes_of_cis(ok_api_client, layer_ids, ciids=[ciid]).get(str(ciid), {})

def get_attributes_of_cis(ok_api_client: okc.OkApiClient, layer_ids: List[str], ciids: Optional[List[uuid.UUID]] = None) -> Dict[uuid.UUID, Dict]:
    """fetches all attributes of cis

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