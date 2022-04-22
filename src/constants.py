"""Constants file"""

import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")

BASE_DIR = os.getcwd()
