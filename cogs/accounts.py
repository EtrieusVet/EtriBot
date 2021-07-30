import json
import discord
from discord.ext import commands
import os
from pretty_help import PrettyHelp
from github import Github

with open('cogs/jfiles/credentials.json', 'r') as file:
    data = json.load(file)
    token = data['Github']['Token']

git = Github(login_or_token=token)

class Accounts(commands.Cog, description='These are for Etrieus but still available nonetheless.'):

    def __init__(self, client):

        self.client = client

    @commands.command(aliases=['register'], brief='Register an account.')
    async def Register(self, ctx, username, password):

        await ctx.message.delete()
        with open('cogs/jfiles/accounts.json', 'r') as f:
            data = json.load(f)

        data[username] = {}
        data[username]['Password'] = password

        with open('cogs/jfiles/accounts.json', 'w') as f:
            json.dump(data, f, indent=4)

        with open('cogs/jfiles/accounts.json', 'r') as f:
            accounts = f.read()

        repo = git.get_repo("EtrieusVet/EtriBot")
        contents = repo.get_contents('cogs/jfiles/accounts.json')
        repo.update_file(contents.path, 'On Join', accounts, contents.sha, branch='main')

        await ctx.send('Recorded!')

def setup(client):
    client.add_cog(Accounts(client))