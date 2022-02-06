from discord.ext import commands

client = commands.Bot(command_prefix="!")


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="credits")
    async def credits(self, ctx: commands.Context):
        """Show the credits."""
        danyb0, alesar = get_emojis()
        await ctx.send(
            f"> **Thanks to:**\n> DanyB0#6791 {danyb0}\n> alesar03#4718 {alesar}"
        )


def get_emojis():
    danyb0 = client.get_emoji(850099185993777179)
    alesar = client.get_emoji(850099186003083304)
    return danyb0, alesar


def setup(bot: commands.Bot):
    bot.add_cog(Credits(bot))
