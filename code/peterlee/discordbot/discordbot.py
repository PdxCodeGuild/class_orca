import discord
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))
        general_channel = client.get_channel(770625101141508097)
        await general_channel.send('Hello, world!')

    async def on_message(self, message):
        #ignores bot messages
        if message.author == self.user:
            return
    


client = MyClient()
client.run('NzY4NTQ1MDY4MjgxNjI2NjQ1.X5CBXw.2x8FnPddVbBPfEGqqsKEh5AC5gg')