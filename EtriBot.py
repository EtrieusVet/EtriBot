### Imports ###


import time
import discord
from discord.ext import commands
import os
import pretty_help
from pretty_help import Navigation, PrettyHelp
import asyncio

### Variables ###


command_prefix = "!"

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=f'{command_prefix}', intents=intents,
                      help_command=PrettyHelp(color=discord.Color.dark_gray(), active_time=(float('inf'))))

@client.command(brief="Changes the command prefix.")
@commands.has_any_role("Ze Creator")
async def Prefix(ctx, prefix):

    command_prefix = prefix
    await ctx.send(f"Command prefix is now {prefix}")
    await ctx.send(f'{command_prefix}')

### Events ###

@client.event
async def on_ready():
    print("{0.user} has awoken!".format(client))
    await client.change_presence(activity=discord.Game('with fire'))

for filename in os.listdir('./cogs'):

    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODA1MDM1OTU0ODg3ODUyMDUy.YBVCKA.QT3bdnDWxycZoifs9mt3T6qYwiU')
