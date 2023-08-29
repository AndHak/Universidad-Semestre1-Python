#Ejercicio 2:
#Dada una matriz cuadrada con datos numéricos, forma un vector con los números primos que 
#se encuentran en la diagonal principal y los números Fibonacci que están en la
#diagonal secundaria. Luego, ordena este vector en orden descendente.
import random

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

matriz = []
hacer_matriz(matriz)
print("\nMatriz Original")
mostrar_matriz(matriz)

def pirmos_y_fibonaccis_diagonales(matriz):
    pirmos_y_fibonaccis_diagonales = []
    dimensiones = len(matriz)
    for fila in range(dimensiones):
        primo = matriz[fila][fila]
        if es_primo(primo):
            pirmos_y_fibonaccis_diagonales.append(primo)
        fibonacci = matriz[fila][dimensiones-fila-1]
        if es_fibonacci(fibonacci):
            pirmos_y_fibonaccis_diagonales.append(fibonacci)
    return pirmos_y_fibonaccis_diagonales
pirmos_y_fibonaccis_diagonales = pirmos_y_fibonaccis_diagonales(matriz)  
print(pirmos_y_fibonaccis_diagonales)

dimensiones = len(matriz)
for i in range(dimensiones - 1):
    for j in range(i+1, dimensiones):
        if matriz[i][i] > matriz[j][j]:
            matriz[i][i], matriz[j][j] = matriz[j][j], matriz[i][i]
        if matriz[i][-i-1] > matriz[j][-j-1]:
            matriz[i][-i-1] ,matriz[j][-j-1] = matriz[j][-j-1], matriz[i][-i-1]

print("\nCon diagonal principal ordenada ascendentemente")
mostrar_matriz(matriz)