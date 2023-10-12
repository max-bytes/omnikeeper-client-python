from setuptools import setup
setup(
    name='omnikeeper_client',
    packages=['omnikeeper_client'],
    package_dir={
        'omnikeeper_client': 'src',
    },
    version='3.4.0',
    description='Python library containing helper functions for implementing omnikeeper clients',
    author='Maximilian Csuk',
    license='Apache 2.0',
    install_requires=[
        "appengine-python-standard~=1.1",
        "gql~=3.4",
        "oauthlib~=3.2",
        "pandas>=2.0",
        "python-json-logger~=2.0",
        "requests-oauthlib~=1.3",
        "requests-toolbelt~=0.10",
        "webcolors~=1.3",
    ]
)
