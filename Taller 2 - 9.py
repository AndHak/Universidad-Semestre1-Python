#9.	Se tiene un vector con datos numéricos, formar dos vectores uno con los números pares
#y otro con los números primos y ordenarlos ascendente y descendente respectivamente. 

numeros = [2, 3, 5, 75, 59, 61, 67, 71, 89, 97, 11, 13, 17, 19, 23, 29, 31, 28, 6 , 7, 8, 99, 22, 24, 44, 66, 64, 75, 37, 41, 43, 47]
pares = []
primos = []

for i in numeros:
    condicion = 1
    divisores = 0
    while condicion <= i:
        if i % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos.append(i)
    if i % 2 == 0:
        pares.append(i)

#Orden ascendente

for i in range(len(primos)-1):
    for j in range(len(primos)-i-1):
        if primos[j] > primos[j+1]:
            temporal = primos[j]
            primos[j] = primos[j+1]
            primos[j+1] = temporal
print("primos", primos)

for i in range(len(pares)-1):
    for j in range(len(pares)-i-1):
        if pares[j] > pares[j+1]:
            temporal = pares[j]
            pares[j] = pares[j+1]
            pares[j+1] = temporal
print("Pares", pares)

#Orden descendente

for i in range(len(primos)-1):
    for j in range(len(primos)-i-1):
        if primos[j] < primos[j+1]:
            temporal = primos[j]
            primos[j] = primos[j+1]
            primos[j+1] = temporal
print("primos", primos)

for i in range(len(pares)-1):
    for j in range(len(pares)-i-1):
        if pares[j] < pares[j+1]:
            temporal = pares[j]
            pares[j] = pares[j+1]
            pares[j+1] = temporal
print("Pares", pares)


