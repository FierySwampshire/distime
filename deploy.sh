#!/bin/bash

# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# create venv
poetry shell

# install dependencies
poetry install

# run bit code
python exec-slash.py