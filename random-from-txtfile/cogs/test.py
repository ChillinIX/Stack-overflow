import random
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def color(self,ctx):
        filename1=open('cogs/DB/color.txt','r')
        wordList1=[line.rstrip('\n') for line in filename1]
        filename1.close()
        out1 = random.choice(wordList1)
        await ctx.send(f"color: {out1}")

async def setup(bot):
    await bot.add_cog(test(bot))