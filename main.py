import datetime
import os
import discord
import dotenv
from discord.ext import commands
from discord import app_commands
import dotenv
from dotenv import load_dotenv
load_dotenv()
bottoken = os.environ.get("TOKEN1")
intents = discord.Intents.all()
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(activity=discord.Game(name=f"Last on_ready executed:{datetime.datetime.now()}(+09:00 JST)"))
    print(f"{datetime.datetime.now()}:on_ready  client.user:{client.user} ")

@tree.command(name='hello', description='Say hello to the world!') 
async def test(interaction: discord.Interaction): 
  await interaction.response.send_message('Hello, World!')

#@bot.command(name="help", description="ヘルプの表示またはコマンドの説明")
#async def help(ctx: discord.ApplicationContext, command: str = ''):
#    if command == '' :
#        text = 'ヘルプ\n/help:ヘルプを表示します。この後ろに引数を追加することでそのコマンドのヘルプを表示します。'
#    elif command == 'help':
#        text = '/help:ヘルプを表示します。この後ろに引数を追加することでそのコマンドのヘルプを表示します。'
#    else:
#        text == 'コマンドが見つからない、またはヘルプに定義されていない可能性があります。'
#    embed = discord.Embed(title='ヘルプ', description="ヘルプ")

client.run(bottoken)
