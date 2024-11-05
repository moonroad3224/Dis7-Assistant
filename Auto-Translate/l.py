import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('ログインしました')

    # アクティビティを設定
    new_activity = f"テスト"
    await client.change_presence(activity=discord.Game(new_activity))

    # スラッシュコマンドを同期
    await tree.sync()

@tree.command(name='hello', description='Say hello to the world!')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello, World!')


client.run("TOKEN")