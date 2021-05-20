import json
import discord
from discord.ext import commands

def get_prefix(client, message):
    with open('cogs/jfiles/servers.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

def get_welcome(client, message):
    with open('cogs/jfiles/servers.json', 'r') as f:
        welcomes = json.load(f)

    return welcomes[str(message.guild.id)]


class Customization(commands.Cog, description="Commands that will customize the server."):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['prefix'], brief="Changes the server prefix.")
    @commands.has_permissions(manage_guild = True)
    async def Prefix(self, ctx, prefix):

        with open('cogs/jfiles/servers.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)]['Prefix'] = prefix

        with open('cogs/jfiles/servers.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'The prefix for the server is now {prefix}.')

    @Prefix.error
    async def prefix_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill out the required argument.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permissions to use this command.")


    @commands.command(aliases=['setwelcome'])
    @commands.has_permissions(manage_guild = True)
    async def SetWelcome(self, ctx, channel: discord.TextChannel):


        with open('cogs/jfiles/servers.json', 'r') as f:

            welcomes = json.load(f)

        welcomes[str(ctx.guild.id)]['Welcome'] = str(channel.id)

        with open('cogs/jfiles/servers.json', 'w') as f:
            json.dump(welcomes, f, indent=4)

        await ctx.send(f"The welcome channel for the server is now {channel}.")

def setup(client):
    client.add_cog(Customization(client))