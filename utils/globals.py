import datetime
import os
from os import getenv

from dotenv import load_dotenv

# bot token
load_dotenv()
TOKEN = getenv("TOKEN")

# base directory
BASE_DIR = os.getcwd()


# date, hour
def dt_hr():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    return date, hour
