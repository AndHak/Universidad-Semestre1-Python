#Se tiene una matriz cuadrada con datos numéricos, Comparar el promedio de los números pares que están sobre la diagonal principal
#con el promedio de los impares de los datos que están bajo la diagonal principal.

import random

filas_y_columas = random.randint(2,10)
matriz = []

for fila in range(filas_y_columas):
    fila_actual = []
    for columna in range(filas_y_columas):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

def es_impar(numero):
    if numero % 2 != 0:
        return True
    return False

#Promedio de pares diagonal principal
suma_pares = 0
contador_pares = 0
promedio_pares = 0
for i in range(filas_y_columas):
    if es_par(matriz[i][i]):
        suma_pares += matriz[i][i]
        contador_pares += 1
promedio_pares = suma_pares/contador_pares
print(f"El promedio de los pares de la diagonal principal es: {suma_pares} / {contador_pares} = {promedio_pares:.2f}")


#promedio de impares diagonal bajo diagonal principal
suma_impares = 0
contador_impares = 0
promedio_impares = 0
for i in range(filas_y_columas):
    if i < filas_y_columas - 1: #Aqui es importante no considerar una ultima fila y columna que no existe porque vamos a recorrer los elementos bajo la diagonal principal con i+1
        if es_impar(matriz[i+1][i]): #si no ponemos la condicion anterior se saldra del rango
            suma_impares += matriz[i+1][i]
            contador_impares += 1
promedio_impares = suma_impares/contador_impares

print(f"El promedio de los impares diagonal bajo diagonal principal es: {suma_impares} / {contador_impares} = {promedio_impares:.2f}")

if promedio_pares > promedio_impares:
    print(f"El promedio de los pares: {promedio_pares} es mayor que el promedio de los impares: {promedio_impares}")
elif promedio_impares > promedio_pares:
    print(f"El promedio de los pares: {promedio_pares} es menor que el promedio de los impares: {promedio_impares}")
else:
    print(f"El promedio de los pares: {promedio_pares} es igual que el promedio de los impares: {promedio_impares}")