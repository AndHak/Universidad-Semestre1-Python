matriz_cero = []

for i in range(10):
    fila = []  # Crear una fila vacía para cada iteración
    for j in range(15):
        fila.append(0)  # Agregar ceros a la fila
    matriz_cero.append(fila)  # Agregar la fila a la matriz



matriz_cero[0][-1] = 99


for fila in matriz_cero:
    print(fila)