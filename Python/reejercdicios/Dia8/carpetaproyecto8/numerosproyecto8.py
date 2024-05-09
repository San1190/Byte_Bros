#generadores


def Cosmetica():
    for n in range(1, 10000):
        yield f"C-{n}"



def Farmacia():
  for n in range(1, 10000):
        yield f"F-{n}"




def Perfueria():
   for n in range(1, 10000):
        yield f"P-{n}"




f = Farmacia()
c = Cosmetica()
p = Perfueria()

def Decorar(num):
    print("\n" + "*" * 23)
    print("Su número es: ")

    if num == 1:
       
        print(next(f))

    elif num == 2:
        
        print(next(c))

    elif num == 3:
        
        print(next(p))

    print("Tome asiento, Gracias")
    print("\n" + "*" * 23)


