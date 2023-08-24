#1.	Se tiene una matriz con datos numéricos repetidos, determinar los datos que más se repiten.

import random

matriz1 = []

filas = random.randint(2,8)
columnas = random.randint(2,8)

for fila in range(filas):
    fila_actual = []
    for elemento in range(columnas):
        numero_random = random.randint(1,10)
        fila_actual.append(numero_random)
    matriz1.append(fila_actual)
print("")
for fila in matriz1:
    print(fila)

def contar_repeticiones(matriz):
    repeticiones = {}
    for fila in range(filas):
        for elemento in matriz[fila]:
            if elemento in repeticiones:
                repeticiones[elemento] += 1
            else:
                repeticiones[elemento] = 1
    return repeticiones

matriz = contar_repeticiones(matriz1)

max_repeticiones = 0
numero_mas_repeticiones = None

min_repeticiones = float("inf")
numero_menos_repeticiones = None

for numero, repeticiones in matriz.items():
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        numero_mas_repeticiones = numero
    if repeticiones < min_repeticiones:
        min_repeticiones = repeticiones
        numero_menos_repeticiones = numero
    print(f"Numero: {numero}    Repeticiones: {repeticiones}" )


print(f"\nEl numero que mas se repite es: {numero_mas_repeticiones} con {max_repeticiones} repeticones")
print(f"\nEl numero que menos se repite es: {numero_menos_repeticiones} con {min_repeticiones} repeticiones")