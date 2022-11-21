from typing import Union
from numpy import array
from requests.structures import CaseInsensitiveDict
import requests
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import hashlib
import json
import io

def build_temp_id(*parts) -> str:
    return ' - '.join(parts)

def build_attribute(name: str, values: 'Union[list[str],str]', type: str = "Text", isArray: bool = False) -> dict:
    return {
        "name":name,
        "value":{
            "type": type,
            "isArray": isArray,
            "values": values if isinstance(values, list) else [values]
        }
    }

def build_id_method_data(attributes: dict) -> dict:
    return {"type": "OKPluginGenericJSONIngest.InboundIDMethodByData, OKPluginGenericJSONIngest", "attributes": attributes}

def build_id_method_attribute(attribute: dict, caseInsensitive: bool = False) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByAttribute, OKPluginGenericJSONIngest",
        "attribute": attribute,
        "modifiers": {
            "caseInsensitive": caseInsensitive
        }}

def build_id_method_intersect(inner: array) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByIntersect, OKPluginGenericJSONIngest",
        "inner": inner
    }


def build_id_method_union(inner: array) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByUnion, OKPluginGenericJSONIngest",
        "inner": inner
    }

def build_id_method_related_temp_id(tempID: str, outgoing: bool, predicateID: str) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByRelatedTempID, OKPluginGenericJSONIngest",
        "tempID": tempID,
        "outgoingRelation": outgoing,
        "predicateID": predicateID
    }

def get_access_token(config: dict) -> str:
    client = LegacyApplicationClient(client_id=config['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=config['token_url'], username=config['username'], password=config['password'])
    return token["access_token"]

# taken from https://death.andgravity.com/stable-hashing
def hash_data(data) -> bytes:
    dumped = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        indent=None,
        separators=(',', ':'),
    )
    hash = hashlib.md5(dumped.encode('utf-8')).digest()
    return hash

def ingest_data(config: dict, data: array, access_token: str):

    api_url = f"%s/api/v1/ingest/genericJSON/data" % (config["url"])
    params={
        "readLayerIDs": config["read_layer_ids"],
        "writeLayerID": config["write_layer_id"]
    }
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer %s" % access_token

    resp = requests.post(api_url, params=params, json=data, verify=False, headers=headers, timeout=config["timeout_seconds"])
    if resp.status_code != 200:
        raise Exception(f"Expected return code 200, received {resp.status_code}: {resp.content}")

def ingest_files(config: dict, files: list[io.StringIO], access_token: str):
    api_url = f"%s/api/v1/ingest/genericJSON/files" % (config["url"])
    params={
        "context": config["ingest_context"]
    }
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer %s" % access_token

    final_files=list(map(lambda file: ('files', file), files))
    resp = requests.post(api_url, params=params, files=final_files, verify=False, headers=headers, timeout=config["timeout_seconds"])
    if resp.status_code != 200:
        raise Exception(f"Expected return code 200, received {resp.status_code}: {resp.content}")
