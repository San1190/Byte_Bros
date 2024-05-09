# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")