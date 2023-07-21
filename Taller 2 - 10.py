#10.	Se tiene un vector con datos numéricos ordenados y repetidos
#mostrar los números y las veces que se repiten utilizando el concepto de rompimiento de control.

import random

numeros = [random.randint(1, 10) for n in range(20)]

for i in range(len(numeros) - 1):
    for j in range(len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print(numeros)

contador_actual = 1
for i in range(1, len(numeros)):
    if numeros[i] == numeros[i - 1]:
        contador_actual += 1
    else:
        print(f"Número", numeros[i - 1], "Repeticiones:", contador_actual)
        contador_actual = 1

print(f"Número", numeros[-1], "Repeticiones:", contador_actual)


