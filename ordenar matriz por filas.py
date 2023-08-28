import random

filas = random.randint(5,10)
columnas = random.randint(5,10)
matriz = []

for fila in range(filas):
    fila_actual = []
    for columa in range(columnas):
        fila_actual.append(random.randint(1,100))
    matriz.append(fila_actual)

print("\nMatriz original")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))

#ordenar
for i in range(filas):
    for j in range(columnas - 1):
        for k in range(j+1, columnas):
            if matriz[i][j] > matriz[i][k]:
                matriz[i][j], matriz[i][k] = matriz[i][k], matriz[i][j]

print("\nOrdenada por filas")
for fila in matriz:
    print(" ".join("{:4}".format(num) for num in fila))