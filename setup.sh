#!/bin/bash

# Get the py-evm folder downloaded and working
git submodule init
git submodule update

# Create and enter a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip 
pip install --upgrade setuptools
pip install -r requirements.txt
cd py-evm
pip install -r requirements-docs.txt
pip install -e . -r requirements-dev.txt

