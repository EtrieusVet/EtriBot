# Imports

import json
import requests
import wolframalpha
import asyncio
import random
import discord
from discord.ext import commands
from EtriBot import client

wolframkey = 'WRH7AP-KHGXRWUY6X'

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
    async def Profile(self, ctx, member: discord.Member):

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

    @Profile.error
    async def profile_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bad Argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)

    @commands.command(aliases=["dm"], brief="Sends a DM to the user.")
    async def DM(self, ctx, member: discord.Member, *, phrase):
        await member.send(f'{ctx.author}: {phrase}')

    @DM.error
    async def dm_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)


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

        embed = discord.Embed(color=discord.Color.dark_gray(), timestamp=ctx.message.created_at)
        embed.add_field(name=f"Question: ", value=f"{que}", inline=False)
        embed.add_field(name=f"Answer: ", value=f"{random.choice(response)}", inline=False)
        embed.set_footer(text=f"Asked by: \n{ctx.author}")
        await ctx.send(embed=embed)

    @Question.error
    async def question_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)


    @commands.command(aliases=["suggest"], brief="Sends a suggestion to the suggestion channel.")
    async def Suggest(self, ctx, *, suggestion):

        with open('cogs/jfiles/servers.json', 'r') as f:
            servers = json.load(f)

        channel_id = servers[str(ctx.guild.id)]['Suggestion']
        channel = self.client.get_channel(int(channel_id))
        embed = discord.Embed(timestamp=ctx.message.created_at, title="Suggestion Form")
        embed.add_field(name=f'{ctx.message.author}\'s suggestion', value=f"{suggestion}", inline=True)
        await ctx.channel.purge(limit=1)
        await asyncio.sleep(0.5)
        await channel.send(embed=embed)

    @Suggest.error
    async def suggest_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['search'], brief="Searches the input into Wolframalpha.")
    async def Search(self, ctx, *, input):

        wolf_client = wolframalpha.Client(wolframkey)
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

    @Percentage.error
    async def percentage_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)

    @commands.command()
    async def E(self, ctx):

        await ctx.send("E")

    @commands.command(aliases=['choice'], brief='Randomly choose selection of a maximum of 5.')
    async def Choice(self, ctx,
                     choice1=None,
                     choice2=None,
                     choice3=None,
                     choice4=None,
                     choice5=None,
                     choice6=None,
                     choice7=None,
                     choice8=None,
                     choice9=None,
                     choice10=None):


        list = [choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10]
        checked_list=[x for x in list if x]
        chosen = random.choice(checked_list)
        separator = ', '
        seperated = separator.join(checked_list)
        embed = discord.Embed(title='Choices', color=discord.Colour.green(), timestamp=ctx.message.created_at)
        embed.add_field(name='Choices:', value=seperated, inline=False)
        embed.add_field(name='Chosen:', value=chosen)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Commands(client))
