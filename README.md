# Chainbridge

A Python library for the [Bitbutter API](https://docs.bitbutter.com/).

![PyPI](https://img.shields.io/pypi/v/chainbridge.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/chainbridge.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chainbridge.svg)
![PyPI - License](https://img.shields.io/pypi/l/chainbridge.svg)

## Features

* Convenient methods for making calls to the API

## Installation

`chainbridge` is available on PyPi. Install it with `pip`:

```
pip install chainbridge
```

or with `easy_install`:

```
easy_install chainbridge
```

The library is currently tested against Python versions 3.4+.

## Documentation

Create a partner `Client` object for interacting with the API:

```python
# Exposes partner routes
from bitbutter.client import Client
partner_client = Client(api_key, api_secret, base_uri, partnership_id, partner_id)
```

Create a user `Client` object for interacting with the API:

```python
# Exposes user routes
from bitbutter.client import Client
user_client = Client(api_key, api_secret, base_uri, partnership_id, user_id)
```

Follow the partner or user API [documentation](https://docs.bitbutter.com/) to see all endpoints. API reference documentation will be made available with [readthedocs.org](https://readthedocs.org/).

## Testing / Contributing

Any and all contributions are welcome! The process is simple: fork this repo, make your changes, run the test suite, and submit a pull request. Tests are run via [nosetests](https://nose.readthedocs.org/en/latest/). To run the tests, clone the repository and then:

```
# Install the requirements
pip install -r requirements.txt
pip install -r test-requirements.txt

# Run the tests for your current version of Python
make tests
```

If you'd also like to generate an HTML coverage report (useful for figuring out which lines of code are actually being tested), make sure the requirements are installed and then run:

```
make coverage
```

We use [tox](https://tox.readthedocs.org/en/latest/) to run the test suite against multiple versions of Python. You can [install tox](http://tox.readthedocs.org/en/latest/install.html) with `pip` or `easy_install`:

```
pip install tox
easy_install tox
```

Tox requires the appropriate Python interpreters to run the tests in different environments. We recommend using [pyenv](https://github.com/yyuu/pyenv#installation) for this. Once you've installed the appropriate interpreters, running the tests in every environment is simple:

```
tox
```

## Documentation

Documentation is built with [MkDocs](http://www.mkdocs.org/about/release-notes/). You can install [`mkdocs`](http://www.mkdocs.org) (>=17.3) with `pip`:

```
pip install mkdocs
```

You can start the development server with the `mkdocs serve` command:

```
mkdocs serve
```

The documentation will be live at `http://127.0.0.1:8000`.

Documentation is built with the `mkdocs build`.

## Distribution

You should have a `.pyirc` configuration file in your home folder (`~/.pyirc`) containing authentication credentials for TestPyPI and PyPI

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=your_username
password=your_password

[pypitest]
repository=https://testpypi.python.org/pypi
username=your_username
password=your_password
```

Ideally, with strict permissions:

```
chmod 600 ~/.pyirc
```

### Update Version

Update the version in `bitbutter/__init__.py`

### Upload to PyPI Test

```
python setup.py sdist upload -r pypitest
```

The latest version will be available [here](https://test.pypi.org/project/chainbridge/)

### Upload to PyPI Live

```
python setup.py sdist upload -r pypi
```

The latest version will be available [here](https://pypi.org/project/chainbridge/)
