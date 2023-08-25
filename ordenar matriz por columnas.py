#matriz ordenada por columnas

import random

dimensiones = random.randint(5,10)
matriz = []

for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1,100))
    matriz.append(fila_actual)

print("\nMatriz original")
for i in matriz:
    print(" ".join("{:4}".format(j) for j in i))

for i in range(dimensiones):
    for j in range(dimensiones - 1):
        for k in range(j + 1, dimensiones):
            if matriz[j][i] > matriz[k][i]:
                matriz[j][i], matriz[k][i] = matriz[k][i], matriz[j][i]

print("\nMatriz ordenada por columnas")
for i in matriz:
    print(" ".join("{:4}".format(j) for j in i))     
