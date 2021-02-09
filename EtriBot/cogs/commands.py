### Imports ###

import random
import discord
from discord.ext import commands

class Commands(commands.Cog, description="Commands that are for general purposes."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands is online")

    @commands.command(aliases=["profile"], brief="Extracts information of the chosen user.")
    async def Profile(self, ctx, member: discord.Member = None):

        author = ctx.message.author
        pfp = member.avatar_url
        
        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
        embed.set_image(url=pfp)
        embed.add_field(name="Username:", value=f"{member}", inline=True)
        embed.add_field(name="ID:", value=f"{member.id}", inline=True)
        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.set_footer(text=f"Requested by:\n{ctx.author} \nID: {ctx.author.id}", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(content=None, embed=embed)

    @commands.command(aliases=["?", "ques"], brief="This answers your fate.")
    async def Question(self, ctx, *, que):
        response = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Yep.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Nah.",
            "Very doubtful."
        ]
        await ctx.send(f'Question: {que}\nAnswer: {random.choice(response)}')

    @commands.command(aliases=["d"], hidden=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["sd"], hidden=True)
    async def clear2(self, ctx, amount=20):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["r"], hidden=True)
    async def clear1(self, ctx, amount=3):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Commands(client))
