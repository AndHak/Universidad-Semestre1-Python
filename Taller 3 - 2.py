#2.	Se tiene una matriz con datos numéricos determinar el mayor, menor y promedio de cada columna.

import random

filas = random.randint(3, 8)
columnas = random.randint(3, 8)
matriz = []

for fila in range(filas):
    fila_actual = []
    for elemento in range(columnas):
        numero_random = random.randint(1, 20)
        fila_actual.append(numero_random)
    matriz.append(fila_actual)

for fila in matriz:
    print(fila)

numero_mayor = 0
numero_menor = float("inf")

#Para recorrer la matriz
for fila in matriz:
    for numero in fila:
        if numero > numero_mayor:
            numero_mayor = numero
        if numero < numero_menor:
            numero_menor = numero

print(f"Numero menor de toda la matriz: {numero_menor}")
print(f"Numero mayor de toda la matriz: {numero_mayor}")

#Para recorrer columnas
for i in range(columnas):
    numero_mayor_columna = 0
    numero_menor_columna = float("inf")
    suma = 0
    contador = 0
    for j in range(filas):
        numero = matriz[j][i]
        suma += numero
        contador += 1
        if numero > numero_mayor_columna:
            numero_mayor_columna = numero
        if numero < numero_menor_columna:
            numero_menor_columna = numero
    promedio = suma/contador
    print(f"Promedio: {promedio:.2f}")
    print(f"El número menor de la columna {i+1} es el número: {numero_menor_columna}")
    print(f"El número mayor de la columna {i+1} es el número: {numero_mayor_columna}")

