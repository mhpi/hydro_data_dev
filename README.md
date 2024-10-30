# Hydro Data (Dev)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue)]()

<img src="docs/images/hydro_data_logo.png" alt="Water Wheel" width="500" height="500">

The purpose of this library is to assist with setting up hydrologic models through a Registry of data records. Each `Record` represents a datastore containing one, or many forcings. The `Registry` is a collection of `Records`. 

Each `Record` will have helper functions for preparing the data to be used in a ML application, and will be generate a Torch Dataset as outputs. 

### Installation:
```shell
git clone https://github.com/mhpi/hydro_data_dev.git
cd hydro_data_dev
pip install .
```

### Developer Mode Installation
The same clone as above, but use hatch's developer mode setting
```shell
pip install -e .
```

### Maintainers:
See Pyproject.toml for information

### Contributing:
We request all changes to this repo be made through a fork and PR
