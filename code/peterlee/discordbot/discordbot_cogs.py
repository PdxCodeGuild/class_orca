from discord.ext import commands

bot = commands.Bot(command_prefix="!")

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello! I am a bot.")

bot.add_cog(Test(bot))

bot.run('NzY4NTQ1MDY4MjgxNjI2NjQ1.X5CBXw.62ULSbChSrOJJPI2bS04Jo1Qsf4')