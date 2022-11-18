import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = '/', intents = intents, help_command = None)

async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
  await load()
  load_dotenv()
  token = os.getenv("token")
  await bot.start(token)

asyncio.run(main())