#12.	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila

import random

filas = random.randint(5,10)
columnas = random.randint(5,10)
matriz = []

for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

promedios = []
for i in range(filas):
    suma = 0
    promedio = 0
    contador = 0
    for j in range(columnas):
        suma += matriz[i][j]
        contador += 1
    promedio = suma/contador
    promedios.append(promedio)

for i, fila in enumerate(matriz):
    print(" ".join("{:4}".format(num) for num in fila),f" Promedio fila: {promedios[i]:.2f}")

#Matriz ordenada respecto a los promedios

for i in range(len(promedios)):
    for j in range(len(promedios)-i-1):
        if promedios[j] > promedios[j+1]:
            promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
            matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

print("\n")
for i, fila in enumerate(matriz):
    print(" ".join("{:4}".format(num) for num in fila),f" Promedio fila: {promedios[i]:.2f}")