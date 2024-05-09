horas = float(input("¿Cuantas horas trabajas?"))
pago = float(input("¿Cuanto te pagan por hora?"))
dinero=round(horas*pago)
print(("Te pagan: ")+str(dinero))

if dinero<1000:
    print("Eres un puto pobre")
elif dinero>1000:
    print("Cobras bien")
if dinero == 1000:
    print("Estás en el límite de ser un pobre")
