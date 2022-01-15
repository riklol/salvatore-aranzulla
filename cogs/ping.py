from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current ping."""
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
