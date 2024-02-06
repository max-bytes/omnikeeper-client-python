import omnikeeper_client as okc

from gql import gql
from gql.transport.exceptions import (
    TransportQueryError,
)

def create_layer(ok_api_client: okc.OkApiClient, layer_id: str, description: str = None, argbColor: int = None) -> bool:
    """creates a layer by specifying layer_id. 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    layer_id : str
        id of layer to create, must only contain charaters [A-Za-z_]

    description : str
        description to set for this layer

    argbColor : int
        color of layer, see omnikeeperclient.hexString2RGBColor() for more details

    Returns
    -------
    bool
        True, if layer was created or was already present. False, if something fails
    """

    query = gql("""
    mutation ($id: String!) {
        manage_createLayer(id: $id) {
            id
        }
    }""")
    
    try:
        ok_api_client.execute_graphql(query, variables=dict(id=layer_id))

        if description is not None or argbColor is not None:
            description = description or ""
            argbColor = argbColor or -1
            update_layerdata(ok_api_client, layer_id, description, argbColor)

        return True
    except TransportQueryError as e:
        return False

def update_layerdata(ok_api_client: okc.OkApiClient, layer_id: str, description: str, argbColor: int) -> bool:
    """updates attributes of a layer

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    layer_id : str
        id of layer to mutate, must only contain charaters [A-Za-z_]

    description : str
        description to set for this layer

    argbColor : int
        color of layer, see omnikeeperclient.hexString2RGBColor() for more details


    Returns
    -------
    bool
        True, if layer was updated. False, if something fails
    """


    query = gql("""
    mutation ($id: String!, $description: String!, $color: Int!) {
        manage_upsertLayerData(
            layer: {id: $id, description: $description, state: ACTIVE, color: $color, generators: []}
        ) {
            id
        }
    }""")

    try:
        ok_api_client.execute_graphql(query, variables=dict(
            id=layer_id,
            description=description,
            color=argbColor)
        )
        return True
    except TransportQueryError as e:
        return False
    
def truncate_layer(ok_api_client: okc.OkApiClient, layer_id: str) -> bool:
    """truncate a layer, removing all attributes and relations on all CIs on that layer

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    layer_id : str
        id of layer to truncate

    Returns
    -------
    bool
        True, if layer was truncated. False, if something fails
    """

    query = gql("""
    mutation ($id: String!) {
        manage_truncateLayer(id: $id)
    }
    """)

    try:
        ok_api_client.execute_graphql(query, variables=dict(
            id=layer_id,
        ))
        return True
    except TransportQueryError as e:
        return False    