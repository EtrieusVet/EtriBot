### Imports ###

import time
import discord
from discord.ext import commands
import os
import pretty_help
from pretty_help import Navigation, PrettyHelp

### Variables ###

#TESTSADSDADSD
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='!', intents=intents,
                      help_command=PrettyHelp(color=discord.Color.dark_gray(), active_time=(float('inf'))))
lol = "lol"

### Commands ###


@client.command(hidden=True)
async def load_132(ctx, extension, amount=1):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit=amount)


@client.command(hidden=True)
async def unload_132(ctx, extension, amount=1):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.purge(limit=amount)


### Events ###


@client.event
async def on_ready():
    print("{0.user} has awoken!".format(client))
    await client.change_presence(activity=discord.Game('with Etrieus'))


for filename in os.listdir('./cogs'):

    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODA1MDM1OTU0ODg3ODUyMDUy.YBVCKA.2vmW4s8nm_gthYjr7350Pcy_CVk')
