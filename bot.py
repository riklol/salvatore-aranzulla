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

# load the functions
bot.load_extension("cogs.credits")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.neko")
bot.load_extension("cogs.nhnt")
bot.load_extension("cogs.vocal")

bot.run(TOKEN)
