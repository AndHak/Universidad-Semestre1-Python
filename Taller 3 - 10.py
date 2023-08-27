#Ordenar las columnas pares ascendentemente y las columnas impares descendentemente

import random

filas = random.randint(5, 10)
columnas = random.randint(5, 10)
matriz = []

for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        fila_actual.append(random.randint(1, 20))
    matriz.append(fila_actual)

print("\nMatriz original")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

for i in range(columnas):
    if i % 2 == 0:
        for j in range(filas - 1):
            for k in range(j + 1, filas):
                if matriz[j][i] > matriz[k][i]:
                    matriz[j][i], matriz[k][i] = matriz[k][i], matriz[j][i]
    else:
        for j in range(filas - 1):
            for k in range(j + 1, filas):
                if matriz[j][i] < matriz[k][i]:
                    matriz[j][i], matriz[k][i] = matriz[k][i], matriz[j][i]

print("\nMatriz ordenada")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))
