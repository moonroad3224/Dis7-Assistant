# Pycordを読み込む
import discord
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get("TOKEN1")
# アクセストークンを設定

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)


# 起動時に自動的に動くメソッド
# #03で詳しく説明します
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")


# Botが見える場所でメッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がBot(自分を含む)だった場合は無視する
    if message.author.bot:
        return

    # メッセージが"hello"だった場合、"Hello!"と返信する
    if message.content == 'hello':
        await message.reply("Hello!")

@bot.command(name="greeting", description="挨拶を行います")
async def greeting(ctx: discord.ApplicationContext, user: discord.Option(discord.User, "対象のユーザー")):
    await ctx.respond(f"Hiii, {user.mention}!")

@bot.command(name="help", description="ヘルプの表示またはコマンドの説明")
async def help(ctx: discord.ApplicationContext, command: str):
    if command == '' :
        text = 'ヘルプ\n/help:ヘルプを表示します。この後ろに引数を追加することでそのコマンドのヘルプを表示します。'
    elif command == 'help':
        text = '/help:ヘルプを表示します。この後ろに引数を追加することでそのコマンドのヘルプを表示します。'
    else:
        text == 'コマンドが見つからない、またはヘルプに定義されていない可能性があります。'
    embed = discord.Embed(title='ヘルプ', description="ヘルプ")
    await ctx.respond(embed)

# Botを起動
bot.run(TOKEN)