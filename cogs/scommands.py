### Imports ###


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

        await member.kick(reason)
        await member.send(f'You are banned for {reason}.')
        await ctx.send(f'{member.mention} was banned for {reason}.')

    @commands.command(aliases=["mute"], brief="Mutes the specified moron.")
    @commands.has_any_role('Ze Creator', 'Anti BS Department', 'Ze alt of ze owner,', 'Special Boiz')
    async def Mute(self, ctx, member: discord.Member, *, reason="no reason provided."):

        if member == None or member == ctx.message.author:
            await ctx.send("You can't mute yourself.")
            return

        guild = ctx.guild
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        await member.add_roles(mutedRole, reason=reason)
        await member.remove_roles(notmutedRole)
        await ctx.send(f'Muted {member.mention} for {reason}.')
        await ctx.channel.purge(limit=1)
        await member.send(f'You are muted in the server {guild.name} for {reason}.')

    @commands.command(aliases=["unmute"], brief="Unmutes the moron.")
    async def Unmute(self, ctx, member: discord.Member):

        guild = ctx.guild
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        await member.add_roles(notmutedRole)
        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}.")
        await member.send(f'You are unmuted, please behave yourself.')

    @commands.command(aliases=["autoUlt"], brief="Autopings the user by a specified number.")
    @commands.has_any_role('Ze Creator')
    async def UltraPing(self, ctx, member: discord.Member = None, *, num):

        channel = discord.utils.get(member.guild.channels, name='autopinger')
        i = 0
        limit = num
        true_limit = 1001
        if float(limit) > true_limit:
            await ctx.channel.send("The limit is 1000.")
        elif float(limit) < true_limit:
            await ctx.send(f'Autopinging..')
            while i < float(limit):
                i += 1
                await channel.send(f'{member.mention}')


def setup(client):
    client.add_cog(SCommands(client))
