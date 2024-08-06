import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import commands as cmd

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('Bot is ready.')

client.add_command(cmd.response)
client.add_command(cmd.addition)
client.add_command(cmd.repeat)

# Run the bot with the token    
client.run(TOKEN)