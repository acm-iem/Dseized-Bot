import discord
import os

from discord.ext import commands, tasks
from random import choice
import discord
from discord.ext import commands
import os
import shutil
from os import system


from discord.utils import get
import time
from discord.ext.commands import check

# Read the Data files and store them in a variable
TokenFile = open("./data/Token.txt", "r") # Make sure to paste the token in the txt file
TOKEN = TokenFile.read() 

OWNERID = 254324351296339968

# Define "bot"
bot = commands.Bot(command_prefix = "-", case_insensitive=True)
status = ['-play', 'Singing']
# Let us Know when the bot is ready and has started
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with the homies | -info"))
    print("Bot is ready")


#@tasks.loop(seconds=8)
#async def change_status():
#    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice(status)))
    #activity=discord.Activity(type=discord.ActivityType.watching, name="Your Server")


@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round(bot.latency*1000, 2)} ms!')

def in_voice_channel():  # check to make sure ctx.author.voice.channel exists
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel
    return check(predicate)

@in_voice_channel()
@bot.command()
async def move(ctx, *, channel : discord.VoiceChannel):
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)

# A simple and small ERROR handler
@bot.event 
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

# Load command to manage our "Cogs" or extensions
@bot.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Unload command to manage our "Cogs" or extensions
@bot.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Reload command to manage our "Cogs" or extensions
@bot.command(name = "reload")
async def reload_(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!") 
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception

#@bot.command()
#async def ping(ctx):
#    await ctx.send(f'My ping is {round(bot.latency*1000, 2)} ms!')
            
# Run our bot

bot.run(str(TOKEN)) # Make sure you paste the CORRECT token in the "./data/Token.txt" file
