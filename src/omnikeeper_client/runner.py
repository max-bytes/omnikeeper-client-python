import argparse
import logging
import yaml
from gql import Client, gql
from .functions import get_access_token, create_logger, create_graphql_client, execute_graphql

class Runner:
    def get_config(self, config_file_path: str) -> dict:
        """Parses the configuration file and returns the parsed content in a dictionary format."""
        try:
            with open(config_file_path, "r") as stream:
                return yaml.safe_load(stream)
        except FileNotFoundError:
            print(f"Error: Config file not found at {config_file_path}")
            exit(1)
        except yaml.YAMLError as e:
            print(f"Error: Unable to parse config file at {config_file_path}: {e}")
            exit(1)

    def parse_args(self):
        """Parse the args."""
        parser = argparse.ArgumentParser(
            description='omnikeepet-data-validator')
        parser.add_argument('--config_file', type=str, required=True,
                            help=' Configuration file location')
        return parser.parse_args()

    def get_logger(self, level=logging.INFO, logfile='example.log'):
        """Setup logging for the project and return logging object"""
    
        # TODO save also loggs on a file
    
        logging.basicConfig(
            level=level,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler()
            ]
        )
    
        logger = logging.getLogger()
        return logger
    
    def run(self):
        """The main runner responsible for running the queryclases"""

        args = self.parse_args()

        config = self.get_config(args.config_file)

        if 'log_level' not in config:
            print('Please provide the logging level in configuration file.')
            exit(1)

        logger = self.get_logger(config['log_level'])

        logger.info('Started the main runner for processing queryclasses...')

        access_token = get_access_token(config['oauth'])
        client = create_graphql_client(f"{config['omnikeeper']['url']}/graphql", access_token)

        query_classes = __import__('queryclasses')

        for query_class  in config['queryclasses']:
            query_class_obj = getattr(query_classes, query_class['class'])(client, logger, query_class['cfg'])
            query_class_obj.process()

        logger.info('The main runner finished processing all queryclasses')
