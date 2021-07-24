### Imports ###

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

            await ctx.send("Please specify the amount of messages to be cleared.")

        if isinstance(error, commands.MissingPermissions):

            await ctx.send("You do not have manage_messages permission.")

        if isinstance(error, commands.BotMissingPermissions):

            await ctx.send("I do not have permissions for that.")

    @commands.command(aliases=["kick"], brief="Kicks the specified user.")
    @commands.has_permissions(kick_members = True)
    async def Kick(self, ctx, member: discord.Member, *, reason="no reason provided"):

        role = discord.utils.get(member.guild.roles, name = "Anti BS Department")

        if member == None or member == ctx.message.author:

            await ctx.send("Why would you kick yourself?")
            return

        if role in member.roles:

            await ctx.send("You cannot kick your fellow peers.")

        else:

            await member.kick(reason=reason)
            await member.send(f"You were kicked for {reason} in {ctx.message.guild.name}.")
            await ctx.send(f'{member.mention} was kicked for {reason}.')

    @Kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify a user to be kicked.")

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have kick_members permission.")

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have permissions for that.")

    @commands.command(aliases=["ban"], brief="Kicks the specified user.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner', 'Special Boiz')
    async def Ban(self, ctx, member: discord.Member, *, reason="no reason provided."):

        role = discord.utils.get(member.guild.roles, name="Anti BS Department")
        if member == None or member == ctx.message.author:

            await ctx.send("You can't ban yourself.")
            return

        if role in member.roles:

            await ctx.send("You cannot ban your fellow peers.")

        else:

            await member.ban(reason)
            await member.send(f'You are banned for {reason}.')
            await ctx.send(f'{member.mention} was banned for {reason}.')

    @commands.command(aliases=["mute"], brief="Mutes the specified moron.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')
    async def Mute(self, ctx, member: discord.Member, *, reason="no reason provided"):

        role = discord.utils.get(member.guild.roles, name="Anti BS Department")

        if member == None or member == ctx.message.author:

            await ctx.send("You can't mute yourself.")
            return

        guild = ctx.message.guild.name
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        if mutedRole in member.roles:

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Mute Form", color=discord.Color.darker_gray())
            embed.add_field(name=f"Mute failed", value=f"{member.mention} is already muted.")
            embed.add_field(name="Mute Form requested by:", value=f"{ctx.message.author.mention}")
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)
            print(guild)

        if role in member.roles:

            await ctx.send("You cannot mute your fellow peers.")

        else:

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Mute Form", color=member.color)
            embed.add_field(name="User:", value=f"{member.mention} has been muted.", inline=False)
            embed.add_field(name="Reason:", value=f"{reason}.", inline=False)
            embed.add_field(name="Mute Form requested by:", value=f"{ctx.message.author.mention}")
            await member.add_roles(mutedRole)
            await member.remove_roles(notmutedRole)
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)
            await member.send(f'You are muted in the server {guild.name} for {reason}.')

    @commands.command(aliases=["unmute"], brief="Unmutes the moron.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')
    async def Unmute(self, ctx, member: discord.Member):

        guild = ctx.guild
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        if notmutedRole in member.roles:

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Unmute Form", color=discord.Color.darker_gray())
            embed.add_field(name=f"Unmute failed", value=f"{member.mention} is not muted.")
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)

        else:

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Unmute Form", color=member.color)
            embed.add_field(name="User:", value=f"{member.mention} has been unmuted.", inline=False)
            embed.add_field(name="Unmute form requested by:", value=f"{ctx.message.author.mention}")
            await member.add_roles(notmutedRole)
            await member.remove_roles(mutedRole)
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)
            await member.send(f'You are unmuted, please behave yourself.')

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
