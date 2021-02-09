### Imports ###


import discord
from discord.ext import commands
import random


### Variables/Classes ###
client = commands.Bot(command_prefix='!')


class Commands:
    @commands.command()
    async def question(self, aliases=["q", "?"], *, ctx, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
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
            "Probably no.",
            "Very doubtful."
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('ODA1MDM1OTU0ODg3ODUyMDUy.YBVCKA.2vmW4s8nm_gthYjr7350Pcy_CVk')
