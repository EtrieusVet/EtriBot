import json
import discord
from discord.ext import commands
import os
from pretty_help import PrettyHelp
from github import Github

token = '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'
git = Github(login_or_token=token)

class Accounts(commands.Cog, description='These are for Etrieus but still available nonetheless.'):

    def __init__(self, client):

        self.client = client

    @commands.command(aliases=['register'], brief='Register an account.')
    async def Register(self, ctx, username, password):

        await ctx.message.delete()
        with open('cogs/jfiles/accounts.json', 'r') as f:
            profiles = json.load(f)

        if username in profiles:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Account duplication.', inline=False)
            embed.add_field(name='Error:', value='This username already exists.')
            await ctx.send(embed=embed)

        else:

            profiles[username] = password

            with open('cogs/jfiles/accounts.json', 'w') as f:
                json.dump(profiles, f, indent=4)

            with open('cogs/jfiles/accounts.json', 'r') as f:
                accounts = f.read()

            repo = git.get_repo("EtrieusVet/EtriBot")
            contents = repo.get_contents('cogs/jfiles/accounts.json')
            repo.update_file(contents.path, 'On Join', accounts, contents.sha, branch='main')

            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success')
            embed.add_field(name='Status:', value='Account created successfully!', inline=False)
            embed.add_field(name='Account creation by:', value=f'{ctx.message.author.mention}')
            await ctx.send(embed=embed)

    @Register.error
    async def register_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)


        if isinstance(error, commands.BadArgument):

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bad argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['login'])
    async def Login(self, ctx, username, password):

        await ctx.message.delete()

        with open('cogs/jfiles/accounts.json', 'r') as f:
            profiles = json.load(f)

        if username in profiles:

            if password == profiles[username]:

                embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success')
                embed.add_field(name='Status:', value='Login successful!', inline=False)
                await ctx.send(embed=embed)

        else:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Failed')
            embed.add_field(name='Status:', value='Login failed.', inline=False)
            embed.add_field(name='Error:', value='Incorrect username or password.')
            await ctx.send(embed=embed)

    @Login.error
    async def login_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bad argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Accounts(client))