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
bottoken = os.environ.get("TOKEN1")
reactionrole_title = ["A role", "B role", None, None, None]
reactionrole_messageid = [1307162596394405928, 1307162596394405928, None, None, None]
reactionrole_roleid = [1307163041137299476, 1307163064751226900, None, None, None]

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
    await interaction.response.send_message(embed=embed)
    print(f"{datetime.datetime.now()}:{interaction.id} Done.")
#いったん別ファイルで使うつもりのコマンド↓

@tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    cmdname = "hello"
    print(f"{datetime.datetime.now()}:{interaction.id} \n{interaction.type}/{cmdname}/{interaction.application_id} \n{interaction.guild}:{interaction.guild_id}")
    await interaction.response.send_message('こんにちは!')
    print(f"{datetime.datetime.now()}:{interaction.id} Done.")

@client.event
async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
    for i in 4:
        if payload.message_id == reactionrole_messageid[i]:
            await payload.member.add_roles(payload.member.guild.get_role(reactionrole_roleid[i]))
    i = 0

@client.event
async def on_raw_reaction_remove(payload):
    for i in 4:
        if payload.message_id == reactionrole_messageid[i] :
            print(f"{datetime.date.now()}:client.event on_raw_reaction_add reactionrole")
            emoji_name = payload.emoji.name
            guild = client.get_guild(payload.guild_id)
            channel = guild.get_channel()
            if emoji_name == ":regional_indicator_a: ":
                for role in guild.get_member(payload.user_id).roles:
                    if role.id == reactionrole_roleid[i]:
                        await guild.get_member(payload.user_id).remove_roles(guild.get_role(reactionrole_roleid[i]))#ロールを削除
    i = 0


client.run(bottoken)