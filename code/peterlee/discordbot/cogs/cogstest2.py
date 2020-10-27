from discord.ext import commands

class Test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello! I am a bot.")


def setup(bot):
    bot.add_cog(Test2(bot))