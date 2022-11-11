from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import urllib.request, json

def get_access_token(config: dict) -> str:
    # first retrieve token_url from omnikeeper endpoint
    oauth_url = "%s/.well-known/openid-configuration" % config['omnikeeper_url']
    with urllib.request.urlopen(oauth_url) as url:
        data = json.loads(url.read().decode())
    token_url = data["token_endpoint"]

    # now fetch access_token from token_url, providing username and password
    client = LegacyApplicationClient(client_id=config['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, username=config['username'], password=config['password'])
    return token["access_token"]

def create_graphql_client(url: str, access_token: str) -> Client:
    transport = AIOHTTPTransport(url=url, headers={'Authorization': "Bearer %s" % access_token})
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

def execute_graphql(client: Client, query: str, variables: str = None):
    prepared_query = gql(query)
    data = client.execute(prepared_query, variable_values=variables)
    return data