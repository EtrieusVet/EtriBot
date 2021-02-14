### Imports ###


import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='1')

### Events ###

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events is online")

    @commands.Cog.listener()
    async def on_ready(self):
        channel = client.get_channel(806133569029931048)
        embed = discord.Embed(
            title="Bot is online"
        )
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join = [
            f'{member.mention} has joined the game.',
            f'The great {member.mention} has arrived.',
            f'{member.mention} somehow got in with an invite.',
            f'{member.mention} the pizza delivery guy.',
            f'/summon {member.mention}.',
            f'{member.mention} crash landed and is stuck here.'

        ]
        channel = discord.utils.get(member.guild.channels, name='hello-world')
        embed = discord.Embed(
            title="Welcome to Bot Test".format(client),
            colour=discord.Colour.dark_gray()
        )
        pfp = member.avatar_url
        embed.set_image(url=pfp)
        await channel.send(embed=embed)
        await channel.send(random.choice(join))


    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = discord.utils.get(member.guild.channels, name='hello-world')
        await channel.send(f'{member.mention} has left the game')


def setup(client):
    client.add_cog(Events(client))
