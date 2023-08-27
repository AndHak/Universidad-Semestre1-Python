#Se tienen dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).

import random

def mezclar(vector1, vector2):
    resultado = []
    i = j = 0

    while i < len(vector1) and j < len(vector2):
        if vector1[i] < vector2[j]:
            resultado.append(vector1[i])
            i += 1
        else:
            resultado.append(vector2[j])
            j += 1

    resultado.extend(vector1[i:])
    resultado.extend(vector2[j:])
    return resultado

def ordenar_mezcla(vector):
    if len(vector) <= 1:
        return vector

    medio = len(vector) // 2
    izquierda = vector[:medio]
    derecha = vector[medio:]

    izquierda = ordenar_mezcla(izquierda)
    derecha = ordenar_mezcla(derecha)

    return mezclar(izquierda, derecha)

matriz1 = []
matriz2 = []
dimensiones = random.randint(3, 6)

for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1, 50))
    matriz1.append(fila_actual)

for i in range(dimensiones):
    fila_actual = []
    for j in range(dimensiones):
        fila_actual.append(random.randint(1, 50))
    matriz2.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

print("\nMatriz 1")
mostrar_matriz(matriz1)

print("\nMatriz 2")
mostrar_matriz(matriz2)

# Convertir matrices en listas planas para ordenarlas
vector1 = [numero for fila in matriz1 for numero in fila]
vector2 = [numero for fila in matriz2 for numero in fila]

vector1_ordenado = ordenar_mezcla(vector1)
vector2_ordenado = ordenar_mezcla(vector2)

print("\nVector 1 ordenado:")
print(vector1_ordenado)

print("\nVector 2 ordenado:")
print(vector2_ordenado)

# Combinar y ordenar los dos vectores utilizando el método de mezcla
resultado_combinado = mezclar(vector1_ordenado, vector2_ordenado)
print("\nResultado combinado y ordenado:")
print(resultado_combinado)
