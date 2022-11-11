from setuptools import setup
setup(
    name='omnikeeper_client',
    packages=['omnikeeper_client'],
    version='1.0.0',
    description='Python library containing helper functions for implementing omnikeeper clients',
    author='Maximilian Csuk',
    license='Apache 2.0',
    install_requires=["aiohttp==3.8.3","gql==3.4.0","requests==2.25.1","numpy==1.21.6","oauthlib==3.2.0","requests-oauthlib==1.3.0","python-json-logger==2.0.2"]
)