from discord.ext import commands

client = commands.Bot(command_prefix="!")


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="credits")
    async def credits(self, ctx: commands.Context):
        """Show the credits."""
        danyb0 = "<a:whyyyyyy:850099185993777179>"
        await ctx.send(f"> **Thanks to:**\n> DanyB0#6791  {danyb0}\n> alesar03#4718")


def setup(bot: commands.Bot):
    bot.add_cog(Credits(bot))
