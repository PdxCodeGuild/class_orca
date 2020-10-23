import discord
from discord.ext import commands
import pandas

client = commands.Bot(command_prefix='!')

#prints a message when the bot comes online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    general_channel = client.get_channel(768544471246962699)
    await general_channel.send('Hello, world!')


@client.event
async def on_message(message):
    #makes the bot respond when someone types a message that starts with hello
    if message.content.startswith('hello'):
        await message.channel.send('Hello! I am a bot.')
    if message.content == "Append":
    #saves data into a csv file
        df = pandas.read_csv('/Users/makav/PDX/class_orca/class_orca/code/peterlee/discordbot/output.csv', index_col=0)
        df = df.append({'A': 'Append this message'}, ignore_index=True)
        df.to_csv('/Users/makav/PDX/class_orca/class_orca/code/peterlee/discordbot/output.csv')


#brings bot onto discord server by using its token
client.run('')