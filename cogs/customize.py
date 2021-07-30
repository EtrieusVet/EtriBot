import json
import discord
from discord.ext import commands
from github import Github

def get_servers(client, message):
    with open('cogs/jfiles/servers.json', 'r') as f:
        servers = json.load(f)

    return servers[str(message.guild.id)]

class Customization(commands.Cog, description="Commands that will customize the server."):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['setsuggestion'], brief='Sets a suggestion channel to the specified mentioned channel.')
    @commands.has_permissions(manage_guild = True)
    async def SetSuggestion(self, ctx, channel: discord.TextChannel):

        await ctx.message.delete()
        with open('cogs/jfiles/credentials.json', 'r') as file:
            data = json.load(file)
            token = data['Github']['Token']

        git = Github(login_or_token=token)

        with open('cogs/jfiles/servers.json') as f:
            servers = json.load(f)

        servers[str(ctx.guild.id)]['Suggestion'] = channel.id

        with open('cogs/jfiles/servers.json', 'w') as f:
            json.dump(servers, f, indent=4)

        with open('cogs/jfiles/servers.json', 'r') as f:
            servers = f.read()

        repo = git.get_repo("EtrieusVet/EtriBot")
        contents = repo.get_contents('cogs/jfiles/servers.json')
        repo.update_file(contents.path, 'On Join', servers, contents.sha, branch='main')

        await ctx.send(f'The suggestion channel is now {channel}')

    @commands.command(aliases=['prefixer'], brief="Changes the server prefix.")
    @commands.has_permissions(manage_guild = True)
    async def Prefixer(self, ctx, prefix):

        with open('cogs/jfiles/credentials.json', 'r') as file:
            data = json.load(file)
            token = data['Github']['Token']

        git = Github(login_or_token=token)


        with open('cogs/jfiles/servers.json', 'r') as f:
            servers = json.load(f)

        servers[str(ctx.guild.id)]['Prefix'] = prefix

        with open('cogs/jfiles/servers.json', 'w') as f:
            json.dump(servers, f, indent=4)

        with open('cogs/jfiles/servers.json', 'r') as f:
            servers = f.read()

        repo = git.get_repo("EtrieusVet/EtriBot")
        contents = repo.get_contents('cogs/jfiles/servers.json')
        repo.update_file(contents.path, 'On Join', servers, contents.sha, branch='main')

        await ctx.send(f'The prefix for the server is now {prefix}.')

    @Prefixer.error
    async def prefix_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please fill out the required argument.")

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permissions to use this command.")


    @commands.command(aliases=['setwelcome'])
    @commands.has_permissions(manage_guild = True)
    async def SetWelcome(self, ctx, channel: discord.TextChannel):

        with open('cogs/jfiles/credentials.json', 'r') as file:
            data = json.load(file)
            token = data['Github']['Token']

        git = Github(login_or_token=token)

        with open('cogs/jfiles/servers.json', 'r') as f:

            servers = json.load(f)

        servers[str(ctx.guild.id)]['Welcome'] = channel.id

        with open('cogs/jfiles/servers.json', 'w') as f:
            json.dump(servers, f, indent=4)

        with open('cogs/jfiles/servers.json', 'r') as f:
            servers = f.read()

        repo = git.get_repo("EtrieusVet/EtriBot")
        contents = repo.get_contents('cogs/jfiles/servers.json')
        repo.update_file(contents.path, 'On Join', servers, contents.sha, branch='main')

        await ctx.send(f"The welcome channel for the server is now {channel}.")

def setup(client):
    client.add_cog(Customization(client))