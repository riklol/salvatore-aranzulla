# bot.py
# potrei ottimizzare tutto con delle funzioni e usando i prefissi x il bot ma al momento non ne ho voglia
# in futuro probabilmente lo farò

import datetime
import os
import random
import threading

import colorama
import discord
from dotenv import load_dotenv

colorama.init()

load_dotenv()

client = discord.Client()

TOKEN = os.environ.get("TOKEN")

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

schedule = []

lista_playlists = {}

print("bot avviato alle: " + datetime.datetime.now().strftime("%H:%M:%S"))


# cancella la schedule a mezzanotte
def mezzanotte(schedule):
    b = 0
    while b == 0:
        if datetime.datetime.now().strftime("%H:%M:%S") == "24:00:00":
            schedule = []
        else:
            pass


# controlla che l'ora segnata = ora corrente
def controllo(schedule):
    a = 0
    while a == 0:
        # controlla per ogni prenotazione se l'ora corrente è = all'ora indicata
        # in caso affermativo cancella l'ora con la prenotazione passata
        for pren in schedule:
            if datetime.datetime.now().strftime("%H:%M") in pren:
                # elimina la prenotazione passata
                schedule.remove(pren)
            else:
                pass


# avvio le funzioni che controllano l'ora in due thread in background
controllo_bg = threading.Thread(target=controllo, daemon=True, args=(schedule,))
controllo_bg.start()

mezzanotte_bg = threading.Thread(target=mezzanotte, daemon=True, args=(schedule,))
mezzanotte_bg.start()


