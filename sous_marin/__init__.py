import os
import pytoml

__version__ = pytoml.load(open(os.path.join(__path__[0], os.pardir, "pyproject.toml")))[
    "tool"
]["poetry"]["version"]
