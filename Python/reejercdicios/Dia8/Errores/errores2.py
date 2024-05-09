def pedir_num():
    while True:
        try:
            n = int(input("Introduce un número:"))

        except:
            print("Ese no es un número")

        else:
            print(f"Ingresaste el número {n}")
            break

    print("Gracias")


pedir_num()