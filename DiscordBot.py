import discord
import random
import os
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

description = ""

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", description=description, intents=intents)
tree = app_commands.CommandTree(client)
dateStr = datetime.today().strftime('%Y-%m-%d')
day = int(datetime.today().day)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="VALORANT"))
    await tree.sync(guild=discord.Object(id=1334394629746851913))
    channel = client.get_channel(1349470222532345989)

    #await channel.send()

try:
    client.run(os.getenv('token'))
except Exception as e:
    print("debug")
    print(e)
    print(e.args)


