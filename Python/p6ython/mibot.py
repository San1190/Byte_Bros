
'''Cosas que hacer:
-Autoroles de juegos , de edad, deuropa o latam
-Mensaje de sugerencias
-Chats personalizados por juego'''
import discord
import requests
from discord.ext import commands as command
import json
import time
import youtube_dl
from discord.ext import tasks
from discord.ext import commands as command
from discord.ext import commands, tasks
from discord.ext import commands, tasks
from discord.utils import get
import random
from itertools import cycle
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get



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
status = cycle(['Miau'])

@tasks.loop(seconds= 100)
async def  change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#---------------COMANDO DE BIENVENIDA-------------------
@client.event
async def on_member_join(member):
    channel = client.get_channel(901808197462011955)
    embed=discord.Embed(title=f"Bienvenid@ {member.name}", description=f"Gracias por unirte a {member.guild.name}!", color = 0Xe68359) # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    embed.add_field(name = "**Cualquier duda comunícalo con los Admins :)**", value = f"__**Espero que te lo pases muy bien!!**__ ")
    embed.set_image(url = "https://i.imgur.com/LbIsVV6.png")
    await channel.send(embed=embed)

@client.command()
async def redes(ctx):

    icon_url = str(ctx.guild.icon_url)
    
    embed = discord.Embed(title = "Estas son mis redes!", color =0Xe68359)
    embed.set_thumbnail(url=f'{icon_url}')
    embed.add_field(name = "Twitch", value=f'[Pincha aquí!](https://www.twitch.tv/martushkaaa)',inline = False)
    embed.add_field(name = "Twitter", value =f'[Pincha aquí!](https://twitter.com/Martushkaaaaa)', inline = False)

    await ctx.send(embed=embed)


#--------------------AUTOROL EN REGLAS------------------

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id                                 
    if message_id ==869659377089519676:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        #role = discord.utils.get(guild.roles,)
        if payload.emoji.name == "Tick":
            role = discord.utils.get(guild.roles, name = "Seguidores")

        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None :
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

#----------AUTOROLES----------------------------

#-------------------reglas-----------------
@client.command()
async def holaaafdfdfdffdfdfdfa(ctx):
    
    icon_url = str(ctx.guild.icon_url)

    embed = discord.Embed( title = "Bienvenid@ al servidor!!!", description = "Gracias por unirte al servidor. Por favor acepte las siguientes normas ^^:", color = 0Xe68359)
    embed.set_thumbnail(url=f'{icon_url}')
    embed.add_field(name = "**NORMA NÚMERO 1**", value = "Debe  haber respeto entre las personas ", inline= False)
    embed.add_field(name = "**NORMA NÚMERO 2**", value = "Evitar cualquier comentario o acción que pueda ser ofensiva para otra persona o colectivo",inline= False)
    embed.add_field(name = "**NORMA NÚMERO 3**", value = "Por favor, no haga spam de ningún otro servidor o canal de yt twitch etc... " , inline= False)
    embed.add_field(name = "**NORMA NÚMERO 4**", value = "Respeto al Administrador, moderador o Staff", inline= False)
    #embed.add_field(name = "Para ver los siguientes canales, reacciona:", value =f"✅",  inline= False)


    embed.set_footer(text='Bot creado por: \nSan1190', icon_url = 'https://i.imgur.com/VZTJWEu.jpg')

    await ctx.send(embed = embed)


@client.event
async def on_raw_reaction_remove(payload):
    pass


@client.command()
async def wallpaper(ctx, search=None):
    num = random.randint(0,20)

    if search == None:

        await ctx.send("Debes escribir de que quieres que sea el wallpaper")


    else:

            embed= discord.Embed(title=f"{ctx.author.display_name} tu wallpaper ^^",color=0Xe68359)
            embed.set_author(name= ctx.author.display_name , icon_url= ctx.author.avatar_url)
            pagina = requests.get(f'https://wall.alphacoders.com/api2.0/get.php?auth=128d83df1468cced822bee552fb69236&method=search&term={search}')
            if pagina.status_code == 200:

                y = json.loads(pagina.content)
                img =y["wallpapers"][num]["url_image"]
                    
                embed.set_image(url= img)

                
            else:
             
                await ctx.send("No se ha encontrado gif")
                
    await ctx.send(embed=embed)

