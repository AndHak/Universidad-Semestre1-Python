import random
matriz = []
dimensiones = 5

for fila in range(dimensiones):
    fila_actual = []
    for columa in range(dimensiones):
        fila_actual.append(random.randint(1,20))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#intercambiar filas
matriz[0], matriz[4] = matriz[4], matriz[0]

print("\n")
for fila in matriz:
    print(fila)

