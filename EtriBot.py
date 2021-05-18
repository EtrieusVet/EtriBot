### Imports ###

import json
import time
import discord
from discord.ext import commands
import os
import pretty_help
from pretty_help import Navigation, PrettyHelp
import asyncio

### Variables ###

def get_prefix(client, message):

    with open('cogs/jfiles/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=get_prefix, intents=intents,
                      help_command=PrettyHelp(color=discord.Color.dark_gray(), active_time=(float('inf'))))

### Events ###

@client.event
async def on_ready():

    print("{0.user} has awoken!".format(client))
    await client.change_presence(activity=discord.Game('with gим∆|Lxy.'))

@client.event
async def on_guild_join(guild):

    with open('cogs/jfiles/prefixes.json', 'r') as f:

        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('cogs/jfiles/prefixes.json', 'w') as f:

        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):

    with open('cogs/jfiles/prefixes.json', 'r') as f:

        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('cogs/jfiles/prefixes.json', 'w') as f:

        json.dump(prefixes, f, indent=4)



for filename in os.listdir('./cogs'):

    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODA1MDM1OTU0ODg3ODUyMDUy.YBVCKA.SAj0cYp4hMoTYWll8LTUhGay2H4')
