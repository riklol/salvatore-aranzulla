import os

from discord import Intents
from discord.ext import commands

import utils

# takes the date and the hour
date, hour = utils.dt_hr()

# first log file
if not os.path.exists("logs"):
    os.mkdir("logs")
os.chdir("logs")

if not os.path.exists(f"{date}.txt"):
    with open(f"{date}.txt", "w") as lg:
        lg.write(
            f"---------FILE DI LOG---------\nDATA CREAZIONE = {date}\nORA CREAZIONE = {hour}\n-----------------------------\n"
        )
else:
    pass

os.chdir(utils.BASE_DIR)

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    # send a message on the console and in a specific channel when the bot is online
    channel = bot.get_channel(941372997674106951)
    print("\nSalvatore è online!\n")
    utils.write_logs("Start", "Bot started")
    await channel.send("\nSono online!")


# load the functions
bot.load_extension("cogs.credits")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.neko")
# bot.load_extension("cogs.nhnt")
bot.load_extension("cogs.vocal")

# run the bot
bot.run(utils.TOKEN)