@client.command()
async def alerta(ctx, *,men=None):
    if ctx.message.author.guild_permissions.administrator:
        

        if ctx.message.channel.id != 942520202455830561:
            await ctx.send("Este comando solo se puede usar en <#942520202455830561>")
        else:
            if men == None:
                await ctx.send(f"{ctx.author.mention}, Es obligatorio escribir el mensaje de la sugerencia\nUso del comando: `m!alerta <mensaje> Mua <3`")
            else:
                await ctx.message.delete()
                channel = client.get_channel(901808297580036116)
                embed = discord.Embed(title=f'Os informo. Miau: ', description=f'{men}', color=0Xe68359)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg = await channel.send("@everyone")
                msg = await channel.send(embed=embed)
               
                await msg.add_reaction('👍🏼')
                await msg.add_reaction('👎🏼')

    else:
        await ctx.send("**No tienes permiso para usar este comando**", delete_after=5.0)


@client.command()
async def skin(ctx):
    num = random.randint(0,389)

    
    pagina = requests.get('https://valorant-api.com/v1/weapons/skins')
    if pagina.status_code == 200:
        y = json.loads(pagina.content)
        img =y["data"][num]["displayIcon"]

        z = json.loads(pagina.content)
        nombre = z["data"][num]["displayName"]
        embed = discord.Embed(title =f"Tu skin es: {nombre} ", color=0Xe68359)    
        embed.set_image(url= img)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        print(num)
       
    else:
     
        await ctx.send("No se ha encontrado gif")
    


@client.command()
async def agente(ctx):
    num = random.randint(0,18)


    pagina = requests.get("https://valorant-api.com/v1/agents")
    if pagina.status_code == 200:
        y = json.loads(pagina.content)
        img =y["data"][num]["displayIcon"]

        z = json.loads(pagina.content)
        nombre = z["data"][num]["displayName"]
        embed = discord.Embed(title =f"Tu personaje es: {nombre} ", color=0Xe68359)    
        embed.set_image(url= img)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        print(num)
       
    else:
     
        await ctx.send("No se ha encontrado gif")

@client.command()
async def rango(ctx):
    num = random.randint(3,24)
     
    pagina = requests.get("https://valorant-api.com/v1/competitivetiers")
    if pagina.status_code == 200:
        y = json.loads(pagina.content)
        img =y["data"][1]["tiers"][num]["largeIcon"]

        z = json.loads(pagina.content)
        nombre = z["data"][1]["tiers"][num]["tierName"]
        embed = discord.Embed(title =f"Tu rango es: {nombre} ", color=0Xe68359)    
        embed.set_image(url= img)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        print(num)


@client.command()
async def quieromimi(ctx):
    await ctx.send("MIMIMIMIMIMMIMI")    


#---------------------------------------------------------- Roles-------------------------------------------------------------------------
@client.command('role')
@commands.has_permissions(administrator=True) #permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
    return await ctx.send('**:x: | ¡Ese rol está por encima del tuyo!**', delete_after=15.0) 
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Se le ha retirado el rol {role} a {user.mention}",delete_after=15.0)
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Se le añadió el rol  {role} a {user.mention}",delete_after=15.0) 


#comando para borrar mensajes
@client.command()
async def clear(ctx, amount=None):
    if ctx.message.author.guild_permissions.administrator:
        if amount == None:
            await ctx.send("Debes poner la cantidad de mensajes que quieres eliminar")
        else:

            await ctx.channel.purge(limit=int(amount))

    else:
        await ctx.send("**No tienes permiso para usar este comando**", delete_after=5.0)



@client.command()
async def perrito(ctx, men : discord.Member=None):
   
    embed= discord.Embed(title= "Perritooo",color=0xe68359)
   

    pagina = requests.get("https://dog.ceo/api/breeds/image/random")
    if pagina.status_code == 200:
        y = json.loads(pagina.content)
        img = y["message"]
        embed.set_image(url=img)
    else:
        await ctx.message.delete()
        await ctx.send("No se ha encontrado gif")
    
    await ctx.send(embed=embed)  


#COMANDOSSS EL HELP DE MIERDA JAJAJAJAJ
@client.command()
async def help(ctx):
    icon_url = str(ctx.guild.icon_url)
    embed=discord.Embed(title = "**AQUÍ ESTÁN MIS COMANDOS , MIAU **", description = "Gracias por usarme :)", color =0Xe68359)
    embed.set_thumbnail(url=f'{icon_url}')
    embed.add_field(name = "**Mis redes!**", value = "```m!redes\n```")
    embed.add_field(name = "**Comandos de moderación**", value = "```m!clear\nm!ban\nm!unban\nm!kick\nm!role\nm!alerta```")
    embed.add_field(name = "**Comandos de imagen**", value = "```m!wallpaper\nm!perrito\n```")
    embed.add_field(name = "**Comandos de valorant**", value = "```m!skin\nm!agente\nm!rango\n```", inline = False)
    embed.add_field(name = "****", value = "****")

    await ctx.send(embed = embed)




