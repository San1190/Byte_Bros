
from random import choice 
import random

def CaraRandom():
    num = random.randint(1,2)

    if num == 1:
        print("Cara")
    elif num == 2:
        print("Cruz")




def CaraLista():
    moneda = ['Cara', 'Cruz']

    sol = choice(moneda)


    print(sol)


CaraRandom()
CaraLista()
