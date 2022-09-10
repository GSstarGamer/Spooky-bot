from discord.ext import commands
import discord
import random
import json

with open("config.json", "r") as json_file:
    j = json.load(json_file)

class freegen(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def roblox(self, ctx):
        channel = ctx.channel.id

        if channel == 1017454482885464114:
            with open(j["accountslocation"], "r") as f1:
                rline = f1.readlines()
                randomline = random.choice(rline)
                combo = randomline.split(":")
                userc = combo[0]
                passc = combo[1]
                newpass = passc.rstrip()
                if len(randomline) == 0:
                    pass
                with open(j["accountslocation"], "w") as wf1:
                    for line in rline:
                        if line.strip('\n') != f"{userc}:{newpass}":
                            wf1.write(line)


            account = f"{userc}:{newpass}"
            author = ctx.author
            embeddm = discord.Embed(title = "Account Below!",color = (0xeb673b),description = f"**User**\n```{userc}```\n**Password**\n```{newpass}```")
            embeddm.set_footer(text = j["footer"])
            await author.send(embed=embeddm)

            embedch = discord.Embed(title = "Account Generated", description = "Check Your DM's!", color = (0xeb673b))
            count = len(open(j["accountslocation"]).readlines())
            embedch.set_footer(text = f"Current stock: {count}")
            await ctx.reply(embed = embedch)
        
        elif channel != 1017454482885464114:
            embed = discord.Embed(title = "Wrong Channel", description = "Please Go To <#1013323993274667115> And Try Again!", color = (0xeb673b))
            await ctx.reply(embed = embed) 

def setup(bot):
    bot.add_cog(freegen(bot))