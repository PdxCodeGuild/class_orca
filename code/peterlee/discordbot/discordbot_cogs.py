import os
from discord.ext import commands
from settings import *

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzY4NTQ1MDY4MjgxNjI2NjQ1.X5CBXw.2x8FnPddVbBPfEGqqsKEh5AC5gg')