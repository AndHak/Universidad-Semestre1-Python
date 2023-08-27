#19.	Se tiene una matriz con datos numéricos repetidos,
# formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos

import random

matriz = []
dimensiones = random.randint(5,10)

for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

print("\nMatriz Original")
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
todoscontadores = []
contadores = []
repeticiones = {}
print("")
for fila in matriz:
    for numero in fila:
        if es_fibonacci(numero):
            if numero in repeticiones:
                repeticiones[numero] += 1
            else:
                repeticiones[numero] = 1

for numero, repeticion in repeticiones.items():
    print(f"Numero: {numero}  Repeticiones: {repeticion}")
    if repeticion > 1:
        todoscontadores.append(repeticion)
    if repeticion > 1 and repeticion not in contadores:
        contadores.append(repeticion)

print(f"\nTodos los contadores de fibonaccis que se repiten: {todoscontadores}")
print(f"Contadores de fibonaccis que se repiten sin repetidos: {contadores}")
