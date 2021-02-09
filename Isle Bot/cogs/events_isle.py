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
        print("Isle Events is online")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join = [
            f'{member.mention} went here because he is targeted by stan.',
            f'The great {member.mention} promised to get Artifact A.',
            f'{member.mention} somehow glitched in with Key Presser.',
            f'{member.mention} brought a drone.',
            f'{member.mention} crashed here and is stuck for 5 days.',
            f'{member.mention} was brought here against their will.'

        ]
        channel = discord.utils.get(member.guild.channels, name='hello-world')
        embed = discord.Embed(
            title="Welcome to Legendary Isle Party".format(client),
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
