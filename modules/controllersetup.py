from sys import prefix
from discord.ext import commands
import discord
import random
import json
import asyncio


script = """
```lua
getgenv().Settings = {
    ['Key'] = "KEY",
    ['Controller'] = CONTROLLERID,
    ['User'] = "USER",
    ['Prefix'] = "PREFIX",
    ['FPS'] = FPS1,
    ['Advert'] = "ADVERT",
    ['Dance'] = "DANCE",
    ['MoreCPU'] = "MORECPU",
}

getgenv().Alts = {
    Alt1 = 12345,
    Alt2 = 12345,
    Alt3 = 12345,
}

loadstring(game:HttpGet('https://raw.githubusercontent.com/halloweevn/SpookyControl/main/Script/v2', true))()
```

"""



with open("config.json", "r") as json_file:
    j = json.load(json_file)
    

prefix = j["prefix"]


class freegen(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def setup(self, ctx):

        def check(m: discord.Message):  # m = discord.Message.
            return m.author.id == ctx.author.id and m.guild == None

        if ctx.guild != None:
            embedser=discord.Embed(title="Please check your DM's", description="If no message then please enable DM's", color=(0xeb673b))
            embedser.set_footer(text = j["footer"])
            await ctx.reply(embed=embedser)
        embeddm=discord.Embed(title="Please type your key", description="Example: ``", color=(0xeb673b))
        embeddm.set_footer(text = j["footer"])
        await ctx.author.send(embed=embeddm)
        try:
            reply_message1 = await self.bot.wait_for('message', check = check, timeout=15.0)
            key = reply_message1.content
            if key.isnumeric() == False:
                embed=discord.Embed(title=f"Please do `{prefix}setup` again. This time enter a value that only contains intgers", description="Ex: `1234`", color=(0xeb673b))
                await ctx.send(embed=embed)
            sch1 = script.replace("KEY", key)
            embed=discord.Embed(title=f"Key = {key}", description="Now please enter your Controller ID", color=(0xeb673b))
            await reply_message1.author.send(embed=embed)
            reply_message2 = await self.bot.wait_for('message', check = check, timeout=15.0)
            controller = reply_message2.content
            sch2 = sch1.replace("CONTROLLERID", controller)

            embed=discord.Embed(title=f"Controller = {controller}", description="Now please enter your User", color=(0xeb673b))
            await reply_message2.author.send(embed=embed)
            reply_message3 = await self.bot.wait_for('message', check = check, timeout=15.0)
            user = reply_message3.content
            sc3 = sch2.replace("USER", user)

            embed=discord.Embed(title=f"User = {user}", description="Now please enter your Prefix", color=(0xeb673b))
            await reply_message3.author.send(embed=embed)
            reply_message4 = await self.bot.wait_for('message', check = check, timeout=15.0)
            prefix = reply_message4.content
            sc4 = sc3.replace("PREFIX", prefix)

            embed=discord.Embed(title=f"Prefix = {prefix}", description="Now please enter the amount of FPS", color=(0xeb673b))
            await reply_message4.author.send(embed=embed)
            reply_message5 = await self.bot.wait_for('message', check = check, timeout=15.0)
            fps = reply_message5.content
            sc5 = sc4.replace("FPS1", fps)

            embed=discord.Embed(title=f"FPS = {fps}", description="Now please enter Advert. Type `none` for default.", color=(0xeb673b))
            await reply_message5.author.send(embed=embed)
            reply_message6 = await self.bot.wait_for('message', check = check, timeout=15.0)
            advert = reply_message6.content
            if advert == "none":
                sc6 = sc5.replace("ADVERT", ".gg/halloweens")
            else:
                sc6 = sc5.replace("ADVERT", advert)
            
            embed=discord.Embed(title=f"Advert = {advert}", description="Now please enter Dance ID. Type `none` for default.", color=(0xeb673b))
            await reply_message6.author.send(embed=embed)
            reply_message7 = await self.bot.wait_for('message', check = check, timeout=15.0)
            dance = reply_message7.content
            if dance == "none":
                sc7 = sc6.replace("DANCE", "rbxassetid://12345")
            else:
                sc7 = sc6.replace("ADVERT", dance)            

            embed=discord.Embed(title=f"Dance ID = {dance}", description="Now would you like to use more cpu? Example `true`. User only `true/false`.", color=(0xeb673b))
            await reply_message7.author.send(embed=embed)
            reply_message8 = await self.bot.wait_for('message', check = check, timeout=15.0)
            cpu = reply_message8.content
            if cpu == "true" or cpu == "false":
                sc8 = sc7.replace("MORECPU", cpu)
            else:
                embed=discord.Embed(title=f"Please do `{prefix}setup` again. This time enter a boolean.", description="Ex: `true`", color=(0xeb673b))
                await ctx.send(embed=embed)

            embed=discord.Embed(title="Script:", description=sc8, color=(0xeb673b))
            embed.set_footer(text = j["footer"])
            await reply_message1.reply(embed=embed)
        except asyncio.TimeoutError:
            embed=discord.Embed(title="You ran out of time :C", description=f'do {prefix}setup to start again.', color=(0xeb673b))
            embed.set_footer(text = j["footer"])
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(freegen(bot))