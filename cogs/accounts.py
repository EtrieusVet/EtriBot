import json
import discord
from discord.ext import commands
import os
from pretty_help import PrettyHelp
from github import Github

class Accounts(commands.Cog, description='These are for Etrieus but still available nonetheless.'):

    def __init__(self, client):

        self.client = client

    @commands.command(aliases=['register'], brief='Register an account.')
    async def Register(self, ctx, username, password):

        with open('jfiles/accounts.json', 'r'):
            data = json.load(f)

        data[username] = {}
        data[username]['Password'] = password

        with open('jfiles/accounts.json', 'w'):
            json.dump(data, f, indent=4)


        with open('jfiles/accounts.json', 'r') as f:
            servers = f.read()

        repo = git.get_repo("EtrieusVet/EtriBot")
        contents = repo.get_contents('jfiles/accounts.json')
        repo.update_file(contents.path, 'On Join', servers, contents.sha, branch='main')

        await ctx.send('Recorded!')

def setup(client):
    client.add_cog(Accounts(client))