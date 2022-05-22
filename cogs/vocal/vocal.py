import asyncio
import re
import urllib.request

import discord
import requests
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
import os

import utils

client = commands.Bot(command_prefix="!")


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # command for bot to join the channel of the user, if the bot has already joined and is in a different it will move to the channel the user is in
    @commands.command(name="join")
    async def join(self, ctx):
        """Join a vocal chat."""

        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        try:
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
        except ClientException:
            pass

        await ctx.send(f"**Joined** {channel}")
        utils.write_logs("Music", "Bot joined voice chat")

    @commands.command(name="leave")
    async def leave(self, ctx):
        """leave a vocal chat."""
        channel = ctx.message.author.voice.channel
        await ctx.voice_client.disconnect()
        await ctx.send(f"**Left** {channel}")
        utils.write_logs("Music", "Bot left voice chat")

    # command to play sound from a youtube URL
    @commands.command(name="play")
    async def play(self, ctx, *, search):
        """Play a song or a playlist."""
        try:
            os.chdir("cogs/vocal")
        except FileNotFoundError:
            pass
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return

        YDL_OPTIONS = {
            "format": "bestaudio",
            "noplaylist": False,
            "quiet": True,
        }
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }

        # takes the urls in the queue file (if it exists)
        if os.path.exists("queue.txt"):
            with open("queue.txt", "r") as qu:
                queue = qu.readlines()
        else:
            qu = open("queue.txt", "w")
            qu.close()

        if search:
            # if there's a link the url is already complete, otherwise takes the first video in the yt search
            if (
                search.startswith("https://")
                or search.startswith("www.")
                or search.startswith("youtube.com")
            ):
                url = search
            else:
                yt_search = search.replace(" ", "+").encode("utf-8")

                html = urllib.request.urlopen(
                    f"https://www.youtube.com/results?search_query={yt_search}"
                )  # nosec (it can't open a local file because the url is the one above, so the linter should not raise a warning)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

                url = f"http://www.youtube.com/watch?v={video_ids[0]}"
    
            # write the song url in the queue file
            with open("queue.txt", "a") as qu:
                qu.write(url+"\n")

        with YoutubeDL(YDL_OPTIONS) as ydl:
            for song in queue:
                url = song.replace("\n", "")
                info = ydl.extract_info(url, download=False)
            #if "entries" in info:
            #    video = info["entries"]
                #queue = []
                #links = []

                # loops entries to grab each video_url
                #for i, item in enumerate(video):
                #    URL = video[i]["url"]
                #    queue.append(URL)
                #    link = video[i]["webpage_url"]
                #    links.append(link)

                # play every song in queue
                #for i, song in enumerate(queue):
                #    while i + 1 <= len(queue):
                #        if not ctx.voice_client.is_playing():
                #            ctx.voice_client.play(
                #                FFmpegPCMAudio(queue[i], **FFMPEG_OPTIONS)
                #            )
                #            await ctx.send(f"**> Now playing:** {links[i]}")
                #            utils.write_logs("Music", f"Played a song ({links[i]})")
                #            i += 1
                #        else:
                #            await asyncio.sleep(0.5)
                #    break

            # if there isn't a playlist
            #else:
                URL = info["url"]
                ctx.voice_client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                await ctx.send(f"**> Now playing:** {url}")
                utils.write_logs("Music", f"Played a song ({url})")

    # skip the current song
    @commands.command(name="skip")
    async def skip(self, ctx):
        """Skip song in playlist."""
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return
        ctx.voice_client.stop()
        await ctx.send("**Skipping...**")
        utils.write_logs("Music", "Skipped a song")

    # pause voice if it' it's playing
    @commands.command(name="pause")
    async def pause(self, ctx):
        """Pause song."""
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return
        ctx.voice_client.pause()
        await ctx.send("**Music paused**")
        utils.write_logs("Music", "Paused a song")

    # resume voice if it is paused
    @commands.command(name="resume")
    async def resume(self, ctx):
        """Resume paused song."""
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return
        ctx.voice_client.resume()
        utils.write_logs("Music", "Resumed a song")

    # stop voice
    @commands.command(name="stop")
    async def stop(self, ctx):
        """Stop song."""
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return
        ctx.voice_client.stop()
        await ctx.send("**Stopping...**")
        utils.write_logs("Music", "Stopped a song")

    # get the song lyrics
    @commands.command(name="lyrics")
    async def lyrics(self, ctx, *, search):
        """Get the song lyrics."""
        if "-" in search:
            artist = search[: search.index("-")]
            title = search[search.index("-") + 1 :]
        else:
            await ctx.send("Metti '-' tra l'artista e la canzone")

        try:
            r = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}")
            lyrics = r.json()
        except:
            pass

        # if the lyrics are longer than 2000 characters split the messages
        # (the max message lenght on discord is 2000 characters)
        try:
            data = str(lyrics["lyrics"])
            if "\n\n" in data:
                data = data.replace("\n\n", "\n")
            if len(data) > 2000:
                data1 = data[: round(len(data) / 2)]
                data2 = data[round(len(data) / 2) :]
                await ctx.send(data1)
                await ctx.send(data2)
            else:
                await ctx.send(data)
        except:
            await ctx.send("Non ho trovato nessun testo :(")
        utils.write_logs("Music", f"Searched lyrics for {artist} - {title}")


    # get the song lyrics
    @commands.command(name="add")
    async def add(self, ctx, *, search):
        """Add a song to the queue."""
        try:
            os.chdir("cogs/vocal")
        except FileNotFoundError:
            pass
        # get the role (used to play a song)
        # if a user doesn't have the DJ role he/she can't play a song
        role = discord.utils.get(ctx.guild.roles, name="DJ")
        role = str(role)
        if "DJ" not in [y.name for y in ctx.message.author.roles]:
            await ctx.send("Qui qualcuno non ha i **PERMESSI** hehe (e non sono io)")
            return

        # if there's a link the url is already complete, otherwise takes the first video in the yt search
        if (
            search.startswith("https://")
            or search.startswith("www.")
            or search.startswith("youtube.com")
        ):
            url = search
        else:
            yt_search = search.replace(" ", "+").encode("utf-8")

            html = urllib.request.urlopen(
                f"https://www.youtube.com/results?search_query={yt_search}"
            )  # nosec (it can't open a local file because the url is the one above, so the linter should not raise a warning)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

            url = f"http://www.youtube.com/watch?v={video_ids[0]}"

        # write the song url in the queue file
        if not os.path.exists("queue.txt"):
            with open("queue.txt", "a") as qu:
                qu.write(url+"\n")
        else:
            with open("queue.txt", "a") as qu:
                qu.write(url+"\n")


def setup(bot: commands.Bot):
    bot.add_cog(Music(bot))
