#ordenar toda la matriz cuadrada

import random

dimensiones = random.randint(5, 10)
matriz = []

for fila in range(dimensiones):
    fila_actual = []
    for columna in range(dimensiones):
        fila_actual.append(random.randint(1, 100))
    matriz.append(fila_actual)

print("Matriz original:")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

# Ordenar la matriz usando el método de burbuja
for i in range(dimensiones * dimensiones):
    for j in range(dimensiones * dimensiones - 1):
        fila_actual = j // dimensiones
        columna_actual = j % dimensiones
        siguiente_fila = (j + 1) // dimensiones
        siguiente_columna = (j + 1) % dimensiones
        if matriz[fila_actual][columna_actual] > matriz[siguiente_fila][siguiente_columna]:
            matriz[fila_actual][columna_actual], matriz[siguiente_fila][siguiente_columna] = matriz[siguiente_fila][siguiente_columna], matriz[fila_actual][columna_actual]

print("\nMatriz ordenada:")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

#ordenar toda la matriz no cuadrada

filas = random.randint(5, 10)
columnas = random.randint(5, 10)
matriz2 = []

for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        fila_actual.append(random.randint(1,100))
    matriz2.append(fila_actual)

print("\nMatriz no cuadrada original")
for fila in matriz2:
    print(" ".join("{:4}".format(num) for num in fila))

for i in range(filas * columnas):
    for j in range(filas * columnas - 1):
        fila_actual = j // columnas
        columna_actual = j % columnas
        fila_siguiente = (j + 1) // columnas
        columna_siguiente = (j + 1) % columnas
        if matriz2[fila_actual][columna_actual] > matriz2[fila_siguiente][columna_siguiente]:
            temporal = matriz2[fila_actual][columna_actual]
            matriz2[fila_actual][columna_actual] = matriz2[fila_siguiente][columna_siguiente]
            matriz2[fila_siguiente][columna_siguiente] = temporal

print("\nMatriz no cuadrada ordenada")
for fila in matriz2:
    print(" ".join("{:4}".format(num) for num in fila))