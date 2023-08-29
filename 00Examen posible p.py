#Ejercicio 1:
#Dada una matriz con datos numéricos, intercambia las filas donde se encuentre
#el mayor número primo y la fila donde se encuentra el menor número Fibonacci.
import random

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


def hacer_matriz(matriz):
    dimensiones = random.randint(4,6)
    for fila in range(dimensiones):
        fila_actual = []
        for columna in range(dimensiones):
            fila_actual.append(random.randint(1,15))
        matriz.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(elemento) for elemento in fila))

matriz = []
hacer_matriz(matriz)
print("\nMatriz Original")
mostrar_matriz(matriz)

def cambiar_filas(matriz):
    fibonacci_menor = float("inf")
    primo_mayor = 0
    posicion_primo_mayor = 0
    posicion_fibonacci_menor = 0
    for posicion, fila in enumerate(matriz):
        for numero in fila:
            if es_fibonacci(numero):
                if numero < fibonacci_menor:
                    fibonacci_menor = numero
                    posicion_fibonacci_menor = posicion
            if es_primo(numero):
                if numero > primo_mayor:
                    primo_mayor = numero
                    posicion_primo_mayor = posicion

    matriz[posicion_fibonacci_menor], matriz[posicion_primo_mayor] = matriz[posicion_primo_mayor], matriz[posicion_fibonacci_menor]
    print("\nMatriz con fila donde estaba")
    print(f"fibonacci menor: {fibonacci_menor} y Primo mayor: {primo_mayor}")
    mostrar_matriz(matriz)
cambiar_filas(matriz)

