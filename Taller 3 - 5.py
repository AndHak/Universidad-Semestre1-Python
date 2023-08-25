#5.	Se tienen dos matrices con datos numéricos, formar un vector con los Fibonacci comunes de las dos matrices sin repetidos.

import random

matriz1 = []
matriz2 = []
fila = random.randint(3,10)
columna = random.randint(3,10)

for i in range(fila):
    fila_actual = []
    for j in range(columna):
        fila_actual.append(random.randint(1,50))
    matriz1.append(fila_actual)

for i in range(fila):
    fila_actual = []
    for j in range(columna):
        fila_actual.append(random.randint(1,50))
    matriz2.append(fila_actual)

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:3}".format(num) for num in fila))

print("Matriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

#Formar vector con fibonaccis comunes sin repetidos

fibonaccis_comunes_sin_repetidos = []

def es_fibonacci(numero):
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= numero:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == numero:
            return True
    return False

for fila in matriz1:
    for numero in fila:
        if es_fibonacci(numero):
            es_comun = False
            for fila2 in matriz2:
                if numero in fila2:
                    es_comun = True
                    break
            if es_comun and numero not in fibonaccis_comunes_sin_repetidos:
                fibonaccis_comunes_sin_repetidos.append(numero)


print(f"Fibonaccis comunes en las dos matrices: {fibonaccis_comunes_sin_repetidos}")