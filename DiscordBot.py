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

#data structure for user
class User:
    def __init__(self, first_name, last_name, discord_user, discord_id, rank, unit, team_name):
        self.first_name = first_name
        self.last_name = last_name
        self.discord_user = discord_user
        self.discord_id = discord_id
        self.rank = rank
        self.unit = unit
        self.team_name = team_name
        self.roles = []

    def add_role(self, role):
        self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)

u = User("Jane", "Doe", "jane#0001", 101, "Member", 2, "Bravo")

print(u.discord_user)  # jane#0001
print(u.roles)         # []

u.add_role("helper")
print(u.roles)  