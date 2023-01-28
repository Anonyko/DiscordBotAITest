import discord
from discord import app_commands
from testbot import *
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@tree.command(name = "carorplane", description = "Predict is this image is a car or plane") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(ctx,url:str):
    predict = predictimg(url)
    await ctx.response.send_message(f'I think it is **{predict}**')
@tree.command(name = "imgtotext", description = "Convert image to text") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def second_command(ctx,url:str,lang:str):
    predict = imgttxt(url,lang)
    await ctx.response.send_message(f'I think this image says \n `{predict}`')
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
client.run(getToken())
