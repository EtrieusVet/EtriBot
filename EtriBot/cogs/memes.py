import discord
from discord.ext import commands
import random


class Memes(commands.Cog, description="Commands that are meme related."):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Memes is online")

    @commands.command(brief="Displays a picture of the legendary Morshu in HD", aliases=["morshu"])
    async def Morshu(self, ctx):
        embed = discord.Embed(
            title='Morshu',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="This is a picture of Morshu RTX")
        embed.set_image(
            url='https://media.discordapp.net/attachments/806444644002693170/806444988543139840/maxresdefault.png?width=840&height=473')
        await ctx.channel.send(embed=embed)

    @commands.command(brief="Displays a random cat picture", aliases=["cat"])
    async def Cat(self, ctx):
        cats = ['https://media.discordapp.net/attachments/806444644002693170/806856386838528020/images_1.jpg',
                'https://cdn.discordapp.com/attachments/806444644002693170/806856405343797268/cute-kitty-rub-my-belly.jpg',
                'https://cdn.discordapp.com/attachments/806444644002693170/806856421832523816/download.jpg',
                'https://cdn.discordapp.com/attachments/806444644002693170/806856437346861056/1df706ae30095ad907b9046cdaae2db6.jpg',
                'https://cdn.discordapp.com/attachments/806444644002693170/806856471295033394/images.jpg',
                'https://cdn.discordapp.com/attachments/806444644002693170/806856490571792384/The-Kitten-Checklist-1.png']
        embed = discord.Embed(
            title="Cat",
            color=discord.Color.blue()
        )
        embed.set_footer(text="This is an adorable cat")
        embed.set_image(url=random.choice(cats))
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Memes(client))
