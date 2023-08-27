#15.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos

import random
matriz = []
dimensiones = random.randint(5,10)

for fila in range(dimensiones):
    fila_actual = []
    for columna in range(dimensiones):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

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

print("")

def contar_repeticiones(matriz):
    repeticiones = {}
    for fila in range(dimensiones):
        for numero in matriz[fila]:
            if numero in repeticiones:
                repeticiones[numero] += 1
            else:
                repeticiones[numero] = 1
    return repeticiones
matriz = contar_repeticiones(matriz)
contadores_fibonaccis = []
for numero, repeticiones in matriz.items():
    if es_fibonacci(numero):
        if repeticiones > 1 and repeticiones not in contadores_fibonaccis:
            contadores_fibonaccis.append(repeticiones)
        print(f"Numero: {numero}  Repeticiones:  {repeticiones}")

print(f"\nContadores de numeros fibonacci que se repiten en la matriz\n {contadores_fibonaccis}")
