# bot.py
import discord
import requests


TOKEN = "ODM0NDU5NDU5NDA0NDMxNDkw.YIBM7g.wTCbevovCVNDU8QqVcj4gmYYJ0c"

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    # no rickroll
    if message.content.startswith("!play https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")

    # no rickroll
    elif message.content.startswith("https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")

    # cerca su Google (pagina principale)
    elif message.content.startswith("!googla "):
        query = message.content[8:]
        query = query.replace(" ", "+")
        await message.channel.send(f"https://google.com/search?q={query.lower()}")

    # cerca su Google (nome sito)
    elif message.content.startswith("!cerca "):
        query = message.content[7:]
        query = query.replace(" ", "")
        url = "https://"
        await message.channel.send(url + query.lower())

    # cerca manga
    elif message.content.startswith("!manga "):
        pre_query = message.content[7:9]
        query = message.content[10:]
        query = query.replace(" ", "-")

        # cerca su AsuraScans
        if pre_query == "as":
            url = "https://www.asurascans.com/comics/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )

        # cerca su LeviatanScans
        elif pre_query == "lv":
            url = "https://leviatanscans.com/lcomic/manga/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )

        # cerca su WebtoonScan
        elif pre_query == "ws":
            url = "https://webtoonscan.com/manhwa/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )

    # lista manga
    elif message.content.startswith("!manga_help"):
        await message.channel.send("Ecco i siti disponibili:")
        await message.channel.send("AsuraScans (**as**)")
        await message.channel.send("LeviatanScans (**lv**)")
        await message.channel.send("WebtoonScan (**ws**)")

    # eroi overwatch
    elif message.content.startswith("!ov_eroi "):
        query = message.content[9:]
        if query == "lista":
            await message.channel.send(
                "Ecco la lista degli eroi di Overwatch (ci metterò un po' e potresti vedere degli stickers):"
            )

            for eroe in lista_eroi:
                await message.channel.send(eroe)
            return

        url = "https://playoverwatch.com/it-it/heroes/"
        await message.channel.send(
            f"Ecco cosa ho trovato per {query}: " + (url + query.lower())
        )

    # help comandi
    elif message.content.startswith("!comandi"):
        await message.channel.send(
            "Ecco i comandi disponibili (per ora): \n\n**Manga**\n- !manga [sito] [nome manga]--> cerca manga\n- !manga_help --> lista siti disponibili\n\n**Overwatch**\n- !ov_eroi [nome eroe] --> cerca eroe\n- !ov_eroi lista --> lista eroi\n\n**Google**\n- !googla [query]--> effettua ricerca su Google\n- !cerca [sito] --> cerca il sito specifico su Google"
        )


lista_eroi = [
    "Ana",
    "Ashe",
    "Baptiste",
    "Bastion",
    "Brigitte",
    "D.VA",
    "Doomfist",
    "Echo",
    "Genji",
    "Hanzo",
    "Junkrat",
    "Lucio",
    "McCree",
    "Mei",
    "Mercy",
    "Moira",
    "Orisa",
    "Pharah",
    "Reaper",
    "Reinhardt",
    "Roadhog",
    "Sigma",
    "Soldato-76",
    "Sombra",
    "Symmetra",
    "Torbjorn",
    "Tracer",
    "Widowmaker",
    "Winston",
    "Wrecking Ball",
    "Zarya",
    "Zenyatta",
]


client.run(TOKEN)
