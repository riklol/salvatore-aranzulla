""" NHENTAI COMMANDS """

import random

import requests
from discord.ext import commands
from discord.ext.commands import Bot
from hentai import Format, Hentai, Utils

import src

bot = Bot("!")


class Nhentai(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="idhent")
    async def nhid(self, ctx: commands.Context, *, doujin_id):
        """Get the hentai from its ID."""
        server, channel, user = get_info(ctx)

        # Check that the doujin exists and the ID is a number
        try:
            doujin_id = int(doujin_id)
            doujin = Hentai(doujin_id)
        except ValueError:
            await ctx.send("The ID must be a number")
        except requests.exceptions.HTTPError:
            await ctx.send("The doujin does not exist")

        # Send the doujin link
        await ctx.send(f"https://nhentai.net/g/{doujin_id}")
        src.write_logs(
            "Weeb", f"Sent {doujin_id} doujin link (https://nhentai.net/g/{doujin_id})"
        )

    @commands.command(name="rhent")
    async def rhent(self, ctx: commands.Context):
        """Get a random hentai."""
        server, channel, user = get_info(ctx)

        # Get a randon ID
        rand_hnt = Utils.get_random_id()

        doujin = Hentai(rand_hnt)

        # Send the doujin link
        await ctx.send(f"https://nhentai.net/g/{doujin.id}")
        src.write_logs(
            channel, 
            "Weeb",
            f"Randomly sent {doujin_id} doujin link (https://nhentai.net/g/{doujin_id})",
        )


# get the server and channel info
def get_info(ctx):
    guild_id = ctx.guild.id
    server = bot.get_guild(guild_id)
    channel_id = ctx.channel.id
    channel = bot.get_channel(channel_id)
    return server, channel, ctx.author.name


def setup(bot: commands.Bot):
    bot.add_cog(Nhentai(bot))
