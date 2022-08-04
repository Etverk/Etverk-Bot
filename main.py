#Imports
from discord.ext import commands
import discord

#Bot intiation
bot = commands.Bot(command_prefix="&", intents = discord.Intents.default())

#Imports discord token from "database.txt"
with open("database.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    botToken = lines[0]






#Login confirmation message
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")




#Runs bot 
bot.run(botToken)