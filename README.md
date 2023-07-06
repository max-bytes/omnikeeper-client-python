# omnikeeper-client-python

## Requirements

* Python 3.9

## Development Setup

### create virtual environment (optional)

```bash
pip install virtualenv
pip install wheel
virtualenv -p python3.9 venv
```

or

```bash
python3.9 -m venv venv
```

### enter virtual environment (optional)

```bash
source ./venv/bin/activate
```

### install requirements

```bash
pip3 install -r requirements.txt
```

### build library

```bash
python setup.py bdist_wheel
```

### upload to PyPi

```bash
twine upload dist/omnikeeper_client-2.0.0-py3-none-any.whl
```