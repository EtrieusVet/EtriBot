import discord
from discord.ext import commands


class Isle(commands.Cog, description="Isle related commands."):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Displays a photo of Stan.", aliases=["stan"])
    async def Stan(self, ctx):
        embed = discord.Embed(
            title="Stan",
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="This is a picture of Stan.")
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/808285823267110932/808285873585782794/300.png'
        )
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=["A", "art a", "a"], brief="Displays a photo of Artifact A")
    async def ArtA(self, ctx):
        embed = discord.Embed(
            title="Artifact A",
            colour=discord.Colour.dark_gold()
        )
        embed.set_image(
            url='https://static.wikia.nocookie.net/badorkbee-games/images/0/06/ArtifactA.png/revision/latest?cb=20191228145403')
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=["B", "b", "art b"])
    async def ArtB(self, ctx):
        embed = discord.Embed(
            title="Artifact B",
            colour=discord.Color.red()
        )
        embed.set_image(url='https://static.wikia.nocookie.net/badorkbee-games/images/0/07/ArtifactB.png/revision/latest?cb=20191228225715')
        await ctx.channel.send(embed=embed)
def setup(client):
    client.add_cog(Isle(client))