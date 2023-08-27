#17.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
#-	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
#-	Ordenar ascendentemente la diagonal principal
#-	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
#-	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
#-	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

import random

matriz = []
dimensiones = random.randint(5,10)

for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1,100))
    matriz.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

print("\nMatriz original")
mostrar_matriz(matriz)

#-	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria

suma_diagonal_principal = 0
contador_diagonal_princiapal = 0
promedio_diagonal_principal = 0
suma_diagonal_secundaria = 0
contador_diagonal_secundaria = 0
promedio_diagonal_secundaria = 0

for i in range(dimensiones):
    suma_diagonal_principal += matriz[i][i]
    contador_diagonal_princiapal += 1
    suma_diagonal_secundaria += matriz[i][-i-1]
    contador_diagonal_secundaria += 1

promedio_diagonal_principal = suma_diagonal_principal/contador_diagonal_princiapal
promedio_diagonal_secundaria = suma_diagonal_secundaria/contador_diagonal_secundaria

print(f"\nPromedio diagonal principal: {promedio_diagonal_principal:.2f}\nPromedio diagonal secundaria: {promedio_diagonal_secundaria:.2f}")

for i in range(dimensiones - 1):
    for j in range(i+1, dimensiones):
        if matriz[i][i] > matriz[j][j]:
            matriz[i][i], matriz[j][j] = matriz[j][j], matriz[i][i]

print("\nCon diagonal principal ordenada ascendentemente")
mostrar_matriz(matriz)

#-	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria

suma_pares_up_diagonal_principal = 0
contador_pares_up_diagonal_princiapal = 0
promedio_pares_up_diagonal_principal = 0
promedio_impares_diagonal_secundaria = 0
contador_impares_diagonal_secundaria = 0
suma_impares_diagonal_secundaria = 0

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False
def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

for i in range(dimensiones):
    if i < dimensiones - 1:
        if es_par(matriz[i][i+1]):
            suma_pares_up_diagonal_principal += matriz[i][i+1]
            contador_pares_up_diagonal_princiapal += 1
    if es_impar(matriz[i][-i-1]):
        suma_impares_diagonal_secundaria += matriz[i][-i-1]
        contador_impares_diagonal_secundaria += 1
if suma_pares_up_diagonal_principal == 0:
    print("No hay numeros pares en la diagonal superior de la diagonal principal")
else:
    promedio_pares_up_diagonal_principal = suma_pares_up_diagonal_principal/contador_pares_up_diagonal_princiapal
    print(f"\nPromedio pares up diagonal 1: {promedio_pares_up_diagonal_principal:.2f}")
if suma_impares_diagonal_secundaria == 0:
    print("No hay numeros impares en la diagonal secundaria")
else:
    promedio_impares_diagonal_secundaria = suma_impares_diagonal_secundaria/contador_impares_diagonal_secundaria
    print(f"Promedio impares diagonal 2: {promedio_impares_diagonal_secundaria:.2f}")

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

fibonacci_mayor = 0
primo_menor = float("inf")
par_mayor = 0
impar_menor = float("inf")

for fila in matriz:
    for numero in fila:
        if es_fibonacci(numero):
            if numero > fibonacci_mayor:
                fibonacci_mayor = numero
        if es_primo(numero):
            if numero < primo_menor:
                primo_menor = numero
        if es_par(numero):
            if numero > par_mayor:
                par_mayor = numero
        if es_impar(numero):
            if numero < impar_menor:
                impar_menor = numero

#-	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.

for i in range(dimensiones):
    matriz[i][i] = primo_menor
    matriz[i][-i-1] = fibonacci_mayor

print(f"\nMatriz con diagonal principal primo menor: {primo_menor}")
print(f"y diagonal secundaria fibonacci mayor: {fibonacci_mayor}")
mostrar_matriz(matriz)

#-	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

for i in range(dimensiones):
    for j in range(dimensiones):
        if i == 0 or i == dimensiones - 1 or j == 0 or j == dimensiones - 1:
            matriz[i][j] = par_mayor
        else:
            matriz[i][j] = impar_menor

print(f"\nMatriz con contorno par mayor: {par_mayor}")
print(f"y su interior con el impar menor: {impar_menor}")
mostrar_matriz(matriz)