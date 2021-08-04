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

        embed = discord.Embed(color=discord.Colour.green(), timestamp=ctx.message.created_at, title='Success')
        embed.add_field(name='Messages cleared:', value=amount, inline=False)
        embed.add_field(name='SCommand called by:', value=f'{ctx.message.author.mention}')
        await ctx.purge(limit=amount+1)
        await ctx.send(embed=embed)


    @Clear.error
    async def clear_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required role.', inline=False)
            embed.add_field(name='Missing permissions:', value='Manage messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bot missing Permissions.', inline=False)
            embed.add_field(name='Missing permissions:', value='Manage essages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bad argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['kick'], brief='Kicks the specified user.')
    @commands.has_permissions(kick_members = True)
    async def Kick(self, ctx, member: discord.Member, *, reason= 'None'):

        await ctx.message.delete()

        if member == ctx.me:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='???', inline=False)
            embed.add_field(name='Error:', value='You must kick me yourself, not use my commands against me.')
            await ctx.send(embed=embed)
            return

        if member == ctx.message.author:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='???', inline=False)
            embed.add_field(name='Error:', value='Why the hell would you want to kick yourself?')
            await ctx.send(embed=embed)
            return

        if member.top_role >= ctx.author.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value='You can only kick users lower than you.')
            await ctx.send(embed=embed)
            return



        if ctx.me.top_role <= member.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value=f'My role is lower than {member.mention}.')
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success!')
            embed.add_field(name='User:', value=f'{member.mention} has been kicked!', inline=False)
            embed.add_field(name='Reason:', value=reason)
            embed.add_field(name='SCommand called by:', value=f'{ctx.message.author.mention}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=['ban'], brief='Kicks the specified user.')
    @commands.has_permissions(ban_members = True)
    async def Ban(self, ctx, member: discord.Member, *, reason= 'None'):

        await ctx.message.delete()
        if member == ctx.message.author:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='???', inline=False)
            embed.add_field(name='Error:', value='Why do you want to ban yourself?')
            await ctx.send(embed=embed)
            return

        if member.toprole == ctx.me:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='???', inline=False)
            embed.add_field(name='Error:', value='You must ban me yourself, not use my commands against me.')
            await ctx.send(embed=embed)
            return

        if member.top_role >= ctx.author.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value='You can only ban users lower than you.')
            await ctx.send(embed=embed)
            return

        if ctx.me.top_role <= member.top_role:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Hierarchy', inline=False)
            embed.add_field(name='Error:', value=f'My role is lower than {member.mention}.')
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title='Success!')
            embed.add_field(name='User:', value=f'{member.mention} has been banned!', inline=False)
            embed.add_field(name='Reason:', value=reason)
            embed.add_field(name='SCommand called by:', value=f'{ctx.message.author.mention}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed)

    @Ban.error
    async def ban_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bot Missing Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Ban Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Ban Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bad Argument')
            embed.add_field(name='Error:', value='I could not process that')
            await ctx.send(embed=embed)


    @Kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline= False)
            embed.add_field(name='Error:', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bot Missing Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Kick Members.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required Permissions.', inline=False)
            embed.add_field(name='Missing Permissions:', value='Kick Members')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bad Argument')
            embed.add_field(name='Error:', value='I could not process that')
            await ctx.send(embed=embed)


    @commands.command(aliases=['mute', 'Silence', 'silence'])
    @commands.has_permissions(manage_messages = True)
    async def Mute(self, ctx, member: discord.Member, *, reason = None):


        await ctx.message.delete()
        mute_role = discord.utils.get(ctx.guild.roles, name = 'Muted')

        if not mute_role:

            mute_role = await ctx.guild.create_role(name='Muted')

            for channel in ctx.guild.channels:

                await channel.set_permissions(mute_role, speak=False, send_messages=False)

        if mute_role in member.roles:

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='???', inline=False)
            embed.add_field(name='Error:', value='They are already muted, give them a break.')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Colour.green(), title='Success!')
            embed.add_field(name='Muted:', value=f'{member.mention}', inline=False)
            embed.add_field(name='Reason:', value=reason)
            embed.add_field(name='SCommand called by:', value=f'{ctx.message.author.mention}')
            await member.add_roles(mute_role, reason=reason)
            await ctx.send(embed=embed)
            await self.client.delete_message(ctx.message)

    @Mute.error
    async def mute_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required permission.', inline=False)
            embed.add_field(name='Missing permissions:', value='Manage messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            embed = discord.Embed(color=discord.Color.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bag argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['unmute', 'Unsilence', 'unsilence'])
    @commands.has_permissions(manage_messages = True)
    async def Unmute(self, ctx, member: discord.Member):

        await ctx.message.delete()
        mute_role = discord.utils.get(ctx.guild.roles, name = 'Muted')

        if mute_role not in member.roles:

            embed = discord.Embed(color=discord.Colour.red(), title='Error')
            embed.add_field(name='Error type', value='???', inline=False)
            embed.add_field(name='Error:', value='You can\'t unmute someone that isn\'t muted.')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Colour.green(), title='Success!')
            embed.add_field(name='Unmuted:', value=f'{member.mention}', inline=False)
            embed.add_field(name='SCommand called by:', value=f'{ctx.message.author.mention}')
            await member.remove_roles(mute_role)
            await ctx.send(embed=embed)

    @Unmute.error
    async def unmute_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required permission.', inline=False)
            embed.add_field(name='Missing permissions:', value='Manage messages')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required argument.', inline=False)
            embed.add_field(name='Error', value='You did not fill in the required argument.')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Color.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Bag argument.', inline=False)
            embed.add_field(name='Error:', value='I could not process that.')
            await ctx.send(embed=embed)

    @commands.command(aliases=["autoUlt"], brief="Autopings the user by a specified number.")
    @commands.has_permissions(manage_guild=True)
    async def UltraPing(self, ctx, member: discord.Member = None, *, num):

        await ctx.message.delete()
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

            await ctx.message.delete()
            embed = discord.Embed(color=discord.Colour.red(), timestamp=ctx.message.created_at, title='Error')
            embed.add_field(name='Error type:', value='Missing required permission.', inline=False)
            embed.add_field(name='Missing roles:', value='Manage guild')
            await ctx.send(embed=embed)

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

def setup(client):
    client.add_cog(SCommands(client))
