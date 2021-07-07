### Imports ###

import json
import requests
import wolframalpha
import wikipedia
import asyncio
import random
import discord
from discord.ext import commands
from EtriBot import client

keys = 'WRH7AP-KHGXRWUY6X'

def get_prefix(client, message):

    with open('cogs/jfiles/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


class Commands(commands.Cog, description="Commands that are for general purposes."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands is online")

    @commands.command(aliases=["profile"], brief="Extracts information of the chosen user.")
    async def Profile(self, ctx, member: discord.Member = None):

        pfp = member.avatar_url
        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at, title="User License")
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="Username:", value=f"{member}", inline=True)
        embed.add_field(name="ID:", value=f"{member.id}", inline=True)
        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Requested by:", value=f"{ctx.message.author.mention}")
        embed.add_field(name="ID:", value=f"{ctx.author.id}")
        await ctx.channel.send(content=None, embed=embed)

    @commands.command(aliases=["dm"], brief="Sends a DM to the user.")
    async def DM(self, ctx, member: discord.Member, *, phrase):
        await member.send(f'{ctx.author}: {phrase}')

    @commands.command(aliases=["?", "ques"], brief="This answers your fate.")
    async def Question(self, ctx, *, que):

        response = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "The answer to that is: yes.",
            "As I see it, yes.",
            "Most likely.",
            "Yep.",
            "Yes.",
            "The answer is obviously no.",
            "It is unlikely.",
            "A big no.",
            "Negative.",
            "The stars have pointed: no.",
            "I believe it is no.",
            "My reply is no.",
            "Sadly, no.",
            "Nah.",
            "Very doubtful."
        ]
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color=discord.Color.dark_gray(), timestamp=ctx.message.created_at)
        embed.add_field(name=f"Question: ", value=f"{que}", inline=False)
        embed.add_field(name=f"Answer: ", value=f"{random.choice(response)}", inline=False)
        embed.set_footer(text=f"Asked by: \n{ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["autoping"], brief="Autopings the user by a specified number.")
    @commands.has_any_role('Ze Creator')
    async def Autoping(self, ctx, member: discord.Member = None, *, num):

        channel = discord.utils.get(member.guild.channels, name='autopinger')
        i = 0
        limit = num
        true_limit = 31

        if float(limit) > true_limit:

            await ctx.channel.send("The limit is 30.")

        elif float(limit) < true_limit:

            await ctx.send(f'Autopinging..')
            while i < float(limit):
                i += 1
                await channel.send(f'{member.mention}')

    @commands.command(aliases=["suggest"], brief="Type a suggestion to send on #suggestions")
    async def Suggest(self, ctx, *, suggestion):

        channel = discord.utils.get(ctx.guild.channels, name = "suggestions")
        embed = discord.Embed(timestamp=ctx.message.created_at, title="Suggestion Form")
        embed.add_field(name=f'{ctx.message.author}\'s suggestion', value=f"{suggestion}", inline=True)
        await ctx.channel.purge(limit=1)
        await asyncio.sleep(0.5)
        await channel.send(embed=embed)

    @commands.command(aliases=['search'], brief="Searches the input into Wolframalpha.")
    async def Search(self, ctx, *, input):

        wolf_client = wolframalpha.Client('WRH7AP-KHGXRWUY6X')
        query = input
        url = f"https://api.wolframalpha.com/v1/result?appid=WRH7AP-KHGXRWUY6X&i={query}"
        response = requests.get(url)
        embed = discord.Embed(title="EtriBot Search", timestamp=ctx.message.created_at, color=discord.Color.green())
        embed.add_field(name="Query:", value=f"{query}", inline= False)
        embed.add_field(name="Results:", value=response.text, inline= False)
        embed.add_field(name="Requested by:", value=f"{ctx.message.author.mention}", inline= False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["%"], brief="Shows a random percentage integer.")
    async def Percentage(self, ctx):
        if ctx.author.id == 744170833324408903:

            percent = random.randint(80, 100)
            string = str(percent)
            await ctx.send(f"{string}%")

        else:

            percent = random.randint(0, 100)
            string = str(percent)
            await ctx.send(f"{string}%")

    @commands.command(aliases=['play'])
    async def Play(self, ctx, url: str):

        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        channel = ctx.author.voice.channel


        if channel == None:

            await ctx.send("You are not in a voice channel.")

        await channel.connect()

    @commands.command()
    async def E(self, ctx):

        await ctx.send("E")

    @commands.command(hidden = True)
    async def Register(self, ctx):

        with open('cogs/jfiles/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = '!'

        with open('cogs/jfiles/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


def setup(client):
    client.add_cog(Commands(client))
