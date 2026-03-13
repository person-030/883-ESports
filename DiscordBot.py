import discord
import random
import os
import json
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
from dotenv import load_dotenv
description = ""
load_dotenv() # Loads the environment variables from the .env file, which is where the bot token is stored. This allows the bot to access the token securely without hardcoding it into the code.
intents = discord.Intents.all()
client = discord.Client(intents=intents) #Declares the bot client and sets the intents to all, which allows the bot to access all events and data from the server. This is necessary for the bot to function properly and assign roles, check user information, etc.
bot = commands.Bot(command_prefix="/", description=description, intents=intents) 
tree = app_commands.CommandTree(client) # Command tree
dateStr = datetime.today().strftime('%Y-%m-%d')
day = int(datetime.today().day) 

users = {}

class User:
    def __init__(self, first_name: str, last_name: str, 
                discord_user: str, discord_id: int, 
                rank: str, roles: list, unit: int, team_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.discord_user = discord_user
        self.discord_id = discord_id
        self.rank = rank
        self.roles = roles
        self.unit = unit
        self.team_name = team_name

def load_users(filepath):
    global users
    # Keeps data new
    users.clear()
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        
        # discord_user is the key, item is value
        for discord_user, item in data.items():
            user = User(
                first_name=item["first_name"],
                last_name=item["last_name"],
                discord_user=item["discord_user"],
                discord_id=item["discord_id"],
                rank=item["rank"],
                roles=item["roles"],
                unit=item["unit"],
                team_name=item["team_name"]
            )
            # Updating Hashmap
            users[discord_user] = user
            print(users)
        return users
    
    except Exception as e:
        print("Error loading users from file:", e)
        return {}


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="883 E-Sports Tournament"))
    await tree.sync(guild=discord.Object(id=1334394629746851913))
    channel = client.get_channel(1341942160542666812)
    await channel.send(f"Bot is online and running on {dateStr}")
    load_users("data.json")

@tree.command(
    name = "join",
    description= "Sign-in for the tournament and get assigned roles.",
    guild = discord.Object(id=1334394629746851913)
)

async def join(interaction: discord.Interaction):
    guild = await client.fetch_guild(1334394629746851913)
    member = await guild.fetch_member(interaction.user.id)

    # Fetching game role IDs
    valorant = guild.get_role(1334397946720157727)
    brawl_stars = guild.get_role(1334397977531519018)
    fortnite = guild.get_role(1476758746553122959)
    tetris = guild.get_role(1334398002302943253)
    clash_royale = guild.get_role(1476758862324437105)

    # Fetching channel IDs
    general = guild.get_channel(1348128251326890055)
    authentication = guild.get_channel(1348128057365364851)
    announcements = guild.get_channel(1349470222532345989)

    # Hardcoded dict for game role IDS
    gameIDs = {
                "Valorant": valorant,
                "Brawl Stars": brawl_stars,
                "Fortnite": fortnite,
                "Tetris": tetris,
                "Clash Royale": clash_royale
    }
    
    # Hardcoded dict for channel IDS
    channelIDs = {
                "General": general,
                "Authentication": authentication,
                "Announcements": announcements
    }
    try:
        print(member.nick)
    except Exception as e:
        print("Error :", e)
        await interaction.response.send_message("An error occurred while fetching your information. Please contact a senior for assistance.", ephemeral=True)
        return


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

