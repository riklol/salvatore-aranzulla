import discord
from discord.ext import commands

import src

client = commands.Bot(command_prefix="!")


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="credits")
    async def credits(self, ctx: commands.Context):
        """Show the credits."""
        danyb0 = "<a:whyyyyyy:850099185993777179>"
        embed = discord.Embed(
            title="Thanks to",
            url="https://github.com/DanyB0/salvatore-aranzulla",
            color=discord.Color.blue(),
        )
        embed.add_field(name="DanyB0#6791", value="lol")
        embed.add_field(name="alesar03#4718", value="lmao")
        await ctx.send(embed=embed)
        src.write_logs("Weeb", "Sent credits")


def setup(bot: commands.Bot):
    bot.add_cog(Credits(bot))
