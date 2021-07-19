import discord
from discord.ext import commands
import random
import asyncio
import json
import requests
import asyncpraw

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

    @commands.command(brief="Shows posts from the subreddit specified.", aliases=['reddit'])
    async def Reddit(self, ctx, *, subreddit = 'memes'):

        async with ctx.typing():

            forbidden = ['hentai', 'sex', 'porn', 'pornhub']

            if any(word in subreddit for word in forbidden):

                await ctx.send("God forbids you to touch this subreddit you god damned subhuman trash.")

            else:
                posts = []
                reddit = asyncpraw.Reddit(client_id="vzt5totaF7G4T1RMg9abeQ",
                                          client_secret="_uf6dK06Ylht_d9owY6LKwu4f804oA",
                                          username="Etrieus",
                                          password="Ornestrio-132",
                                          user_agent="Etrieus"
                                          )
                redditsubs = await reddit.subreddit(subreddit)

                top = redditsubs.top(limit=100)

                async for submission in top:

                    posts.append(submission)

                random_sub = random.choice(posts)
                redditor = random_sub.author
                name = random_sub.title
                url = random_sub.url
                embed = discord.Embed(
                    title=name,
                    color=discord.Color.blue()
                )



                embed.set_image(url=url)
                embed.add_field(name="Text:", value=random_sub.name)
                embed.add_field(name="Author:", value=redditor)
                embed.add_field(name="Link:", value=f'[Source]({url})')
                await ctx.send(embed=embed)

                if random_sub.selftext is None:
                    print("No text found")
                else:
                    with open("Post.txt", "w") as file:
                        file.write(random_sub.selftext)

                    with open("Post.txt", "rb") as file:
                        await ctx.send(file = discord.File(file, 'Post.txt'))

def setup(client):
    client.add_cog(Memes(client))
