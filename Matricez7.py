import random

# Definir el tamaño de la matriz
filas = random.randint(3,10)
columnas = random.randint(3,10)

# Crear una matriz vacía
matriz = []

# Llenar la matriz con valores aleatorios en un rango específico
for fila in range(filas):
    fila_actual = []
    for columna in range(columnas):
        valor_aleatorio = random.randint(1, 10)  # Cambia el rango según tus necesidades
        fila_actual.append(valor_aleatorio)
    matriz.append(fila_actual)

# Imprimir la matriz
for fila in matriz:
    print(fila)
