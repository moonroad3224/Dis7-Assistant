import os,dotenv,datetime
import discord
from pathlib import Path
from discord import app_commands
from discord.app_commands import describe
#from discord.commands import SlashCommandGroup
from discord.ext import commands
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
dotenv.load_dotenv()

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tree.command(name="hello", description="挨拶を返します")
    async def hello(interaction: discord.Interaction):
        cmdname = "hello"
        print(f"{datetime.datetime.now()}:{interaction.id} \n{interaction.type}/{cmdname}/{interaction.application_id} \n{interaction.guild}:{interaction.guild_id}")
        await interaction.response.send_message('こんにちは!')
        print(f"{datetime.datetime.now()}:{interaction.id} Done.")

def setup(bot):
    bot.add_cog(Example(bot))