#!python3

from pathlib import Path

import tomllib

with open(Path(__file__).parent / "pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)
    print(pyproject["project"]["version"])
