#!/bin/bash
#pull latest code
git pull
#update env
source env/bin/activate
#update dependencies
pip3 install -r requirements.txt
#restart bot
python3 bot.py
