import aiohttp
import discord
from discord.ext import commands

class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:
                data = await r.json()
                embed = discord.Embed(title="Cat")
                embed.set_image(url=data['file'])
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Image(bot))