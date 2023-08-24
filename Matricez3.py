matriz_cero = []

for i in range(10):
    matriz_cero.append([])
    for j in range(15):
        matriz_cero[i].append(0)

matriz_cero[0][-1] = 99


for fila in matriz_cero:
    print(fila)