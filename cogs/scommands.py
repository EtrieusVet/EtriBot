### Imports ###

import asyncio
import discord
from discord.ext import commands


class SCommands(commands.Cog, description="Commands only used by specific roles."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        print("SCommands is online!")

    @commands.command(aliases=["clear"], brief="Clears messages including the command.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')

    async def Clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=1)
        await asyncio.sleep(0.5)
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["kick"], brief="Kicks the specified user.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner', 'Special Boiz')
    async def Kick(self, ctx, member: discord.Member, *, reason="no reason provided."):

        if member == None or member == ctx.message.author:

            await ctx.send("You can't kick yourself.")
            return

        await member.kick(reason=reason)
        await member.send(f"You were kicked for {reason}.")
        await ctx.send(f'{member.mention} was kicked for {reason}.')

    @commands.command(aliases=["ban"], brief="Kicks the specified user.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner', 'Special Boiz')
    async def Ban(self, ctx, member: discord.Member, *, reason="no reason provided."):

        if member == None or member == ctx.message.author:

            await ctx.send("You can't ban yourself.")
            return

        await member.ban(reason)
        await member.send(f'You are banned for {reason}.')
        await ctx.send(f'{member.mention} was banned for {reason}.')

    @commands.command(aliases=["mute"], brief="Mutes the specified moron.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')
    async def Mute(self, ctx, member: discord.Member, *, reason="no reason provided"):


        if member == None or member == ctx.message.author:
            await ctx.send("You can't mute yourself.")
            return

        guild = ctx.guild
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        if mutedRole in member.roles:

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Mute Form", color=discord.Color.darker_gray())
            embed.add_field(name=f"Mute failed", value=f"{member.mention} is already muted.")
            embed.add_field(name="Mute Form requested by:", value=f"{ctx.message.author.mention}")
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)

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
    @commands.has_any_role('Ze Creator', 'Special Boiz')
    async def UltraPing(self, ctx, member: discord.Member = None, *, num):

        channel = discord.utils.get(member.guild.channels, name='autopinger')
        i = 0
        limit = num
        true_limit = 10001
        if float(limit) > true_limit:
            await ctx.channel.send("The limit is 1000.")
        elif float(limit) < true_limit:
            await ctx.send(f'Autopinging..')
            while i < float(limit):
                i += 1
                await channel.send(f'{member.mention}')


def setup(client):
    client.add_cog(SCommands(client))