@client.event
async def on_ready():
    print(colorama.Fore.GREEN + "\n{0.user} è online!".format(client))
    gioco_bot = random.choices(lista_giochi_bot)
    # imposta lo stato del bot in modo tale che sembri stia giocando a qualcosa
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

    # cerca su Google (pagina principale)
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

    # cerca su Google (nome sito)
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

    # HELP

    # help comandi
    if message.content.lower().startswith("!comandi"):
        await message.channel.send(
            f"> {love}\n> Ecco i comandi disponibili (le [ ] vanno omesse):\n> \n> **Bot**\n> - `!bot_pic` --> immagine profilo del bot\n> - `!bot_repo` --> visualizza repository GitHub del bot\n> \n> **Google**\n> - `!googla [query]` --> effettua ricerca su Google\n> - `!cerca [sito]` --> cerca il sito specifico su Google\n> \n> **Schedule**\n> - `!prenota [ora]` --> prenotati per un orario\n> - `!annulla_prn [ora]` --> annulla prenotazione\n> - `!schedule` --> visualizza elenco prenotazioni\n> \n> **Registrazione Playlist YouTube**\n> - `!registra_playlist [URL playlist]` --> registra la playlist\n> - `!rimuovi_playlist` --> rimuove la playlist\n> - `!playlist` --> visualizza l'url della playlist salvata\n"
        )
        print(f"{nome} ha visualizzato la lista comandi alle {orario}\n")
        return

    # BOT

    # mostra foto profilo
    if message.content.lower().startswith("!bot_pic"):
        await message.channel.send("Ecco la mia immagine profilo")
        await message.channel.send(file=discord.File("image.png"))
        print(f"{nome} ha visualizzato l'immagine profilo del bot alle {orario}\n")

    # visualizza repository di GitHub
    if message.content.lower().startswith("!bot_repo"):
        await message.channel.send(f"{me} Ecco il mio repository di GitHub")
        await message.channel.send("https://github.com/DanyB0/Shadow-Ruler")
        print(f"{nome} ha visualizzato il repo di GitHub del bot alle {orario}\n")

    # SCHEDULE

    # prenota sessione online
    if message.content.lower().startswith("!prenota "):

        ora = message.content[9:]

        schedule.sort()

        try:
            # esclude il ":"
            controlla_ora_1 = int(ora[-5])
            controlla_ora_2 = int(ora[-4])
            controlla_ora_3 = int(ora[-2:])
        except ValueError:
            await message.channel.send(f"{errore} L'orario deve essere un numero")
            return
        except IndexError:
            await message.channel.send(
                f"{errore} Il formato dell'ora deve essere **[ORE(2 cifre)]:[MINUTI(2 cifre)]**"
            )
            return

        # controlla che i minuti siano minori di 60
        if int(ora[-2:]) > 59:
            await message.channel.send(f"{ahh} Quanti minuti ci sono in 1 ora?")
            return

        # controlla che l'ora sia stata scritta correttamente ([ORA]:[MINUTI])
        if len(ora[-4:]) != 4:
            await message.channel.send(
                f"{errore} Il formato dell'ora non è corretto.\n(deve essere **[ore]:[minuti]**)"
            )
            return

        # controlla che non ci siano orari duplicati
        if f"{nome}: {ora}\n" in schedule:
            await message.channel.send(f"{ahh} ti sei già segnato per quell'orario!")
            return

        # controlla che l'orario per cui ci si vuole prenotare non sia passato
        if int(ora[0:2]) < int(datetime.datetime.now().strftime("%H")):
            await message.channel.send(f"{ahh} {nome} Quest'orario è già passato!")
            return

        # appende il nome e l'ora nel file
        schedule.append(f"{nome}: {ora}\n")
        await message.channel.send(
            f"Ho registrato la prenotazione {ok}\nDigita **!schedule** per visualizzare l'elenco delle prenotazioni."
        )
        print(f"{nome} ha prenotato una sessione alle {ora}\n")
        return schedule

    # rimuovi prenotazione
    if message.content.lower().startswith("!annulla_prn "):

        ora = message.content[13:]

        try:
            # esclude il ":"
            controlla_ora_1 = int(ora[-4])
            controlla_ora_2 = int(ora[-2:])
        except ValueError:
            await message.channel.send(f"{errore} L'orario deve essere un numero")
            return

        if len(ora[-4:]) != 4:
            await message.channel.send(
                f"{errore} Il formato dell'ora non è corretto.\n (deve essere **[ore]:[minuti (con anche secondi)]**)"
            )
            return

        # controlla che l'orario che si vuole rimuovere esista
        if f"{nome}: {ora}\n" not in schedule:
            await message.channel.send(
                f"{errore} {nome} non ti sei mai prenotato per quest'orario!"
            )
            return

        # elimina la prenotazione
        schedule.remove(f"{nome}: {ora}\n")

        # riscrive nel file le altre prenotazioni
        for prenotazione in schedule:
            schedule.append(prenotazione)
        await message.channel.send(
            f"{ok} Prenotazione rimossa.\nDigita **!schedule** per visualizzare l'elenco delle prenotazioni."
        )
        print(f"{nome} ha annullato una sessione alle {ora}\n")
        return schedule

    # mostra schedule
    if message.content.lower().startswith("!schedule"):
        if schedule == []:
            await message.channel.send(
                "Attualmente non ci sono prenotazioni.\nPer prenotarti per un orario digita **!prenota [ora]**"
            )
        schedule.sort()
        try:
            schedule.remove("\n")
        except ValueError:
            pass
        for prenotazione in schedule:
            await message.channel.send(f"> {prenotazione}")
        print(f"{nome} ha visualizzato la schedule alle {orario}\n")
        return

    # PLAYLIST
    # registra la playlist dell'utente
    if message.content.lower().startswith("!registra_playlist "):
        playlist = message.content[19:]
        yt = message.content[19:42]
        if yt != "https://www.youtube.com":
            await message.channel.send(f"{errore} L'URL non è corretto")
            return
        else:
            lista_playlists[nome] = playlist
            await message.channel.send(f"{ok} La playlist è stata registrata")
            return

    # rimuove la playlist dell'utente
    if message.content.lower().startswith("!rimuovi_playlist"):
        try:
            lista_playlists = lista_playlists.pop(nome, f"{nome} non in dict")
            await message.channel.send(f"{ok} La playlist è stata eliminata")
            return
        except KeyError:
            await message.channel.send(
                f"{errore} Non hai mai registrato una playlist! Digita **!registra_playlist** per registrarne una"
            )
            return

    # visualizza la mia playlist dell'utente
    if message.content.lower().startswith("!playlist"):
        try:
            play = lista_playlists[nome]
            await message.channel.send(f"Ecco il link della playlist di {nome} {succo}")
            await message.channel.send(play)
            return
        except KeyError:
            await message.channel.send(
                f"{errore} Non hai mai registrato una playlist! Digita **!registra_playlist** per registrarne una"
            )
            return


client.run(TOKEN)
