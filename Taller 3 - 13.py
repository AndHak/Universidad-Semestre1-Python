#	Se tiene una matriz cuadrada de orden N realizar lo siguiente
#    -	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
#    -	Ordenar ascendentemente la diagonal principal
#    -	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
#    -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
#    -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

import random

dimensiones = random.randint(5,10)
matriz = []
matriz2 = matriz

for fila in range(dimensiones):
    fila_actual = []
    for columna in range(dimensiones):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

print("\nMatriz original")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

#promedio diagonal principal y secundaria

promedio_diagonal_primaria = 0
promedio_diagonal_secundaria = 0
suma_diagonal_primaria = 0
suma_diagonal_secundaria = 0
contador = 0
for i in range(dimensiones):
    suma_diagonal_primaria += matriz[i][i]
    suma_diagonal_secundaria += matriz[i][-i-1]
    contador += 1

promedio_diagonal_primaria = suma_diagonal_primaria/contador
promedio_diagonal_secundaria = suma_diagonal_secundaria/contador


print(f"\nPromedio diagonal 1: {promedio_diagonal_primaria:.2f}")
print(f"Promedio diagonal 2: {promedio_diagonal_secundaria:.2f}")

#ordenar ascendentemente la diagonal principal

for i in range(dimensiones - 1):
    for j in range(i + 1, dimensiones):
        if matriz[i][i] > matriz[j][j]:
            matriz[i][i], matriz[j][j] = matriz[j][j], matriz[i][i]

print("\nCon diagonal primaria ordenada")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

#Promedio pares e impares diagonales

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

promedio_pares_up_diagonal_primaria = 0
promedio_impares_diagonal_secundaria = 0
contador_pares = 0
contador_impares = 0
suma_pares_up_diagonal_primaria = 0
suma_impares_diagonal_secundaria = 0

for i in range(dimensiones):
    if i < dimensiones - 1:
        if es_par(matriz[i][i+1]):
            suma_pares_up_diagonal_primaria += matriz[i][i+1]
            contador_pares += 1
if suma_pares_up_diagonal_primaria == 0 and contador_pares == 0:
    promedio_pares_up_diagonal_primaria = 0
else:
    promedio_pares_up_diagonal_primaria = suma_pares_up_diagonal_primaria/contador_pares
print(f"\nEl promedio de los pares de up diagonal principal: {promedio_pares_up_diagonal_primaria:.2f}")

for i in range(dimensiones):
    if es_impar(matriz[i][-i-1]):
        suma_impares_diagonal_secundaria += matriz[i][-i-1]
        contador_impares += 1
if suma_impares_diagonal_secundaria == 0 and contador_impares == 0:
    promedio_impares_diagonal_secundaria = 0
else:
    promedio_impares_diagonal_secundaria = suma_impares_diagonal_secundaria/contador_impares
print(f"El promedio de impares de la diagonal secundaria: {promedio_impares_diagonal_secundaria:.2f}")

#LLenar diagonal primaria con primo menor y secundaria con fibonacci mayor

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
        num2 =secuencia
        if secuencia == numero:
            return True
    return False

fibonacci_mayor = 0
contador_fibonaccis = 0
contador_primos = 0
primo_menor = float("inf")

for fila in matriz:
    for numero in fila:
        if es_fibonacci(numero):
            contador_fibonaccis = 1
            if contador_fibonaccis == 1:
                fibonacci_mayor = numero
            else:
                if numero > fibonacci_mayor:
                    fibonacci_mayor = numero
        if es_primo(numero):
            contador_primos += 1
            if contador_primos == 1:
                primo_menor = numero
            else:
                if numero < primo_menor:
                    primo_menor = numero

print(f"\nEl fibonacci mayor de la matriz es: {fibonacci_mayor}")
print(f"El primo menor de la matriz es: {primo_menor}")

#Sustituir la diagonal primaria y secundaria por el primo menor y fibonacci mayor

for i in range(dimensiones):
    matriz[i][i] = primo_menor
    matriz[i][-i-1] = fibonacci_mayor

print("\nCon la diagonal primaria y secundaria sustituida")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

#Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

impar_menor = float("inf")
par_mayor = 0

for fila in matriz2:
    for numero in fila:
        if es_impar(numero):
            if numero < impar_menor:
                impar_menor = numero
        if es_par(numero):
            if numero > par_mayor:
                par_mayor = numero

print(f"\nPar mayor: {par_mayor} Impar menor: {impar_menor}")

for fila in range(dimensiones):
    for numero in range(dimensiones):
        matriz[numero][fila] = impar_menor

for i in range(dimensiones):
    for j in range(dimensiones):
        if i == 0:
            matriz[i][j] = par_mayor
            matriz[j][i] = par_mayor
        if i == dimensiones - 1:
            matriz[i][j] = par_mayor
            matriz[j][i] = par_mayor

#for fila in range(dimensiones):
#   for numero in range(dimensiones):
#        if fila == 0 or fila == dimensiones - 1 or numero == 0 or numero == dimensiones - 1:
#            matriz[fila][numero] = par_mayor
#        else:
#            matriz[fila][numero] = impar_menor

print("\nContorno e interno con par e impar")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))