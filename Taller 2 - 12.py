#12.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.

import random

array1 = [random.randint(1, 100) for n in range(50)]
array2 = [random.randint(1, 100) for n in range(50)]
primos1 = []
primos2 = []
for i in array1:
    condicion = 1
    divisores = 0
    while condicion <= i:
        if i % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos1.append(i)
for i in array2:
    condicion = 1
    divisores = 0
    while condicion <= i:
        if i % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos2.append(i)
primos_comunes = [n for n in primos2 if n in primos2 and n in primos1]
primos_comunes_sin_repetirse = []
for i in primos_comunes:
    if i not in primos_comunes_sin_repetirse:
        primos_comunes_sin_repetirse.append(i)
print('Primos comunes sin repetirse')
print(primos_comunes_sin_repetirse)
