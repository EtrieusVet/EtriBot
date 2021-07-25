# Imports

import asyncio
import discord
from discord.ext import commands

class SCommands(commands.Cog, description="Commands for people with permissions."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        print("SCommands is online!")

    @commands.command(aliases=["clear"], brief="Clears messages including the command.")
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, ctx, amount: int):

        await ctx.channel.purge(limit=amount+1)

    @Clear.error
    async def clear_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required role.')
            embed.add_field(name='Missing Roles:', value='Manage Messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bot Missing Permissions.')
            embed.add_field(name='Missing Roles:', value='Manage Messages')
            await ctx.send(embed=embed)


    @commands.command(aliases=['kick'], brief='Kicks the specified user.')
    @commands.has_permissions(kick_permissions = True)
    async def Kick(self, ctx, member: discord.Member, *, reason= 'None'):

        if member.top_role >= ctx.author.top_role:

            await ctx.purge(limit=1)
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Hierarchy')
            embed.add_field(name='Error:', value='You can only kick users lower than you.')
            await ctx.send(embed=embed)

        if member == ctx.message.author:

            await ctx.purge(limit=1)
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='???')
            embed.add_field(name='Error:', value='Why the hell would you want to kick yourself?')
            await ctx.send(embed=embed)

        else:

            await ctx.purge(limit=1)
            await member.kick(reason=reason)
            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='SCommand form')
            embed.add_field(name='User:', value=f'{member.mention}')
            embed.add_field(name='Reason:', value=reason)


    @Kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bot Missing Permissions.')
            embed.add_field(name='Missing Roles:', value='Manage Messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required role.')
            embed.add_field(name='Missing Roles:', value='Manage Messages')
            await ctx.send(embed=embed)

    @commands.command(aliases=["autoUlt"], brief="Autopings the user by a specified number.")
    @commands.has_permissions(manage_guild = True)
    async def UltraPing(self, ctx, member: discord.Member = None, *, num):

        channel = discord.utils.get(member.guild.channels, name='autopinger')
        i = 0
        limit = num
        true_limit = 101

        if float(limit) > true_limit:

            await ctx.channel.send("The limit is 100.")

        elif float(limit) < true_limit:

            await ctx.send(f'Autopinging..')
            while i < float(limit):
                i += 1
                await channel.send(f'{member.mention}')

    @UltraPing.error
    async def pinger_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required role.')
            embed.add_field(name='Missing Roles:', value='Manage Guild')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(SCommands(client))
