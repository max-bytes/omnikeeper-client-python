from setuptools import setup
setup(
    name='omnikeeper_client',
    packages=['omnikeeper_client'],
    version='3.4.0',
    description='Python library containing helper functions for implementing omnikeeper clients',
    author='Maximilian Csuk',
    license='Apache 2.0',
    install_requires=["webcolors==1.3","aiohttp==3.8.3","gql==3.4.1","requests==2.25.1","oauthlib==3.2.0","requests-oauthlib==1.3.0","python-json-logger==2.0.2", "requests_toolbelt==0.10.1", "pandas==2.1.0"]
)
