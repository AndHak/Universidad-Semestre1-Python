#18.	Se tienen dos matrices con datos numéricos y se solicita;
#-	Formar un vector con los elementos comunes de las dos matrices sin repetidos
#-	Formar un vector con los primos comunes de las dos matrices sin repetidos
#-	Formar un vector con los primos no comunes de las dos matrices sin repetidos

import random
matriz1 = []
matriz2 = []

def llenar_matriz(matriz):
    dimensiones = random.randint(5,6)
    for fila in range(dimensiones):
        fila_actual = []
        for columna in range(dimensiones):
            fila_actual.append(random.randint(1,50))
        matriz.append(fila_actual)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join("{:4}".format(n) for n in fila))

llenar_matriz(matriz1)
llenar_matriz(matriz2)
print("\nMatriz 1")
mostrar_matriz(matriz1)
print("\nMatriz 2")
mostrar_matriz(matriz2)

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

numeros_comunes = []
primos_comunes = []

for fila in matriz1:
    for numero in fila:
        if es_primo(numero):
            for fila2 in matriz2:
                if numero in fila and numero not in primos_comunes:
                    primos_comunes.append(numero)
        for fila2 in matriz2:
            if numero in fila and numero not in numeros_comunes:
                numeros_comunes.append(numero)

print(f"\nNumeros comunes: {sorted(numeros_comunes)}")
print(f"Primos comunes: {sorted(primos_comunes)}")

primos_no_comunes = []

for fila in matriz1:
    for numero in fila:
        if es_primo(numero):
            es_comun = True
            for fila2 in matriz2:
                if numero in fila2:
                    es_comun = False
                    break
            if es_comun and numero not in primos_no_comunes:
                primos_no_comunes.append(numero)
for fila2 in matriz2:
    for numero in fila2:
        if es_primo(numero):
            es_comun = True
            for fila in matriz1:
                if numero in fila:
                    es_comun = False
                    break
            if es_comun and numero not in primos_no_comunes:
                primos_no_comunes.append(numero)

print(f"Primos no comunes en las matricez: {sorted(primos_no_comunes)}")