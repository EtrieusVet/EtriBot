import discord
from discord.ext import commands
import random
import asyncio

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
        cats = ['https://media.discordapp.net/attachments/806444644002693170/811023336128643082/1800x1200_cat_relaxing_on_patio_other.jpg?width=710&height=473',
                'https://media.discordapp.net/attachments/806444644002693170/811023633111711794/Z.png',
                'https://cdn.discordapp.com/attachments/806444644002693170/811023715541319700/PersianCatFactsHistoryPersonalityandCare_ASPCAPetHealthInsurance_whitePersiancatrestingonabrownsofa-.png',
                'https://media.discordapp.net/attachments/806444644002693170/811023755442520084/images.png',
                'https://media.discordapp.net/attachments/806444644002693170/811023886199947324/Persian-cat-sleeping.png?width=709&height=473',
                'https://media.discordapp.net/attachments/806444644002693170/811023794893226014/Culture-Grumpy-Cat-487386121.png?width=629&height=473',
                'https://cdn.discordapp.com/attachments/806444644002693170/811023886199947324/Persian-cat-sleeping.png',
                'https://media.discordapp.net/attachments/806444644002693170/811024268526616616/images.png',
                'https://media.discordapp.net/attachments/806444644002693170/811024093713006612/kitten-looking-up-towards-the-camera-royalty-free-image-1592957811.png?width=474&height=473']
        embed = discord.Embed(
            title="Cat",
            color=discord.Color.blue()
        )
        embed.set_footer(text="This is an adorable cat")
        embed.set_image(url=random.choice(cats))
        await ctx.channel.send(embed=embed)



def setup(client):
    client.add_cog(Memes(client))
