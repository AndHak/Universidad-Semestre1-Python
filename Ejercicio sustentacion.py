#Hallar el primo mayor de las filas impares de la matriz
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

def hacer_matriz(matriz):
    dimensiones = random.randint(4,6)
    for fila in range(dimensiones):
        fila_actual = []
        for columna in range(dimensiones):
            fila_actual.append(random.randint(1,15))
        matriz.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

def mostrar_primos_filas_impares(matriz):
    primos_filas_impares = []
    for fila in range(len(matriz)):
        if fila % 2 == 0:
            primo_mayor = 0
            for columna in range(len(matriz)):
                numero = matriz[fila][columna]
                if es_primo(numero):
                    if numero > primo_mayor:
                        primo_mayor = numero
            primos_filas_impares.append(primo_mayor)
    print(primos_filas_impares)

matriz = []
hacer_matriz(matriz)
print("\nMatriz Original")
mostrar_matriz(matriz)
print("\nMatriz con primo mayor de las filas impares")
mostrar_matriz(matriz)
mostrar_primos_filas_impares(matriz)
