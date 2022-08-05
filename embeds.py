import discord

def get_help(prefix):
    embed = discord.Embed(
        title = "Help",
        description = f"Etverk commands start with {prefix}.",
        color = 0xde9c16
    )
    
    embed.add_field(
        name = "&help",
        value = "Shows all commands this bot supports.",
        inline = True
    )
   
    return embed