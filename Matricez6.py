print("Consumo de empresa ganadera")

granja_A = []
filas = 0
columnas = 0

def animales():
    animales = []
    while True:
        animal = input("Agregue un animal, presione 0 para terminar: ")
        if animal == "0":
            return animales
        else:
            animales.append(animal)
animales = animales()

def alimentos():
    alimentos = []
    while True:
        alimento = input("Ingrese el alimento, presione 0 para terminar: ")
        if alimento == "0":
            return alimentos
        else:
            alimentos.append(alimento)
alimentos = alimentos()

for fila in range(len(animales)):
    granja_A.append([])
    for columna in range(len(alimentos)):
        cantidad = int(input(f"Cuánta cantidad del alimento '{alimentos[columna]}' necesita el animal '{animales[fila]}': "))
        granja_A[fila].append(cantidad)

for i, fila in enumerate(granja_A):
    print(f"{animales[i]} [", end=" ")
    for j, elemento in enumerate(fila):
        print(f"{alimentos[j]}: {elemento}", end=" ")
    print("]")

