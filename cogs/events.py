### Imports ###

from better_profanity import profanity
import discord
from discord.ext import commands
import random
import asyncio
import json

client = commands.Bot(command_prefix='1')


def get_welcome(client, message):
    with open('cogs/jfiles/servers.json', 'r') as f:
        welcomes = json.load(f)

    return welcomes[str(message.guild.id)]['Welcome']


### Events ###

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        with open('cogs/jfiles/servers.json', 'r') as f:
            welcomes = json.load(f)

        channel_id = welcomes[str(member.guild.id)]['Welcome']
        channel = self.client.get_channel(int(channel_id))
        join = [
            f'{member.mention} has joined the game.',
            f'The great {member.mention} has arrived.',
            f'{member.mention} somehow got in with an invite.',
            f'{member.mention} took a peek',
            f'/summon {member.mention}.',
            f'{member.mention} crash landed and is stuck here.'

        ]
        role = discord.utils.get(member.guild.roles, name='Member')
        embed = discord.Embed(
            title=f"{member.guild}",
            colour=discord.Colour.dark_gray()
        )

        pfp = member.avatar_url
        embed.add_field(name=f"Welcome to {member.guild}", value=random.choice(join))
        embed.add_field(name="User ID:", value=f'{member.id}', inline=False)
        embed.set_thumbnail(url=pfp)
        await channel.send(embed=embed)
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        with open('cogs/jfiles/servers.json', 'r') as f:
            welcomes = json.load(f)

        channel_id = welcomes[str(member.guild.id)]['Welcome']
        channel = self.client.get_channel(int(channel_id))
        leave = [
            f'{member.mention} has left the game.',
            f'The great {member.mention} left and took the damn cake.',
            f'{member.mention} got out of the server.',
            f'{member.mention} left with the damn pizza.',
            f'/leave {member.mention}.',
            f'{member.mention} fixed his ship and flew away.'

        ]
        role = discord.utils.get(member.guild.roles, name='Member')
        embed = discord.Embed(
            title=f"{member.guild}".format(client),
            colour=discord.Colour.dark_gray()
        )

        pfp = member.avatar_url
        embed.add_field(name=f"Goodbye", value=random.choice(leave))
        embed.add_field(name="User ID:", value=f'{member.id}', inline=False)
        embed.set_thumbnail(url=pfp)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Events(client))
