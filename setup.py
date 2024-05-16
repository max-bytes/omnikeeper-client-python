from setuptools import setup
setup(
    name='omnikeeper_client',
    packages=['omnikeeper_client'],
    package_dir={
        'omnikeeper_client': 'src/omnikeeper_client',
    },
    version='5.3.0',
    description='Python library containing helper functions for implementing omnikeeper clients',
    author='Maximilian Csuk',
    license='Apache 2.0',
    install_requires=[
        # "oauthlib-sessionhandler @ git+https://github.com/MHx-Operations/oauthlib-sessionhandler.git@1a87cbc23dba7e0a9b20fe7eb8a19c41ab3f2980" NOTE: cannot include dependency to git+https library, manual installation required
        "appengine-python-standard~=1.1",
        "gql~=3.4",
        "oauthlib~=3.2",
        "pandas>=2.0",
        "python-json-logger~=2.0",
        "requests-oauthlib~=1.3",
        "requests-toolbelt~=0.10",
        "webcolors~=1.3",
        "pydantic~=2.6",
    ]
)
