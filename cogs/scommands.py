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

    @commands.command(aliases=["mute"], brief="Mutes the specified moron.")
    async def Mute(self, ctx, member: discord.Member, *, reason="no reason provided"):

        guild = ctx.guild
        mutedRole = discord.utils.get(member.guild.roles, name='Muted')
        notmutedRole = discord.utils.get(member.guild.roles, name="Member")

        if not mutedRole:
            mutedRole = await guild.create_role('Muted')

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await member.remove_roles(notmutedRole)
        await ctx.send(f'Muted {member.mention} for {reason}.')
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

def setup(client):
    client.add_cog(SCommands(client))
