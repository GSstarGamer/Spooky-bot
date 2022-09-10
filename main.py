
import discord 
from discord.ext import commands
import os
import json

with open("config.json", "r") as json_file:
    j = json.load(json_file)
    print("Loaded config.")

os.system("cls")
print("Loading Spooky bot :cool:")

intents = discord.Intents.all()
discord.member = True

Bot_Prefix = j["prefix"]
bot = commands.Bot(command_prefix=Bot_Prefix, intents = intents)
bot.remove_command("help")



#on start
@bot.event
async def on_ready():
    os.system("cls")
    print(f"Ez, logged into bot '{bot.user.display_name}'.")
    await bot.change_presence(activity=discord.Streaming(name=j["activity"], url="https://www.twitch.tv/who_is_halloween"))


#cogs
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
       print(f"Loading cog: {filename}")
       bot.load_extension(f'commands.{filename[:-3]}')\

#help command
genfree = f"""
This command is used to generate a roblox account. Use in <#1017328855696023593>. Usage:
`{Bot_Prefix}roblox`
"""

genbooster = f"""
This command is used to generate a roblox account. Only for boosters. Use in <#1017329396903854111> Usage:
`{Bot_Prefix}roblox2`
"""

stock = f"""
This command is the count of stock of accounts. Usage:
`{Bot_Prefix}stock`
"""

cashcounter = f"""
Script for **Cash Counter**. Usage:
`{Bot_Prefix}cashcounter`
"""
crash = f"""
Crash scripts for **Da Hood**. Usage:
`{Bot_Prefix}crash`
"""

group = f"""
**Spooky Control Group**. Usage:
`{Bot_Prefix}group`
"""
gui = f"""
**Spooky Seller GUI**. Usage:
`{Bot_Prefix}gui`
"""

@bot.group(invoke_without_command=True)
async def help(ctx):
    #gen help
    embed=discord.Embed(title="Here are the list of commands for account generator & scripts, and usage", description=f'prefix is set to "{Bot_Prefix}"', color=(0xeb673b))
    embed.add_field(name="Free generator", value=genfree, inline=True)
    embed.add_field(name="Booster generator", value=genbooster, inline=True)
    embed.add_field(name="Stock", value=stock, inline=True)
    embed.add_field(name="Cash Counter Script", value=cashcounter, inline=True)
    embed.add_field(name="Crash Scripts", value=crash, inline=True)    
    embed.add_field(name="Spooky Roblox Group", value=group, inline=True)
    embed.add_field(name="Spooky GUI", value=gui, inline=True)
    embed.set_footer(text = j["footer"])

    await ctx.reply(embed=embed)



bot.run(j["token"]
)