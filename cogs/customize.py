import json
import time
import discord
from discord.ext import commands
import os
import pretty_help
from pretty_help import Navigation, PrettyHelp
import asyncio

class Customization(commands.Cog, description="Commands that will customize the server."):

    def __init__(self, client):
        self.client = client

    def get_prefix(client, message):
        with open('cogs/jfiles/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

    @commands.command(aliases=['prefix'], brief="Changes the server prefix.")
    async def Prefix(ctx, prefix):

        with open('cogs/jfiles/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('cogs/jfiles/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'The prefix for the server is now {prefix}')

def setup(client):
    client.add_cog(Customization(client))