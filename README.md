# omnikeeper-client-python

## Usage

### prepare your environment

This setup was tested and developed using VSCode

~~~bash
# ensure no local stuff is added
unset PYTHONPATH

python3 -m venv .venv
. .venv/bin/activate
pip3 install --upgrade pip

# install project requirements
pip3 install -r requirements.txt

# install additional dev requirements (used to develop)
pip3 install -r requirements-dev.txt
~~~

### get familiar

have a look at our [examples](examples/)

## Build and Package

**Work in Progress**


https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives

~~~bash
python3 -m pip install --upgrade build

~~~
