import discord
from discord.ext import commands
import random
import asyncio
import json
import requests

class Memes(commands.Cog, description="Commands that are meme related."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Memes is online")

    @commands.command(brief="Displays a random cat picture", aliases=["cat"])
    async def Cat(self, ctx):

        embed = discord.Embed(
            title="Cat",
            color=discord.Color.blue()
        )
        results = requests.get('https://api.thecatapi.com/v1/images/search').json()
        content = results[0]['url']
        embed.set_footer(text="This is an adorable cat")
        embed.set_image(url=content)
        await ctx.channel.send(embed=embed)





def setup(client):
    client.add_cog(Memes(client))
