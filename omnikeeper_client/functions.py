from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from pythonjsonlogger import jsonlogger
import logging

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


def get_access_token(config: dict) -> str:
    client = LegacyApplicationClient(client_id=config['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=config['token_url'], username=config['username'], password=config['password'])
    return token["access_token"]
