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
    async def on_member_join(self, member: discord.Member = None):
        join = [
            f'{member.mention} has joined the game.',
            f'The great {member.mention} has arrived.',
            f'{member.mention} somehow got in with an invite.',
            f'{member.mention} the pizza delivery guy.',
            f'/summon {member.mention}.',
            f'{member.mention} crash landed and is stuck here.'

        ]
        role = discord.utils.get(member.guild.roles, name='Member')

        channel = discord.utils.get(member.guild.channels, name='hello-world')
        embed = discord.Embed(
            title="Welcome to Bot Test".format(client),
            colour=discord.Colour.dark_gray()
        )
        pfp = member.avatar_url
        embed.add_field(name=f"Username:", value=f'{member}')
        embed.add_field(name="User ID:", value=f'{member.id}', inline=False)
        embed.set_thumbnail(url=pfp)
        await channel.send(embed=embed)
        await member.add_roles(role)
        await channel.send(random.choice(join))


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='hello-world')
        await channel.send(f'{member.mention} has left the game.')

    @commands.Cog.listener()
    async def on_message(self, ctx, message = None):
        if message.content == "Am I good?":
            await ctx.send("Yes, yes you are you magnificent bastard.")

def setup(client):
    client.add_cog(Events(client))
