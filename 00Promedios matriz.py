import random

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


def hacer_matriz(matriz):
    dimensiones = random.randint(4,6)
    for fila in range(dimensiones):
        fila_actual = []
        for columna in range(dimensiones):
            fila_actual.append(random.randint(1,15))
        matriz.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(elemento) for elemento in fila))

matriz = []
hacer_matriz(matriz)
print("\nMatriz Original")
mostrar_matriz(matriz)

def matriz_promedios_fila(matriz):
    promedios = []
    for fila in range(len(matriz)):
        suma_fila = 0
        promedio_fila = 0
        contador_fila = 0
        for columna in range(len(matriz)):
            numero = matriz[fila][columna]
            suma_fila += numero
            contador_fila += 1
        promedio_fila = suma_fila/contador_fila
        promedios.append(promedio_fila)
    return promedios
promedios = matriz_promedios_fila(matriz)

print("matriz con promedios")
for i, fila in enumerate(matriz):
        print(" ".join("{:4}".format(elemento) for elemento in fila),f"  Promedio:  {promedios[i]}")

def matriz_promedios_columna(matriz):
    promedios = []
    for fila in range(len(matriz)):
        suma_columna = 0
        promedio_columna = 0
        contador_columna = 0
        for columna in range(len(matriz)):
            numero = matriz[columna][fila]
            suma_columna += numero
            contador_columna += 1
        promedio_columna = suma_columna/contador_columna
        promedios.append(promedio_columna)
    return promedios
promedios = matriz_promedios_columna(matriz)
print(promedios)

def matriz_promedio(matriz):
    promedio = 0
    suma = 0
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            suma += matriz[i][j]
            contador += 1
    promedio = suma/contador
    return promedio
promedio = matriz_promedio(matriz)
print(promedio)