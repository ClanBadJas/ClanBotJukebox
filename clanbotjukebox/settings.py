import os

import discord
from discord.commands.options import OptionChoice
from dotenv import load_dotenv

load_dotenv()


def _int(name: str):
    try:
        return int(name)
    except ValueError:
        return None

# Get General Bot settings
DISCORD_TOKEN = os.getenv('BOT_TOKEN')
DISCORD_GUILD_ID = _int(os.getenv('GUILD_ID'))
DISCORD_LOG_CHANNEL = _int(os.getenv('LOG_CHANNEL'))

# Configure Lavalink server
# Set Lavalink server IP or hostname
DISCORD_LAVALINK_HOST = os.getenv('LAVALINK_HOST')
# Set Lavalink server port
DISCORD_LAVALINK_PORT = _int(os.getenv('LAVALINK_PORT'))
# Set Lavalink server password
DISCORD_LAVALINK_PASSWORD = os.getenv('LAVALINK_PASSWORD')
# Set Lavalink server Discord Region
DISCORD_LAVALINK_REGION = os.getenv('LAVALINK_REGION')

# Configure Spotify Auth
# Spotify account
DISCORD_SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
# Spotify Token
DISCORD_SPOTIFY_CLIENT_TOKEN = os.getenv('SPOTIFY_CLIENT_TOKEN')

# Set up a list of Guilds to connect, only one in this case
DISCORD_GUILD_IDS = [DISCORD_GUILD_ID]

# Define which intents the bot requires to function
INTENTS = discord.Intents(
    members=True, 
    presences=True, 
    voice_states=True, 
    guild_messages=True, 
    guilds=True, 
    message_content = True
)

#  The default cog(s) to be started
DISCORD_COGS = [
    OptionChoice(name="music", value="Music"),
]