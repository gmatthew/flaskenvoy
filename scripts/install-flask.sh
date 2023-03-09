#!/bin/sh
apt-get install python3 python3-venv python3-pip -y

## Install Dependencies
cd /work/app
pip3 install -r requirements.txt

# Install webserver
apt-get install gunicorn -y

# Start Webserver
# gunicorn -w 3 main:app