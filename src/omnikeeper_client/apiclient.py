
from gql import gql, Client as GqlClient
from graphql import DocumentNode
from gql.transport.requests import RequestsHTTPTransport

import oauthlib_sessionhandler

from typing import (
    Any,
    Dict,
    Optional, Union
)

class OkApiClient():
    # TODO doc class

    def __init__(self,
                 backend_url : str,

                 client_id : str = None,
                 client_secret : str = None,
                 username : str = None,
                 password : str = None,

                ) -> None:
        
        self._backend_url = backend_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password

        self._use_auth = False
        self._oash = None
        if self._client_id is not None:
            self._use_auth = True
            self._oash = oauthlib_sessionhandler.OAuthLibSessionHandler(
                wellknown_url=f"{self._backend_url}/.well-known/openid-configuration",
                client_id=self._client_id,
                client_secret=self._client_secret,
                username=self._username,
                password=self._password,
            )

        self.graphql_url = f"{self._backend_url}/graphql"

    def _get_graphql_client(self) -> GqlClient:
        headers={}
        if self._use_auth:
            headers['Authorization'] = f"Bearer {self._oash.get_accesstoken()}"

        transport = RequestsHTTPTransport(url=self.graphql_url, headers=headers, verify=True)
        return GqlClient(transport=transport, fetch_schema_from_transport=True)
    
    # TODO doc at least public functions
    def execute_graphql(self, query: Union[str, DocumentNode], variables: Optional[Dict[str, Any]] = None):
        client = self._get_graphql_client()
        
        prepared_query = gql(query) if query is str else query
        data = client.execute(prepared_query, variable_values=variables)
        
        return data