# bot.py
# potrei ottimizzare tutto con delle funzioni ma al momento non ne ho voglia
# in futuro probabilmente lo farò
import discord
import datetime
import random
import os


TOKEN = "ODM0NDU5NDU5NDA0NDMxNDkw.YIBM7g.wTCbevovCVNDU8QqVcj4gmYYJ0c"

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} è online!".format(client))


@client.event
async def on_message(message):

    # RICKROLL

    # no rickroll
    if message.content.startswith("!play https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")
        print(
            "tentativo di rickroll alle " + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # no rickroll
    elif message.content.startswith("https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        await message.channel.send("Non mi RickRollerai hahaha")
        print(
            "tentativo di rickroll alle " + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # GOOGLE

    # cerca su Google (pagina principale)
    elif message.content.startswith("!googla "):
        query = message.content[8:]
        if "." in query:
            await message.channel.send("Forse il comando che vuoi usare è **!cerca**")
            return
        query = query.replace(" ", "+")
        await message.channel.send(f"https://google.com/search?q={query.lower()}")
        print(
            f"ricerca generica su Google ({query}) alle "
            + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # cerca su Google (nome sito)
    elif message.content.startswith("!cerca "):
        query = message.content[7:]
        if "." not in query:
            await message.channel.send("Forse il comando che vuoi usare è **!googla**")
            return
        query = query.replace(" ", "")
        url = "https://"
        await message.channel.send(url + query.lower())
        print(
            f"ricerca specifica su Google ({query}) alle "
            + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # MANGA

    # cerca manga
    elif message.content.startswith("!manga "):

        pre_query = message.content[7:9]
        query = message.content[10:]
        query = query.replace(" ", "-")

        # cerca su AsuraScans
        if pre_query == "as":
            sito = "AsuraScans"
            url = "https://www.asurascans.com/comics/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query} in {sito}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )
            print(
                f"ricerca manga ({query}) su AsuraScans alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

        # cerca su LeviatanScans
        elif pre_query == "lv":
            sito = "LeviatanScans"
            url = "https://leviatanscans.com/lcomic/manga/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query} in {sito}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )
            print(
                f"ricerca manga ({query}) su LeviatanScans alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

        # cerca su WebtoonScan
        elif pre_query == "ws":
            sito = "WebtoonScan"
            url = "https://webtoonscan.com/manhwa/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query} in {sito}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )
            print(
                f"ricerca manga su ({query}) WebtoonScan alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

        # cerca su IsekaiScan
        elif pre_query == "is":
            sito = "IsekaiScan"
            url = "https://isekaiscan.com/manga/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query} in {sito}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )
            print(
                f"ricerca manga ({query}) su WebtoonScan alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

        # cerca su MangaSekai
        elif pre_query == "ms":
            sito = "MangaSekai"
            url = "https://mangasekai.altervista.org/manga/"
            await message.channel.send(
                f"Ecco cosa ho trovato per {query} in {sito}: " + (url + query.lower())
            )
            await message.channel.send(
                "Se il manga cercato non è disponibile consiglio di cambiare sito"
            )
            await message.channel.send(
                "per vedere una lista dei siti disponibili digita **" "!manga_help" "**"
            )
            print(
                f"ricerca manga ({query}) su WebtoonScan alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

    # lista manga
    elif message.content.startswith("!manga_help"):
        await message.channel.send("Ecco i siti disponibili:")
        await message.channel.send("AsuraScans (**as**)")
        await message.channel.send("LeviatanScans (**lv**)")
        await message.channel.send("WebtoonScan (**ws**)")
        await message.channel.send("IsekaiScan (**is**)")
        await message.channel.send("MangaSekai (**ms**)")
        print("aiuto manga alle " + datetime.datetime.now().strftime("%H:%M:%S"))
        return

    # OVERWATCH

    # eroi overwatch
    elif message.content.startswith("!ov_eroi "):
        query = message.content[9:]

        if query == "lista":
            await message.channel.send(
                "Ecco la lista degli eroi di Overwatch (ci metterò un po' e potresti vedere degli stickers):"
            )

            for eroe in lista_eroi:
                await message.channel.send(eroe)
            print(
                "lista eroi Overwatch alle "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            return

        url = "https://playoverwatch.com/it-it/heroes/"
        await message.channel.send(
            f"Ecco cosa ho trovato per {query}: " + (url + query.lower())
        )
        print(
            f"ricerca eroe ({query}) su Overwatch alle "
            + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # HELP

    # help comandi
    elif message.content.startswith("!comandi"):
        await message.channel.send(
            "Ecco i comandi disponibili (per ora): \n\n**Bot**\n- !bot_pic --> immagine profilo del bot\n- !bot_imgs [topic] [n] --> mostra n immagini casuali (max 9) relative al topic scelto\n- !bot_imgs list --> lista topic disponibili\n\n**Manga**\n- !manga [sito] [nome manga] --> cerca manga\n- !manga_help --> lista siti disponibili\n\n**Overwatch**\n- !ov_eroi [nome eroe] --> cerca eroe\n- !ov_eroi lista --> lista eroi\n\n**Google**\n- !googla [query] --> effettua ricerca su Google\n- !cerca [sito] --> cerca il sito specifico su Google"
        )
        print(
            "visualizzata lista comandi alle "
            + datetime.datetime.now().strftime("%H:%M:%S")
        )
        return

    # IMMAGINI

    # mostra foto profilo
    elif message.content.startswith("!bot_pic"):
        await message.channel.send("Ecco la mia immagine profilo")
        await message.channel.send(file=discord.File("image.png"))

    # mostra immagine casuale relativa ad un topic
    elif message.content.startswith("!bot_imgs "):
        topic_num = message.content[10:]
        topic_num = topic_num.replace(" ", "")
        # numero immagini da visualizzare
        numero = topic_num[-1]
        if not topic_num[-2:] in lista_numeri_img:
            await message.channel.send("Posso inviare al massimo 9 immagini")
            return
        # topic da visualizzare
        topic = topic_num[:-1]
        # lista con i nomi dei file nella cartella del topic
        list_file = os.listdir(f"imgs/{topic.lower()}")
        # immagine casuale
        n = random.choices(list_file, k=int(numero))
        # cambia cartella nel topic e invia le foto nella lista
        for i in range(len(n)):
            await message.channel.send(
                file=discord.File(f"imgs/{topic.lower()}/{n[i]}")
            )
        print(f"inviate {int(numero)} foto di {topic}")


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

lista_numeri_img = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8" "h9"]


client.run(TOKEN)
