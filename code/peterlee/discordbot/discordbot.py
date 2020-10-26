import discord
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))
        general_channel = client.get_channel(768544471246962699)
        await general_channel.send('Hello, world!')

    async def on_message(self, message):
        #ignores bot messages
        if message.author.bot:
            return


client = MyClient()
#brings bot onto discord server by using its token
client.run('NzY4NTQ1MDY4MjgxNjI2NjQ1.X5CBXw.62ULSbChSrOJJPI2bS04Jo1Qsf4')