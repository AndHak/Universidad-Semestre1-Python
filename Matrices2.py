matriz_cero = []

for i in range(5):
    matriz_cero.append([0] * 10)

matriz_cero[0][0] = 1
matriz_cero[0][1] = 2
matriz_cero[1][0] = 3
matriz_cero[1][1] = 4

for fila in matriz_cero:
    print(fila)
    