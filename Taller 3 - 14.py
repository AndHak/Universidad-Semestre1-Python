#14.	Se tienen dos matrices con datos numéricos y se solicita;
#    -	Formar un vector con los elementos comunes de las dos matrices sin repetidos
#   -	Formar un vector con los primos comunes de las dos matrices sin repetidos
#  -	Formar un vector con los primos no comunes de las dos matrices sin repetidos

import random

matriz1 = []
matriz2 = []

for i in range(random.randint(3,5)):
    fila_actual = []
    for j in range(random.randint(3,5)):
        fila_actual.append(random.randint(1,50))
    matriz1.append(fila_actual)

for i in range(random.randint(3,5)):
    fila_actual = []
    for j in range(random.randint(3,5)):
        fila_actual.append(random.randint(1,50))
    matriz2.append(fila_actual)

print("\nMatriz 1")
for i in matriz1:
    print(" ".join("{:4}".format(num) for num in i))

print("\nMatriz 2")
for i in matriz2:
    print(" ".join("{:4}".format(num) for num in i))

primos_comunes = []
numeros_comunes = []
primos_no_comunes = []

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

#    -	Formar un vector con los elementos comunes de las dos matrices sin repetidos y primos comunes

for fila in matriz1:
    for i in fila:
        for fila2 in matriz2:
            if i in fila2 and i not in numeros_comunes:
                numeros_comunes.append(i)
        if es_primo(i):     
            for fila2 in matriz2:
                if i in fila2 and i not in primos_comunes:
                    primos_comunes.append(i)

# Formar un vector con los primos no comunes de las dos matrices sin repetidos

for fila in matriz1:
    for i in fila:
        if es_primo(i):
            primo_no_comun = True
            for fila2 in matriz2:
                if i in fila2:
                    primo_no_comun = False
                    break
            if primo_no_comun and i not in primos_no_comunes:
                primos_no_comunes.append(i)

for fila2 in matriz2:
    for j in fila2:
        if es_primo(j):
            primo_no_comun = True
            for fila in matriz1:
                if j in fila:
                    primo_no_comun = False
                    break
            if primo_no_comun and j not in primos_no_comunes:
                primos_no_comunes.append(j)

print(f"\nNúmeros comunes en las dos matrices: {numeros_comunes}")
print(f"Primos comunes en las dos matricez: {primos_comunes}")
print(f"Primos no comunes en ambas matrices: {primos_no_comunes}")


