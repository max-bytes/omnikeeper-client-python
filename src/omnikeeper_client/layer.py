import omnikeeper_client as okc
from gql import gql

def create_layer(ok_api_client: okc.OkApiClient, layer_id: str) -> bool:
    query = gql("""
    mutation ($id: String!) {
        manage_createLayer(id: $id) {
            id
        }
    }""")
    ok_api_client.execute_graphql(query, variables=dict(id=layer_id))
    return True