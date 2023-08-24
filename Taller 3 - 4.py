#4.	Se tiene una matriz con datos numéricos, intercambiar las columnas donde se encuentra el primo mayor y el primo menor.

import random

filas = random.randint(3,10)
columnas = random.randint(3,10)
matriz = []

for i in range(filas):
    fila_actual = []
    for j in range(columnas):
        numero_random = random.randint(1,50)
        fila_actual.append(numero_random)
    matriz.append(fila_actual)

for fila in matriz:
    print(fila)

primo_menor = float("inf")
primo_mayor = 0

for i in range(columnas):
    for j in range(filas):
        numero = matriz[j][i]
        condicion = 1
        divisores = 0
        es_primo = False
        while condicion <= numero:
            if numero % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            es_primo = True
            if es_primo:
                if numero > primo_mayor:
                    primo_mayor = numero
                    posicion_primo_mayor = i
                if numero < primo_menor:
                    primo_menor = numero
                    posicion_primo_menor = i


print(f"Primo mayor: {primo_mayor}   posicion columna: {posicion_primo_mayor+1}")
print(f"Primo menor: {primo_menor}   posicion columna: {posicion_primo_menor+1}")

# Intercambiar columnas
for columna in matriz:
    columna[posicion_primo_mayor], columna[posicion_primo_menor] = columna[posicion_primo_menor], columna[posicion_primo_mayor]


print("Matriz después del intercambio:")
for fila in matriz:
    print(fila)




        