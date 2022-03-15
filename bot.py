from os import getenv

import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # send a message on the console and in a specific channel when the bot is online
    channel = bot.get_channel(941372997674106951)
    print("\nSalvatore è online!\n")
    await channel.send("\nSono online!")

# load the functions
bot.load_extension("cogs.credits")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.neko")
bot.load_extension("cogs.nhnt")
bot.load_extension("cogs.vocal")

# run the bot
bot.run(TOKEN)
