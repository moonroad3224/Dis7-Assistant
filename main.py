import datetime,os,discord,dotenv
from discord import options
from dotenv import load_dotenv
load_dotenv()
bottoken = os.environ.get('TOKEN1') #ボットのトークン トークン本体は.envファイルに記入
cliant = discord.bot()
intents = discord.Intents.all()
client = discord.client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"Last on_ready executed:{datetime.datetime.now()}(+09:00 JST)"))
    print(f"{datetime.datetime.now()}:on_ready  client.user:{client.user} ")


