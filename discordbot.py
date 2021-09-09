import discord
from discord.ext import commands
from discord.utils import get
import random

intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix="+", intents=intents)
token = "" # insert token here

@client.event
async def on_ready():
    print("Login: Success")
    print("User: " + client.user.name + "#" + client.user.discriminator)
    print("ID: " + str(client.user.id))

# function that kicks a random user from voice channel of calling user
@client.command(name='roulette')
async def vc_roulette(ctx):
    if (current_channel := ctx.message.author.voice) != None: # grabs vc of calling user if being called from someone in a vc
        unlucky_user = random.choice(current_channel.channel.members) # picks random user in that channel
        await unlucky_user.edit(voice_channel=None) # sets unlucky user's voice channel to none (in essence, kicks them)
        await ctx.message.channel.send("purged user " + '<@!%s>' % unlucky_user.id)
    else:
        await ctx.message.channel.send("call it from a voice channel" + '<@!%s>' % ctx.message.author.id) # alerts caller that the function needs to be called from voice channel if not doing so
      
client.run(token)
