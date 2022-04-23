"""Constants file"""

import os
from os import getenv

from dotenv import load_dotenv

import datetime

# bot token
load_dotenv()
TOKEN = getenv("TOKEN")

# base directory
BASE_DIR = os.getcwd()

# these are not constants but are here to simplify the work
date = datetime.datetime.now().strftime("%Y-%m-%d")
hour = datetime.datetime.now().strftime("%H:%M:%S")

