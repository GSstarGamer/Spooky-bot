from discord.ext import commands
import discord
import json
import random


with open("config.json", "r") as json_file:
    j = json.load(json_file)

cashcounter = """
```lua
loadstring(game:HttpGet('https://raw.githubusercontent.com/halloweevn/SpookyControl/main/Source%20%3AD/CashCounter'))()
```
"""

swagmode = """
```lua
loadstring(game:HttpGet('https://raw.githubusercontent.com/lerkermer/lua-projects/master/SuperCustomServerCrasher'))()
```
"""

encryptcrash = """
```lua
loadstring(game:HttpGet('https://raw.githubusercontent.com/remorseW/encryptW/main/CustomEncryptCrasher.lua'))()
```
"""

betterdahood = """
```lua
loadstring(game:HttpGet('https://raw.githubusercontent.com/BetterDaHood/BetterDaHoodCrasher/main/Crash'))()
```
"""

sellergui = """
```lua
loadstring(game:HttpGet('https://raw.githubusercontent.com/halloweevn/SpookyControl/main/Source%20%3AD/GUI'))()
```
"""

class scripts(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cashcounter(self, ctx):
        embed=discord.Embed(title="Spooky Cash Counter", description = cashcounter, color=(0xeb673b))
        embed.set_footer(text = j["footer"])
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def crash(self, ctx):
        embed=discord.Embed(title="Da Hood Crash Scripts", description = "", color=(0xeb673b))
        embed.add_field(name="**Swag Mode**", value=swagmode, inline=False)
        embed.add_field(name="**Encrypt Crash**", value=encryptcrash, inline=False)
        embed.add_field(name="**Better Da Hood**", value=betterdahood, inline=False)
        embed.set_footer(text = j["footer"])
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def group(self, ctx):
        embed=discord.Embed(title="Spooky Control Group", description = "[Roblox group](https://www.roblox.com/groups/13629749/Halloween#!/about)", color=(0xeb673b))
        embed.set_footer(text = j["footer"])
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def gui(self, ctx):
        embed=discord.Embed(title="Spooky Seller GUI", description = sellergui, color=(0xeb673b))
        embed.set_footer(text = j["footer"])
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(scripts(bot))