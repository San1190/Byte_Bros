
from twitchio.ext import commands



bot = commands.Bot(
     irc_token= "oauth:9ju8bgk5b1m93uwxr54dvq761ox8mj",
     client_id = "xmo32d7ynohuxw2vwf3s9ei5irazal",
     client_secret = "p6ylcf6h5cr2zms9qt2rjj237ih9w7",
     nick= "ChomusukeBot",
     prefix= "c!",
     initial_channels= ["martushkaaa"]
 )


@bot.event
async def event_ready():
    print("conectado")

@bot.command(name = "siguiendodesde")
async def followage(ctx):
    info = await bot.get_follow(from_id=ctx.author.id,to_id="tu id") #para tener tu id escribe !id desde tu cuenta donde vas a hacer directo
    follow_info = info["followed_at"]
    siguiendo_desde = (follow_info[:10])
    await ctx.send(f"{ctx.author.name} es seguidor desde {siguiendo_desde}")

@bot.command(name = "id")# lo puedes borrar despues de obtener tu id
async def id(ctx):
    print(ctx.author.id)


bot.run()