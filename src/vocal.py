import re
import urllib.request

import discord
from discord import FFmpegPCMAudio, TextChannel
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix="!")


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    # command to play sound from a youtube URL
    @commands.command()
    async def play(self, ctx, search):
        YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }

        yt_search = search.replace(" ", "+")

        html = urllib.request.urlopen(
            f"https://www.youtube.com/results?search_query={yt_search}"
        )
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        url = f"http://www.youtube.com/watch?v={video_ids[0]}"

        voice = discord.voice_client.VoiceClient

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info["url"]

        ctx.voice_client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

        await ctx.send("**Bot is playing:\n**")
        await ctx.send(url)

    # command to resume voice if it is paused
    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()

    # command to pause voice if it is playing
    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("**Music paused**")

    # command to stop voice
    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("**Stopping...**")


def setup(bot: commands.Bot):
    bot.add_cog(Music(bot))