@client.command()
async def userinfo(ctx, mention : discord.Member=None):
    if mention == None:
                    user = str(client.get_user(ctx.author.id))
                    usu = ctx.author.display_name
                    user_init = ctx.author.created_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                    user_join = ctx.author.joined_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                    roles = ctx.author.roles
                    filt = roles[::-1]
                    if user[0:len(user)-5] == usu:
                        apodo = "Ninguno"
                    else:
                        apodo = ctx.author.display_name
                    final_roles = ""
                    for role in filt:
                        final_roles += "-|-<@&" + str(role.id) + ">-|-"
                    embed = discord.Embed(color=0Xe68359)
                    embed.set_author(name=f'Perfil de {ctx.author.display_name}')
                    embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
                    embed.add_field(name='Nombre y tag:', value=f'{user}')
                    embed.add_field(name='ID:', value=f'{ctx.author.id}')
                    embed.add_field(name='|', value=f'|')
                    embed.add_field(name='Apodo:', value=f'{apodo}')
                    embed.add_field(name='Rol más alto:', value=f'{roles[-1]}')
                    embed.add_field(name='|', value=f'|')
                    embed.add_field(name='Cuenta creada el:', value=f'{user_init}')
                    embed.add_field(name='En el servidor desde:', value=f'{user_join}')
                    embed.add_field(name='|', value=f'|')
                    embed.add_field(name='Roles:', value=f'{final_roles}')
                    embed.set_footer(text=f'Información pedida por {ctx.author.display_name}')
                    await ctx.send(embed=embed)
    else:
                    user = str(mention)
                    user2 = int(mention.id)
                    user3 = str(client.get_user(user2))
                    user = user[0:len(user)-5]
                    user_init = mention.created_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                    user_join = mention.joined_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                    roles = mention.roles
                    filt = roles[::-1]
                    apodo = mention.display_name
                    final_roles = ""
                    for role in filt:
                        final_roles += "-|-<@&" + str(role.id) + ">-|-"
                    embed = discord.Embed(color=0Xe68359)
                    embed.set_author(name=f'Perfil de {mention.display_name}')
                    embed.set_thumbnail(url=f'{mention.avatar_url}')
                    embed.add_field(name='Nombre y tag:', value=f'{user3}')
                    embed.add_field(name='ID:', value=f'{mention.id}')
                    embed.add_field(name='ㅤㅤ|', value=f'|')
                    embed.add_field(name='Apodo:', value=f'{apodo}')
                    embed.add_field(name='Rol más alto:', value=f'{roles[-1]}')
                    embed.add_field(name='|', value=f'|')
                    embed.add_field(name='Cuenta creada el:', value=f'{user_init}')
                    embed.add_field(name='En el servidor desde:', value=f'{user_join}')
                    embed.add_field(name='|', value=f'|')
                    embed.add_field(name='Roles:', value=f'{final_roles}')
                    embed.set_footer(text=f'Información pedida por {ctx.author.display_name}')
                    await ctx.send(embed=embed)


@client.command()
async def serverinfo(ctx):

    icon_url = str(ctx.guild.icon_url)
      
    embed = discord.Embed(color=0Xe68359)
    embed.set_thumbnail(url=f'{icon_url}')
    embed.add_field(name='Nombre del servidor:', value=f'{ctx.guild.name}')
    embed.add_field(name='ID del servidor:', value=f'{ctx.guild.id}')
    embed.add_field(name='Región:', value=f'{ctx.guild.region}', inline=True)
    embed.add_field(name='Dueño del servidor:', value=f'{ctx.guild.owner}')
    embed.add_field(name='Nivel de verificación:', value=str(ctx.guild.verification_level))
    embed.add_field(name='Estado actual:', value='En linea')
    embed.add_field(name='Miembros:', value=f'{ctx.guild.member_count}')
    embed.add_field(name='Canales y categorías:', value=f'{len(ctx.guild.channels)}')
    embed.add_field(name='Canales texto:', value=f'{len(ctx.guild.text_channels)}')
    embed.add_field(name='Canales voz:', value=f'{len(ctx.guild.voice_channels)}')
    embed.add_field(name='Roles:', value=f'{len(ctx.guild.roles)}')
    embed.add_field(name='Rol más alto:', value=f'{ctx.guild.roles[-1]}')
    embed.add_field(name='Número de emojis:', value=f'{len(ctx.guild.emojis)}')
    embed.add_field(name='Creado el:', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.add_field(name='icono del servidor:', value=f'[Icono link]({icon_url})')
    embed.set_footer(text=f'Información pedida por {ctx.author.display_name}')
    await ctx.send(embed=embed)



#Prueba música je
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="𝖛𝖔𝖟 𝖆𝖉𝖒𝖎𝖓𝖘")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()





client.run("OTExOTcxNTEwODkyMjQ1MDAy.YZpJpw.mNA-O3QTxbwgu3I0LiQVKkHjnsc")


