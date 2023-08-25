#Se tienen dos matrices con datos numéricos, formar un vector con los primos que están en los dos matrices sin repetidos.

import random

filas = random.randint(2,10)
columnas = random.randint(2,10)
matriz1 = []
matriz2 = []

for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        fila_actual.append(random.randint(1,50))
    matriz1.append(fila_actual)

for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        fila_actual.append(random.randint(1,50))
    matriz2.append(fila_actual)

print("")
for fila in matriz1:
    print(" ".join("{:3}".format(num) for num in fila))

print("\n")
for fila in matriz2:
    print(" ".join("{:3}".format(num) for num in fila))

def es_primo(numero):
    divisores = 0
    condicion = 1
    while condicion <= numero:
        if numero % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        return True
    return False

primos_en_ambas_matrices_sin_repetidos = []
primos_comunes_sin_repetidos = []

for fila in matriz1:
    for numero in fila:
        if es_primo(numero) and numero not in primos_en_ambas_matrices_sin_repetidos:
            primos_en_ambas_matrices_sin_repetidos.append(numero)

for fila in matriz2:
    for numero in fila:
        if es_primo(numero) and numero not in primos_en_ambas_matrices_sin_repetidos:
            primos_en_ambas_matrices_sin_repetidos.append(numero)

print(f"Primos encontrados en ambas matrices: {primos_en_ambas_matrices_sin_repetidos}")

for fila in matriz1:
    for numero in fila:
        if es_primo(numero):
            es_comun = False
            for fila2 in matriz2:
                if numero in fila2:
                    es_comun = True
                    break
            if es_comun and numero not in primos_comunes_sin_repetidos:
                primos_comunes_sin_repetidos.append(numero)

print(f"Primos comunes sin repetidos: {primos_comunes_sin_repetidos}")