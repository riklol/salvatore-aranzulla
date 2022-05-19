#!/bin/bash
#create virtual env
python3 -m venv env
#load env
source env/bin/activate
#install requirements
pip install -r requirements.txt
echo "Done, now you can start the bot with: ./start.sh"
