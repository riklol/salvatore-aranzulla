"""This file handle all the logs"""

import datetime
import os
import src


# write the logs
def write_logs(cat, action):

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    
    with open(f"logs/{date}.txt", "a") as log_f:
        log_f.write(f"{date} {hour} - {cat} - {action}\n")
