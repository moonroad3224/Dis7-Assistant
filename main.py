import os,dotenv,datetime
import discord
from pathlib import Path
from discord import app_commands
from discord.app_commands import describe
from discord.ext import commands
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(client)
dotenv.load_dotenv()

directory = Path("appdir")
file_list = [f for f in directory.iterdir() if f.is_file()]

print(file_list)

bottoken = os.environ.get("TOKEN1")

@client.event
async def on_ready():
#    await bot.load_extension("hello.py") #読み込めない
    await client.change_presence(activity=discord.Game(name=f"Last on_ready executed:{datetime.datetime.now()}(+09:00 JST)"))
    print(f"{datetime.datetime.now()}:on_ready  client.user:{client.user} ")
    await tree.sync()



@tree.command(name="issues", description="問題を発見したら")
async def help(interaction: discord.Interaction):
    cmdname = "issues"
    print(f"{datetime.datetime.now()}:{interaction.id} \n{interaction.type}/{cmdname}/{interaction.application_id} \n{interaction.guild}:{interaction.guild_id} \nBuilt-in Commands")
    text = f"もし問題が発生しましたらこちら入力してくれるとありがたいです。（GitHubアカウントが必要です。）: https://github.com/moonroad3224/Dis7-Assistant/issues"
    text = f"{text}\nもしくはmoonroad3224-中村久八まで"
    embed = discord.Embed(title="ヘルプ", description=text, color=0x2000FF)
    embed.add_field(name="ヘルプ", value="フィールドの値", inline=False)
    print(f"{datetime.datetime.now()}:{interaction.id} Done.")
#いったん別ファイルで使うつもりのコマンド↓

@tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    cmdname = "hello"
    print(f"{datetime.datetime.now()}:{interaction.id} \n{interaction.type}/{cmdname}/{interaction.application_id} \n{interaction.guild}:{interaction.guild_id}")
    await interaction.response.send_message('こんにちは!')
    print(f"{datetime.datetime.now()}:{interaction.id} Done.")

client.run(bottoken)