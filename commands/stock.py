from discord.ext import commands
import discord
import json

with open("config.json", "r") as json_file:
    j = json.load(json_file)


class stockcheck(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def stock(self, ctx):
        with open(j["accountslocation"], 'r') as fp:
            lines = len(fp.readlines())
            embed = discord.Embed(title = "**Current Roblox Stock**:", description = lines, color = (0xeb673b))
            await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(stockcheck(bot))