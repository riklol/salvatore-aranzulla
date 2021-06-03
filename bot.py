import datetime
import os
import random

import colorama
import discord
from dotenv import load_dotenv

colorama.init()

load_dotenv()

client = discord.Client()

TOKEN = os.environ.get("TOKEN")

# list of games which will be the playing status of the bot
lista_giochi_bot = [
    "Skyrim",
    "Hollow Knight",
    "Minecraft",
    "Fortnite",
    "Fat Prisoner Simulator",
    "osu!",
    "Undertale",
    "Assassin's Creed II",
    "Mini Ninjas",
    "Heavy Rain",
    "Time & Eternity",
    "Shadow of the Colossus",
]

coin_flip = ["testa", "croce"]


@client.event
async def on_ready():
    print(colorama.Fore.GREEN + "\n{0.user} è online!".format(client))
    gioco_bot = random.choices(lista_giochi_bot)
    # set the bot status
    await client.change_presence(activity=discord.Game(name=f"{gioco_bot[0]}"))
    print(colorama.Fore.WHITE + f"Il bot sta giocando a {gioco_bot[0]}\n")


@client.event
async def on_message(message):

    nome = message.author.name

    orario = datetime.datetime.now().strftime("%H:%M:%S")

    # emojis
    errore = client.get_emoji(833779980294029314)
    ahh = client.get_emoji(829011307957190767)
    party = client.get_emoji(829011307604869140)
    ok = client.get_emoji(837074839318822943)
    me = client.get_emoji(837074855735066684)
    love = client.get_emoji(837074776928288779)
    succo = client.get_emoji(829011307750883369)

    # super easter egg
    numero_rand = random.randint(1, 1000)
    if numero_rand == 13:
        await message.channel.send(
            f"{party} Complimenti {nome}! Questo è un messaggio casuale con una probabilità dello 0,001% {party}!",
            tts=True,
        )
        print(
            colorama.Fore.GREEN
            + f"{nome} ha trovato l'Easter Egg super segretisimo alle {orario}"
        )
        print(colorama.Fore.WHITE + "")

    # RICKROLL
    # no rickroll
    if (
        "dQw4w9WgXcQ" in message.content
        or "oHg5SJYRHA0" in message.content
        or "j5a0jTc9S10" in message.content
        or "never gonna give you up" in message.content.lower()
    ):
        await message.delete()
        await message.channel.send("Non mi RickRollerai hahaha")
        await message.channel.send(file=discord.File("imgs/ET.jpg"))
        print(f"{nome} ha effettuato un tentativo di rickroll alle {orario}\n")
        return

    # GOOGLE
    # search on Google (query)
    if message.content.lower().startswith("!googla "):
        query = message.content[8:]
        if "." in query:
            await message.channel.send(
                f"{errore} Forse il comando che vuoi usare è **!cerca**"
            )
            return
        query = query.replace(" ", "+")
        await message.channel.send(f"https://google.com/search?q={query.lower()}")
        print(
            f"{nome} ha effettuato una ricerca generica su Google ({query}) alle {orario}\n"
        )
        return

    # search on Google (URL)
    if message.content.lower().startswith("!cerca "):
        query = message.content[7:]
        if "." not in query:
            await message.channel.send(
                f"{errore} Forse il comando che vuoi usare è **!googla**"
            )
            return
        query = query.replace(" ", "")
        url = "https://"
        await message.channel.send(url + query.lower())
        print(
            f"{nome} ha effettuato una ricerca specifica su Google ({query}) alle {orario}\n"
        )
        return

    # BOT
    # view profile image
    if message.content.lower().startswith("!bot_pic"):
        await message.channel.send("Ecco la mia immagine profilo")
        await message.channel.send(file=discord.File("image.png"))
        print(f"{nome} ha visualizzato l'immagine profilo del bot alle {orario}\n")

    # view GitHub repo
    if message.content.lower().startswith("!bot_repo"):
        await message.channel.send(f"{me} Ecco il mio repository di GitHub")
        await message.channel.send("https://github.com/DanyB0/Shadow-Ruler")
        print(f"{nome} ha visualizzato il repo di GitHub del bot alle {orario}\n")

    # GAMES
    # coin flip
    if message.content.lower().startswith("!flip"):
        side = random.choices(coin_flip)[0]
        print(
            f"Esito: {side} (se il messaggio dopo è diverso è stata usata l'opzione --hck)"
        )
        # if the option --hck is used switch the results
        if message.content.lower()[6:] == "--hck":
            if side == "testa":
                side = "croce"
            else:
                side = "testa"
        await message.channel.send(f"{succo} **{side}**")
        print(f"{nome} ha lanciato una moneta con esito {side} alle {orario}\n")
        return

    # HELP
    # help commands
    if message.content.lower().startswith("!comandi"):
        await message.channel.send(
            f"> {succo}\n> Ecco i comandi disponibili (le [ ] vanno omesse):\n> \n> **Bot**\n> - `!bot_pic` --> immagine profilo del bot\n> - `!bot_repo` --> visualizza repository GitHub del bot\n> \n> **Google**\n> - `!googla [query]` --> effettua ricerca su Google\n> - `!cerca [sito]` --> cerca il sito specifico su Google\n> \n> **Giochi**\n> - `!flip [--hck]` --> testa o croce (--hck inverte l'estrazione)"
        )
        print(f"{nome} ha visualizzato la lista comandi alle {orario}\n")
        return


client.run(TOKEN)
