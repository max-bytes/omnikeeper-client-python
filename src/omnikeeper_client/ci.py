import omnikeeper_client as okc

from gql import gql
from gql.transport.exceptions import (
    TransportQueryError,
)

import uuid

# TODO mcsuk: how to create a ci without _name?
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

# TODO mcsuk: answer if ok to make mutate_ci more convenient and include graphQL_merged_attributes_to_simple_attributes from data types
# TODO mcsuk: does insertAttributes mean upsert attributes?

# def mutate_cis(ok_api_client: okc.OkApiClient, layer_id: str) -> bool:
#     """creates a layer by specifying layer_id. 

#     Parameters
#     ----------
#     ok_api_client : OkApiClient
#         The OkApiClient instance representing omnikeeper connection

#     layer_id : str
#         id of layer to create, must only contain charaters [A-Za-z_]

#     Returns
#     -------
#     bool
#         True, if layer was created or was already present. False, if something fails
#     """

#     query = gql("""
#     mutation ($id: String!) {
#         manage_createLayer(id: $id) {
#             id
#         }
#     }""")
    
#     try:
#         ok_api_client.execute_graphql(query, variables=dict(id=layer_id))
#         return True
#     except TransportQueryError as e:
#         return False    

# def get_ci_attributes(ok_api_client: okc.OkApiClient, layer_id: str) -> bool:
#     """creates a layer by specifying layer_id. 

#     Parameters
#     ----------
#     ok_api_client : OkApiClient
#         The OkApiClient instance representing omnikeeper connection

#     layer_id : str
#         id of layer to create, must only contain charaters [A-Za-z_]

#     Returns
#     -------
#     bool
#         True, if layer was created or was already present. False, if something fails
#     """

#     query = gql("""
#     mutation ($id: String!) {
#         manage_createLayer(id: $id) {
#             id
#         }
#     }""")
    
#     try:
#         ok_api_client.execute_graphql(query, variables=dict(id=layer_id))
#         return True
#     except TransportQueryError as e:
#         return False    