from discord.ext import commands, tasks
from discord.ext.commands import Bot
import discord
import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import youtube_dl

import urllib.request
import re
import ffmpeg


bot = Bot("!")

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}




class Vocal(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx: commands.Context):
        """Join a vocal chat."""
        server, channel, user = get_info(ctx)
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel.")

    @commands.command(name="leave")
    async def leave(self, ctx: commands.Context):
        """Leave a vocal chat."""
        server, channel, user = get_info(ctx)
        await ctx.voice_client.disconnect()

    
    @commands.command(name="play")
    async def play(self, ctx: commands.Context, *, search):

        search = search.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

            audio_source = discord.FFmpegPCMAudio('vuvuzela.mp3')
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)
    

    @bot.command(name='pause', help='This command pauses the song')
    async def pause(ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
        
    @bot.command(name='resume', help='Resumes the song')
    async def resume(ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")
    
    @bot.command(name='stop', help='Stops the song')
    async def stop(ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")


'''
    @bot.command(name='play', help='To play song')
    async def play(self, ctx: commands.Context):

        print(f"\n\n\n{bot.voice_clients}\n\n\n")


        channel = ctx.message.author.voice.channel
        print(f"\n\n\n{channel}\n\n\n")
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        print(f"\n\n\n{voice}\n\n\n")
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        search = "alan walker alone"
        search = search.replace(" ", "+")

        

        
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

        song = pafy.new(video_ids[0])  # creates a new pafy object

        audio = song.getbestaudio()  # gets an audio source

        source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use

        voice.play(source)  # play the source
'''






# get the server and channel info
def get_info(ctx):
    guild_id = ctx.guild.id
    server = bot.get_guild(guild_id)
    channel_id = ctx.channel.id
    channel = bot.get_channel(channel_id)
    return server, channel, ctx.author.name


def setup(bot: commands.Bot):
    bot.add_cog(Vocal(bot))
