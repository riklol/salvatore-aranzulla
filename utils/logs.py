"""This file handles all the logs"""

import datetime
import os

import utils


# checks that the daily log file exists, if not creates it
def check_log():
    date, hour = utils.dt_hr()
    if not os.path.exists(f"logs/{date}.txt"):
        with open(f"{date}.txt", "w") as lg:
            lg.write(
                f"---------FILE DI LOG---------\nDATA CREAZIONE = {date}\nORA CREAZIONE = {hour}\n-----------------------------\n"
            )
    else:
        pass


# write the logs
def write_logs(cat, action):

    date, hour = utils.globals.dt_hr()

    check_log()

    with open(f"logs/{date}.txt", "a") as log_f:
        log_f.write(f"{date} {hour} - {cat} - {action}\n")
