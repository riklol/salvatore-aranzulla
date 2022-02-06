from discord.ext import commands

client = commands.Bot(command_prefix="!")


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="credits")
    async def credits(self, ctx: commands.Context):
        """Show the credits."""
        await ctx.send(
            "> **Thanks to:**\n> DanyB0#6791 https://cdn.discordapp.com/emojis/850099185993777179.gif?size=48&quality=lossless\n> alesar03#4718 https://cdn.discordapp.com/emojis/930873952576864297.gif?size=48&quality=lossless"
        )

        
def setup(bot: commands.Bot):
    bot.add_cog(Credits(bot))
