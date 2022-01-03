import datetime
import json
import os
import random

import colorama
import discord
import requests
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

rock_paper = ["carta", "forbice", "sasso"]

# get the periodic table as json
# table_req = requests.get("https://neelpatel05.pythonanywhere.com/").text
# table = json.loads(table_req)


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

    msg = message.content
    if " " in msg:
        msg = msg.replace(" ", "")

    orario = datetime.datetime.now().strftime("%H:%M:%S")

    # emojis
    errore = client.get_emoji(833779980294029314)
    ahh = client.get_emoji(829011307957190767)
    party = client.get_emoji(829011307604869140)
    ok = client.get_emoji(837074839318822943)
    me = client.get_emoji(837074855735066684)
    love = client.get_emoji(837074776928288779)
    succo = client.get_emoji(829011307750883369)
    danyb0 = client.get_emoji(850099185993777179)
    alesar = client.get_emoji(850099186003083304)

    message_list = []

    # super easter egg
    numero_rand = random.randint(1, 10000)
    if numero_rand == 13:
        await message.channel.send(
            f"{party} Complimenti {nome}! Questo è un messaggio casuale con una probabilità dello 0,01% {party}!",
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
        "dQw4w9WgXcQ" in msg
        or "oHg5SJYRHA0" in msg
        or "j5a0jTc9S10" in msg
        or "never gonna give you up" in msg.lower()
    ):
        await message.delete()
        await message.channel.send("Non mi RickRollerai hahaha")
        await message.channel.send(file=discord.File("imgs/ET.jpg"))
        print(f"{nome} ha effettuato un tentativo di rickroll alle {orario}\n")
        return

    # GOOGLE
    # search on Google (query)
    if msg.lower().startswith("!googla "):
        query = msg[8:]
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
    if msg.lower().startswith("!cerca "):
        query = msg[7:]
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
    if msg.lower().startswith("!bot_pic"):
        await message.channel.send("Ecco la mia immagine profilo")
        await message.channel.send(file=discord.File("image.png"))
        print(f"{nome} ha visualizzato l'immagine profilo del bot alle {orario}\n")

    # view GitHub repo
    if msg.lower().startswith("!bot_repo"):
        await message.channel.send(f"{me} Ecco il mio repository di GitHub")
        await message.channel.send("https://github.com/DanyB0/Shadow-Ruler")
        print(f"{nome} ha visualizzato il repo di GitHub del bot alle {orario}\n")

    # GAMES
    # coin flip
    if msg.lower().startswith("!flip"):
        side = random.choices(coin_flip)[0]
        print(
            f"Esito: {side} (se il messaggio dopo è diverso è stata usata l'opzione --hck)"
        )
        # if the option --hck is used switch the results
        if msg.lower()[6:] == "--hck":
            if side == "testa":
                side = "croce"
            else:
                side = "testa"
        await message.channel.send(f"{succo} **{side}**")
        print(f"{nome} ha lanciato una moneta con esito {side} alle {orario}\n")
        return

    # rock paper scissors
    if msg.lower().startswith("!rps"):
        r_p_s_b = random.choices(rock_paper)[0]
        r_p_s_u = msg.lower()[4:]
        print(r_p_s_u)
        if r_p_s_u not in rock_paper:
            await message.channel.send(
                f"{errore} Devi scegliere un'opzione tra **carta, forbice, sasso**"
            )
        print(f"Scelta carta forbice sasso del bot: {r_p_s_b}")
        print(f"Scelta carta forbice sasso di {nome}: {r_p_s_u}")

        # check who wins
        if r_p_s_b == "carta":
            if r_p_s_u == "carta":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **PAREGGIO**"
                )
                print("Esito partita: PAREGGIO\n")
            if r_p_s_u == "forbice":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **{nome} VINCE!**"
                )
                print(f"Esito partita: {nome} VINCE!\n")
            if r_p_s_u == "sasso":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **IL BOT VINCE!**"
                )
                print("Esito partita: IL BOT VINCE!\n")

        if r_p_s_b == "forbice":
            if r_p_s_u == "carta":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **IL BOT VINCE!**"
                )
                print("Esito partita: IL BOT VINCE!\n")
            if r_p_s_u == "forbice":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **PAREGGIO**"
                )
                print("Esito partita: PAREGGIO\n")
            if r_p_s_u == "sasso":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **{nome} VINCE!**"
                )
                print(f"Esito partita: {nome} VINCE!\n")

        if r_p_s_b == "sasso":
            if r_p_s_u == "carta":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **{nome} VINCE!**"
                )
                print(f"Esito partita: {nome} VINCE!\n")
            if r_p_s_u == "forbice":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **IL BOT VINCE!**"
                )
                print("Esito partita: IL BOT VINCE!\n")
            if r_p_s_u == "sasso":
                await message.channel.send(
                    f"{succo}\n{nome}: **{r_p_s_u}**\nBot: **{r_p_s_b}**\nEsito: **PAREGGIO**"
                )
                print("Esito partita: PAREGGIO\n")
        return

    # UTILITY
    # (display neko image)
    if msg.lower().startswith("!neko"):
        # take the neko image
        url_neko_pic = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
        await message.channel.send(f"{url_neko_pic}")
        print(f"{nome} ha visualizzato una neko alle {orario}\n")
        return

    # (display image from rule34)
    if msg.lower().startswith("!r34"):
        img_list = []
        # take the tag image
        tag = msg.lower()[4:]
        teg = tag.replace(" ", "")
        if not tag:
            try:
                # take all the images with the given tag
                r = requests.get(
                    f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1"
                ).json()
            except json.decoder.JSONDecodeError:
                await message.channel.send(f"{errore} Il tag non esiste!")
                return
            # append the links to the images int the list
            for elem in r:
                img_list.append(elem["file_url"])
            # casual number
            n = random.randint(0, len(r))
            await message.channel.send(f"{img_list[n]}")
            print(
                f"{nome} ha visualizzato un'immagine da r34 con tag '{tag}' alle {orario}\n"
            )
            return
        # if the user specify a tag
        try:
            # take all the images with the given tag
            r = requests.get(
                f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1"
            ).json()
        except json.decoder.JSONDecodeError:
            await message.channel.send(f"{errore} Il tag non esiste!")
            return
        # append the links to the images int the list
        for elem in r:
            img_list.append(elem["file_url"])
        # casual number
        n = random.randint(0, len(r))
        await message.channel.send(f"{img_list[n]}")
        print(
            f"{nome} ha visualizzato un'immagine da r34 con tag '{tag}' alle {orario}\n"
        )
        return

    # # periodic table
    # if msg.lower().startswith("!elem"):
    #     symbol = msg[6:8].capitalize()
    #     # replace the white space with anything
    #     if " " in symbol:
    #         symbol = symbol.replace(" ", "")
    #     # search trough the table the element
    #     for element_dict in table:
    #         if symbol in element_dict.values():
    #             # display the caratheristics
    #             for attribute in element_dict:
    #                 message_list.append(
    #                     f"**{attribute}**: *{element_dict.get(attribute)}*\n"
    #                 )
    #         # format the message
    #         string = ("> ").join(message_list)
    #     # error messsage
    #     if message_list == []:
    #         string = f"{errore} Non ci sono elementi con quel simbolo!"
    #     # send the message
    #     await message.channel.send(f"> {string}")
    #     print(f"{nome} ha cercato l'elemento {symbol} alle {orario}\n")
    #     return

    # CREDITS
    # show credits
    if msg.lower().startswith("!credits"):
        await message.channel.send(
            f"> **Thanks to:**\n> DanyB0  {danyb0}\n> alesar03 {alesar}"
        )
        return

    # HELP
    # help
    if msg.lower().startswith("!comandi"):
        await message.channel.send(
            f"> {succo}\n> **Ecco i comandi disponibili (le [ ] vanno omesse)**:\n> \n> **Bot**\n> - `!bot_repo` --> visualizza repository GitHub del bot\n> \n> **Google**\n> - `!googla [query]` --> effettua ricerca su Google\n> - `!cerca [sito]` --> cerca il sito specifico su Google\n> \n> **Giochi**\n> - `!flip [--hck]` --> testa o croce (--hck inverte l'estrazione)\n> - `!rps [carta/forbice/sasso]` --> giochi a carta, forbice, sasso vs il bot\n> \n> **Utility**\n> - `!neko` --> neko image ;)\n> - feature nascosta (34)\n> \n> **Crediti**\n> - `!credits` --> mostra i riconoscimenti"
        )
        print(f"{nome} ha visualizzato la lista comandi alle {orario}\n")
        return


client.run(TOKEN)
