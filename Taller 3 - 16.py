#16.	Se tiene una matriz con datos numéricos y se solicita
#-	Intercambia la primera columna con la última
#-	Obtener el mayor, menor y promedio de cada columna
#-	Ordenar las filas pares ascendentemente y las filas impares descendentemente
#-	Ordenar la matriz descendentemente
#-	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila
#-	Intercambiar las filas donde se encuentre el mayor y el menor de la matriz
#-	Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el Fibonacci 4.
#-	Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor
#-	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos

import random
matriz = []
dimensiones = random.randint(5,10)

for fila in range(dimensiones):
    fila_actual = []
    for columna in range(dimensiones):
        fila_actual.append(random.randint(1,50))
    matriz.append(fila_actual)

print("\nMatriz Original")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

for i in range(dimensiones):
    for j in range(dimensiones):
        if i == 0:
            matriz[j][i], matriz[j][-i-1] = matriz[j][-i-1], matriz[j][i]

print("\nCambiar primera con ultima columna")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))
print("")
contador_mayor_menor = 0
for i in range(dimensiones):
    promedio_columna = 0
    suma_columna = 0
    contador_columna = 0
    for j in range(dimensiones):
        suma_columna += matriz[j][i]
        contador_columna += 1
        contador_mayor_menor += 1
        if contador_mayor_menor == 1:
            numero_mayor = matriz[j][i]
            numero_menor = matriz[j][i]
        else:
            if numero_mayor < matriz[j][i]:
                numero_mayor = matriz[j][i]
            if numero_menor > matriz[j][i]:
                numero_menor = matriz[j][i]
    promedio_columna = suma_columna/contador_columna
    print(f"Promedio de la columna {i+1}: {promedio_columna:.2f}")
print(f"\nNumero mayor: {numero_mayor}  Numero menor: {numero_menor}")

#-	Ordenar las filas pares ascendentemente y las filas impares descendentemente

for i in range(dimensiones):
    if i % 2 == 0 and i < dimensiones - 1:
        for j in range(dimensiones - 1):
            for k in range(j + 1, dimensiones):
                if matriz[i][j] < matriz[i][k]:
                    matriz[i][j], matriz[i][k] = matriz[i][k], matriz[i][j]
    else:
        for j in range(dimensiones - 1):
            for k in range(j + 1, dimensiones):
                if matriz[i][j] > matriz[i][k]:
                    matriz[i][j], matriz[i][k] = matriz[i][k], matriz[i][j]

print("\nFilas pares e impares ordenadas")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#-	Ordenar la matriz descendentemente

for i in range(dimensiones * dimensiones):
    for j in range(dimensiones * dimensiones - i - 1):
        fila_actual = j // dimensiones
        columna_actual = j % dimensiones
        siguiente_fila = (j+1) // dimensiones
        siguiente_columna = (j+1) % dimensiones
        if matriz[fila_actual][columna_actual] > matriz[siguiente_fila][siguiente_columna]:
            matriz[fila_actual][columna_actual], matriz[siguiente_fila][siguiente_columna] = matriz[siguiente_fila][siguiente_columna], matriz[fila_actual][columna_actual]

print("\nMatriz ordenada ascendentemente")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#-	Intercambiar las filas de la matriz de acuerdo al orden ascendente de los promedios de cada fila

promedios_fila = []
for i in range(dimensiones):
    suma_fila = 0
    contador_fila = 0
    promedio_fila = 0
    for j in range(dimensiones):
        suma_fila += matriz[i][j]
        contador_fila += 1
    promedio_fila = suma_fila/contador_fila
    promedios_fila.append(promedio_fila)

for i in range(len(promedios_fila)):
    for j in range(len(promedios_fila)- i - 1):
        if promedios_fila[j] < promedios_fila[j+1]:
            promedios_fila[j], promedios_fila[j+1] = promedios_fila[j+1], promedios_fila[j]
            matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

print("\nMatriz ordenada con promedios")
for i, fila in enumerate(matriz):
    print(" ".join("{:4}".format(n) for n in fila),f"  Promedio fila {i+1}: {promedios_fila[i]:.2f}")

#-	Intercambiar las filas donde se encuentre el mayor y el menor de la matriz

contador_mayor_menor = 0
for i, fila in enumerate(matriz):
    for numero in fila:
        contador_mayor_menor += 1
        if contador_mayor_menor == 1:
            numero_mayor = numero
            posicion_numero_mayor = i
            numero_menor = numero
            posicion_numero_menor = i
        else:
            if numero_mayor < numero:
                numero_mayor = numero
                posicion_numero_mayor = i
            if numero_menor > numero:
                numero_menor = numero
                posicion_numero_menor = i

matriz[posicion_numero_mayor], matriz[posicion_numero_menor] = matriz[posicion_numero_menor], matriz[posicion_numero_mayor]

print("\nMatriz con filas numero mayor y menor cambiadas")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#-	Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.

def es_fibonacci(numero):
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= numero:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == numero:
            return True
    return False

fibonacci_mayor = 0
fibonacci_menor = float("inf")
for i, fila in enumerate(matriz):
    for numero in fila:
        if es_fibonacci(numero):
            if numero > fibonacci_mayor:
                fibonacci_mayor = numero
                posicion_fibonacci_mayor = i
            if numero < fibonacci_menor:
                fibonacci_menor = numero
                posicion_fibonacci_menor = i

matriz[posicion_fibonacci_mayor], matriz[posicion_fibonacci_menor] = matriz[posicion_fibonacci_menor], matriz[posicion_fibonacci_mayor]

print(f"\nCon fila fibonacci mayor: {fibonacci_mayor} y menor: {fibonacci_menor} cambiadas")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#-	Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor

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

primo_mayor = 0
fibonacci_menor = float("inf")

for i, fila in enumerate(matriz):
    for numero in fila:
        if es_primo(numero):
            if numero > primo_mayor:
                primo_mayor = numero
                posicion_primo_mayor = i
        if es_fibonacci(numero):
            if numero < fibonacci_menor:
                fibonacci_menor = numero
                posicion_fibonacci_menor = i

matriz[posicion_fibonacci_menor], matriz[posicion_primo_mayor] = matriz[posicion_primo_mayor], matriz[posicion_fibonacci_menor]

print(f"\nCon fila fibonacci menor: {fibonacci_menor} con primo mayor: {primo_mayor} cambiadas")
for fila in matriz:
    print(" ".join("{:4}".format(n) for n in fila))

#-	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos

contador_primos = 0
for i in range(dimensiones):
    for j in range(dimensiones):
        if es_primo(matriz[i][j]):
            contador_primos += 1
            if contador_primos == 2:
                segundo_primo = matriz[i][j]
            if contador_primos == 4:
                cuarto_primo = matriz[i][j]
                break

if segundo_primo < cuarto_primo:
    es_consecutivo = True
    contador = segundo_primo + 1
    while contador < cuarto_primo:
        condicion = 1
        divisores = 0
        while condicion <= contador:
            if contador % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            es_consecutivo = False
            break
        contador += 1
    if es_consecutivo:
        print(f"El primo: {cuarto_primo} si es consecutivo del segundo primo: {segundo_primo}")
else:
    print(f"El primo: {cuarto_primo} no es consecutivo del segundo primo: {segundo_primo}")

