#Se tiene una matriz con datos numéricos, intercambiar las filas donde se encuentre el mayor y el menor de la matriz.

import random

filas = random.randint(2,8)
columnas = random.randint(2,8)
matriz = []

for i in range(filas):
    fila_actual = []
    for j in range(columnas):
        numero_random = random.randint(1,50)
        fila_actual.append(numero_random)
    matriz.append(fila_actual)

for fila in matriz:
    print(fila)

mayor = 0
menor = float("inf")

for i, fila in enumerate(matriz):
    for numero in fila:
        if numero > mayor:
            mayor = numero
            posicion_mayor = i
        if numero < menor:
            menor = numero
            posicion_menor = i

print(f"Menor: {menor}  fila: {posicion_menor+1}")
print(f"Mayor: {mayor}  fila: {posicion_mayor+1}")

#cambiar filas
matriz[posicion_mayor], matriz[posicion_menor] = matriz[posicion_menor], matriz[posicion_mayor]
for fila in matriz:
    print(fila)

