#Se tiene una matriz cuadrada con datos numéricos, formar un vector con los primos que se encuentran en la diagonal principal y la diagonal secundaria.

import random

filas_y_columnas = random.randint(2,10)
matriz = []

for fila in range(filas_y_columnas):
    fila_actual = []
    for columna in range(filas_y_columnas):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))

def es_primo(numero):
    condicion = 1
    divisores = 0
    while condicion <= numero:
        if numero % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        return True
    return False

#para diagonal primaria, buscar primos
primos = []
for i in range(filas_y_columnas):
    if es_primo(matriz[i][i]):
        primos.append(matriz[i][i])
    if es_primo(matriz[i][-i - 1]):
        primos.append(matriz[i][-i - 1])

print(f"primos en la diagonal primaria y secundaria: {primos}")