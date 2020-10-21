import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello! I am a bot.')

client.run('NzY4NTQ1MDY4MjgxNjI2NjQ1.X5CBXw.Cmd9BJ1vv-lAgO5OfYErUO5RvLc')