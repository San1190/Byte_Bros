class Comandos:
    def __init__(self):
        pass

    def Mensaje(self,ctx):
        print("El texto es:",ctx)

    def Color(self,ctx):
        print("Te gusta el color",ctx)


bot = Comandos()


txt1 = input("Escribe lo que quieras: ")
bot.Mensaje(txt1)

txt2 = input("Coloca un color: ")
bot.Color(txt2)