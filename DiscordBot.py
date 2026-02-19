import discord
import random
import os
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() # Loads the environment variables from the .env file, which is where the bot token is stored. This allows the bot to access the token securely without hardcoding it into the code.

description = ""
# todo implement datastructure for a user
# implement hashmap for users 
# implement a function to check if a user is in the hashmap and assign roles accordingly

intents = discord.Intents.all()
client = discord.Client(intents=intents) #Declares the bot client and sets the intents to all, which allows the bot to access all events and data from the server. This is necessary for the bot to function properly and assign roles, check user information, etc.
bot = commands.Bot(command_prefix="/", description=description, intents=intents) 
tree = app_commands.CommandTree(client) # Command tree
dateStr = datetime.today().strftime('%Y-%m-%d')
day = int(datetime.today().day) 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="883 E-Sports Tournament"))
    await tree.sync(guild=discord.Object(id=1334394629746851913))
    channel = client.get_channel(1349470222532345989)

    await channel.send(f"Bot is online and running on {dateStr}")

try:
    client.run(os.getenv('token')) # This command gets the token from the .env file and runs the bot
except Exception as e:
    print("debug")
    print(e)
    print(e.args)


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
        #preventing duplicate roles from being added to the user
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)

