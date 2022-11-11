from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def get_access_token(config: dict) -> str:
    client = LegacyApplicationClient(client_id=config['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=config['token_url'], username=config['username'], password=config['password'])
    return token["access_token"]

def create_graphql_client(url: str, access_token: str) -> Client:
    transport = AIOHTTPTransport(url=url, headers={'Authorization': "Bearer %s" % access_token})
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

def execute_graphql(client: Client, query: str, variables: str):
    prepared_query = gql(query)
    data = client.execute(query=prepared_query, variables=variables)
    return data