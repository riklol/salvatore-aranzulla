import asyncio
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
    @commands.command(name="join")
    async def join(self, ctx):
        """Join a vocal chat."""
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command(name="leave")
    async def leave(self, ctx):
        """leave a vocal chat."""
        await ctx.voice_client.disconnect()

    # command to play sound from a youtube URL
    @commands.command(name="play")
    async def play(self, ctx, *, search):
        """Play a song or a playlist."""
        YDL_OPTIONS = {
            "format": "bestaudio",
            "noplaylist": False,
            "quiet": True,
        }
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }

        # if there's a link the url is already complete, otherwise takes the first video in the yt search
        if (
            search.startswith("https://")
            or search.startswith("www.")
            or search.startswith("youtube.com")
        ):
            url = search
        else:
            yt_search = search.replace(" ", "+")

            html = urllib.request.urlopen(
                f"https://www.youtube.com/results?search_query={yt_search}"
            ) # nosec (it can't open a local file because the url is the one above, so the linter should not raise a warning)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

            print(f"https://www.youtube.com/results?search_query={yt_search}")
            print(video_ids)

            url = f"http://www.youtube.com/watch?v={video_ids[0]}"

        voice = discord.voice_client.VoiceClient

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            if "entries" in info:
                video = info["entries"]
                queue = []
                links = []

                # loops entries to grab each video_url
                for i, item in enumerate(video):
                    URL = video[i]["url"]
                    queue.append(URL)
                    link = video[i]["webpage_url"]
                    links.append(link)

                # play every song in queue
                for i in range(len(queue)):
                    while i + 1 <= len(queue):
                        if not ctx.voice_client.is_playing():
                            print(f"\n\n\n{i}")
                            print(f"\n{queue[i]}\n\n\n")
                            ctx.voice_client.play(
                                FFmpegPCMAudio(queue[i], **FFMPEG_OPTIONS)
                            )
                            await ctx.send("**Now playing:\n**")
                            await ctx.send(links[i])
                            i += 1
                        else:
                            await asyncio.sleep(0.5)
                    break

            # if there isn't a playlist
            else:
                URL = info["url"]
                ctx.voice_client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                await ctx.send("**Now playing:\n**")
                await ctx.send(url)

    # skip the current song
    @commands.command(name="skip")
    async def skip(self, ctx):
        """Skip song in playlist."""
        ctx.voice_client.stop()
        await ctx.send("**Skipping...**")

    # pause voice if it' i's playing
    @commands.command(name="pause")
    async def pause(self, ctx):
        """Pause song."""
        ctx.voice_client.pause()
        await ctx.send("**Music paused**")

    # resume voice if it is paused
    @commands.command(name="resume")
    async def resume(self, ctx):
        """Resume paused song."""
        ctx.voice_client.resume()

    # stop voice
    @commands.command(name="stop")
    async def stop(self, ctx):
        """Stop song."""
        ctx.voice_client.stop()
        await ctx.send("**Stopping...**")


def setup(bot: commands.Bot):
    bot.add_cog(Music(bot))
