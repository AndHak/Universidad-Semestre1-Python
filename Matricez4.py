filas = int(input("Ingrese el numero de filas de la matriz: "))
columnas = int(input("Ingrese el numero de columas de la matriz: "))
matriz = []
#for i in range(filas):
    #matriz.append([0] * columnas)

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        num = int(input("Fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(num)

for fila in matriz:
    print(fila)