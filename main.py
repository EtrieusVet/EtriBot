"""
Made by Etrieus
Help with Lopmop

"""

import discord
import random as r
from discord.ext import commands
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="!", intents = intents)
# Program Ready
@client.event
async def on_ready():
    print("Ze Robot iz rready")
# Program Commands
@client.command()
async def hello(ctx):
    await ctx.send("Hi")
@client.command(aliases = ["roastme"])
async def insultme(ctx):
    insults = ["YOU ARE TERRIBLE.",
               "Look at you, being a dumbass.",
               "Wow you are really stupid.",
               "You must be sad doing this command.",
               "What a sad loser.",
               "gay.",
               "Hello chucklenuts.",
               "You must be a fatass.",
               "You are a dumbass."]
    await ctx.send(r.choice(insults))

@client.command(aliases = ["Question", "ques"])
async def question(ctx, *, question):
    responses = [ "Most certainly.",
                 "Definitely.",
                  "Sure.",
                  "Maybe.",
                  "I have no idea.",
                  "Nope.",
                  "Lol no.",
                  "Probably.",
                  "Got no idea.",
                  "I am not sure.",
                  "Ask someone else.",
                  "I haven't a clue.",
                  "I don't think so",
                  "Yeah.",
                  "100%.",
                  "I think it yes",
                  "Im afraid not.",
                  "I am sure, yes."
                  "Don't make me laugh.",
                  "No.",
                  "Yes."
                  ]
    await ctx.send(f'Question: {question}\nAnswer: {r.choice(responses)}')

# Program Events
@client.event
async def on_member_join(member, ctx):
    await ctx.send(f'{member} has let himself in.')
@client.event
async def on_member_remove(member, ctx):
    await ctx.send(f'{member} has let himself out.')

client.run("ODA1MDM1OTU0ODg3ODUyMDUy.YBVCKA.Pom2XOjQpRfxlbAFKD0Tq1A8izQ")