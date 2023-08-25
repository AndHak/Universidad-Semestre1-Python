import random

filas_y_columnas = random.randint(2,10)
matriz = []

for fila in range(filas_y_columnas):
    fila_actual = []
    for columna in range(filas_y_columnas):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))

#para diagonal primaria
for i in range(filas_y_columnas):
    matriz[i][i] = 0

print("\n")
for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))

#para diagonal secundaria
for i in range(filas_y_columnas):
    matriz[i][-i-1] = 1

print("\n")
for fila in matriz:
    print(" ".join("{:3}".format(num) for num in fila))