#!/bin/bash
echo "Installing Python dependencies..."

# Create virtualenv only if it doesn't exist
if [ ! -d /var/www/webapp/venv ]; then
  /usr/local/bin/python3.13 -m venv /var/www/webapp/venv
fi

source /var/www/webapp/venv/bin/activate

pip install --upgrade pip
pip install -r /var/www/webapp/requirements.txt
