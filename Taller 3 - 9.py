#9.	Se tiene una matriz con datos numéricos, donde hay varios primos, determinar si el segundo primo encontrado al recorrer la matriz
#   por columnas es consecutivo con el cuarto primo encontrado.

import random

filas = random.randint(5,10)
columnas = random.randint(5,10)
matriz = []

for fila in range(filas):
    fila_actual = []
    for columa in range(columnas):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))

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

contador_primos = 0
for i in range(columnas):
    for j in range(filas):
        numero = matriz[j][i]
        if es_primo(numero):
            contador_primos += 1
            if contador_primos == 2:
                segundo_primo = numero
            if contador_primos == 4:
                cuarto_primo = numero
                break

print(f"Segundo primo encontrado: {segundo_primo}")
print(f"Cuarto primo encontrado: {cuarto_primo}")
        
#Determinar si es consecutivo

es_consecutivo = True
if segundo_primo < cuarto_primo:
    analizador = segundo_primo + 1
    while analizador < cuarto_primo:
        divisores = 0
        condicion = 1
        while condicion <= analizador: 
            if analizador % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            es_consecutivo = False
            break
        analizador += 1
    if es_consecutivo:
        print(f"El primo: {cuarto_primo} es consecutivo del {segundo_primo}")
    else:
        print(f"El primo: {segundo_primo} y el {cuarto_primo} no son consecutivos")
else:
    print(f"El primo: {segundo_primo} y el {cuarto_primo} no son consecutivos")

    