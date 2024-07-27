#!/bin/bash

VENV_PATH=${1:-$(pwd)/.pyenv}
WORKING_DIRECTORY=${2:-$(pwd)}

# Create virtual environment if it does not exist
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_PATH
    source $VENV_PATH/bin/activate
    pip install -r requirements.txt
else
    echo "Activating existing virtual environment..."
    source $VENV_PATH/bin/activate
fi

# Start the Flask application
cd $WORKING_DIRECTORY
python proxy.py
