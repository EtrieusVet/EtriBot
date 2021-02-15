### Imports ###

import discord
from discord.ext import commands


class SCommands(commands.Cog, description="Commands only used by specific roles."):

    def __init__(self, client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready():
            print("SCommands is online!")

        @commands.command(aliases=["d"])
        @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')
        async def clear(self, ctx, amount=5):
            await ctx.channel.purge(limit=amount)


