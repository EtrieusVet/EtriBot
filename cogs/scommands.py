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
            embed.add_field(name='Error Type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required role.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Manage Messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bot Missing Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Manage Messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bad Argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['kick'], brief='Kicks the specified user.')
    @commands.has_permissions(kick_members = True)
    async def Kick(self, ctx, member: discord.Member, *, reason= 'None'):

        if member == ctx.message.author:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='???', inline=False)
            embed.add_field(name='Error:', value='Why the hell would you want to kick yourself?')
            await ctx.send(embed=embed)
            return

        if member.top_role >= ctx.author.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value='You can only kick users lower than you.')
            await ctx.send(embed=embed)
            return

        if member.toprole == ctx.me:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='???', inline=False)
            embed.add_field(name='Error:', value='You must kick me yourself, not use my commands against me.')
            await ctx.send(embed=embed)
            return

        if ctx.me.top_role <= member.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value=f'My role is lower than {member.mention}.')
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success!')
            embed.add_field(name='User:', value=f'{member.mention} has been kicked!', inline=False)
            embed.add_field(name='Reason:', value=reason)
            await member.kick(reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=['ban'], brief='Kicks the specified user.')
    @commands.has_permissions(kick_members = True)
    async def Ban(self, ctx, member: discord.Member, *, reason= 'None'):

        if member == ctx.message.author:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='???', inline=False)
            embed.add_field(name='Error:', value='Why do you want to ban yourself?')
            await ctx.send(embed=embed)
            return

        if member.toprole == ctx.me:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='???', inline=False)
            embed.add_field(name='Error:', value='You must ban me yourself, not use my commands against me.')
            await ctx.send(embed=embed)
            return

        if member.top_role >= ctx.author.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value='You can only ban users lower than you.')
            await ctx.send(embed=embed)
            return

        if ctx.me.top_role <= member.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value=f'My role is lower than {member.mention}.')
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success!')
            embed.add_field(name='User:', value=f'{member.mention} has been banned!', inline=False)
            embed.add_field(name='Reason:', value=reason)
            await member.kick(reason=reason)
            await ctx.send(embed=embed)

    @Ban.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bot Missing Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Ban Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Ban Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bad Argument')
            embed.add_field(name='Error:', value='I could not process that')
            await ctx.send(embed=embed)

    @Kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required argument.', inline= False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bot Missing Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Kick Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Missing required Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Kick Members')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error Type:', value='Bad Argument')
            embed.add_field(name='Error:', value='I could not process that')
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
