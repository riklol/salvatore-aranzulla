# bot.py
import discord


TOKEN = "ODM0NDU5NDU5NDA0NDMxNDkw.YIBM7g.wTCbevovCVNDU8QqVcj4gmYYJ0c"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.content.startswith("!play https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")

    elif message.content.startswith("https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")

client.run(TOKEN)