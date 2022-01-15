from discord.ext import commands


class Hlp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hlp")
    async def hlp(self, ctx: commands.Context):
        """print commands"""
        await ctx.send("never gonna give you up... ♪♫")


def setup(bot: commands.Bot):
    bot.add_cog(Hlp(bot))
