import discord
from discord.ext import commands
import random
import asyncio
import json
import requests
import praw


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

    @commands.command(brief="Shows memes from reddit.", aliases=['meme'])
    async def Meme(self, ctx):

        posts = []
        reddit = praw.Reddit(client_id="vzt5totaF7G4T1RMg9abeQ",
                             client_secret="_uf6dK06Ylht_d9owY6LKwu4f804oA",
                             username="Etrieus",
                             password="Ornestrio-132",
                             user_agent="Etrieus"
                             )
        subreddit = reddit.subreddit('memes')

        top = subreddit.top(limit=100)

        for submission in top:
            posts.append(submission)

        random_sub = random.choice(posts)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(
            title=name,
            color=discord.Color.blue()
        )
        embed.set_footer(text=url)
        embed.set_image(url=url)

        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Memes(client))
