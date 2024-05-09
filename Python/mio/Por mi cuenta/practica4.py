


weight = input("¿Cuál es tu peso en kg? ")
height = input("¿Cuál es tu estatura en metros?")
bmi = round(float(weight)/float(height)**2,2)
print("Tu índice de masa corporal es " + str(bmi))