import os,dotenv,datetime
import discord
from discord import app_commands
from discord.app_commands import describe
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
dotenv.load_dotenv()

bottoken = os.environ.get("TOKEN1")

@client.event
async def on_ready():
    print('ログインしました')
    await tree.sync()

@tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('こんにちは!')

@tree.command(name="greet", description="名前を指定して挨拶します")
async def greet(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'{name}さん、こんにちは!')

@tree.command(name="add", description="2つの数字を足します")
async def add(interaction: discord.Interaction, a: int, b: int = 0):
    result = a + b
    await interaction.response.send_message(f'結果: {result}')

@tree.command(name="multiply", description="2つの数字を掛けます")
@describe(a="1つ目の数字", b="2つ目の数字")
async def multiply(interaction: discord.Interaction, a: int, b: int):
    result = a * b
    await interaction.response.send_message(f'結果: {result}')


client.run(f"{bottoken}")