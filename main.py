#Imports
from discord.ext import commands
import discord
import embeds

#Config
prefix = "&"

#Bot intiation
bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.default())

#Imports discord token from "database.txt"
with open("database.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    botToken = lines[0]

bot.remove_command('help')
@bot.command()
async def help(ctx):
    await ctx.send(content=None, embed=embeds.get_help(prefix))

#Login confirmation message
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#Runs bot 
bot.run(botToken)
