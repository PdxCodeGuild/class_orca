from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Rolls a random number between 1 and 6")
    async def roll(self, ctx):
        n = random.randrange(1, 7)
        await ctx.send(n)


def setup(bot):
    bot.add_cog(Roll(bot))