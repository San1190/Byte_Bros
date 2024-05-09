
import discord
from discord.ext import commands as command
from discord.ext import tasks
from discord.ext import commands as command
from discord.ext import commands, tasks
from discord.utils import get
import random
from itertools import cycle
from threading import Thread
from random import randint





intents = discord.Intents.default()
intents.members = True
client = command.Bot(command_prefix='m!', intents=intents) 
prefijo = "m!"
Client = discord.Client()
client.remove_command('help')


@client.event
async def on_ready():
    change_status.start()
    print("Estoy en linea")
status = cycle(['---MinaBot---'])


@tasks.loop(seconds= 100)
async def  change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def redes(ctx):
   # emoji = client.get_emoji(788774122011492352)
    #emoji2 = client.get_emoji(788774138667860000)
    #emoji3 = client.get_emoji(788768749842071582)


    embed=discord.Embed(title= "Redes sociales de Mina!!!", color=0x11A3EE)
    embed.set_thumbnail(url ="https://i.imgur.com/pfDTn7M.png" )
    embed.add_field(name =f' Instagram ', value= '[Pincha aquí!!](https://www.instagram.com/mina_starliart/)',inline = False)
    embed.add_field(name =f"Instagram de dibujios", value='[Pincha aquí](https://www.instagram.com/minastarlia_art/)',inline=False)
    embed.add_field(name =f'Twitch', value= '[Pincha aquí!!](https://www.twitch.tv/mina_starliart)',inline = False)
    embed.add_field(name =f'Twitter', value= '[Pincha aquí!!](https://twitter.com/mina_starliart)',inline = False)
    await ctx.message.delete()
    await ctx.send(embed=embed)









client.run("OTY4NTk5NTgxMDQwNDQ3NTA4.YmhMpw.3jkpJU4Tb_gNR6Rvd_-ysODqCWQ")