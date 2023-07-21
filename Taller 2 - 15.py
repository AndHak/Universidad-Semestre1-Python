#15.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente
#y el otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma que
#quede ordenado descendentemente, solo con números pares.

#Random arrays
import random
numeros1 = []
numeros2 = []
for i in range(20):
    num = random.randint(1,30)
    numeros1.append(num)
for i in range(20):
    num = random.randint(1,30)
    numeros2.append(num)
print(numeros1)
print(numeros2)
#orden ascendente para uno using burblesort
print('ORDENADOS')
for i in range(len(numeros1)-1):
    for j in range(len(numeros1)-i-1):
        if numeros1[j] > numeros1[j+1]:
            temporal = numeros1[j]
            numeros1[j] = numeros1[j+1]
            numeros1[j+1] = temporal
print(numeros1)
#orden descendente para otro using burblesort
for i in range(len(numeros2)-1):
    for j in range(len(numeros2)-i-1):
        if numeros2[j] < numeros2[j+1]:
            temporal = numeros2[j]
            numeros2[j] = numeros2[j+1]
            numeros2[j+1] = temporal
print(numeros2)
#Tercer vector de Pares con orden descendente
print('ARRAY DE PARES CON ORDEN DESCENDENTE')
vector = []
for i in numeros1:
    if i % 2 == 0:
        vector.append(i)
for i in numeros2:
    if i % 2 == 0:
        vector.append(i)
#Ordenar vector usando QuickSort
def particionado(vector):
    pivote = vector[0]
    menores = []
    mayores = []
    for i in range(1, len(vector)):
        if vector[i] < pivote:
            menores.append(vector[i])
        else:
            mayores.append(vector[i])
    return menores, pivote, mayores
def quicksort_descendente(vector):
    if len(vector) < 2:
        return vector
    menores, pivote, mayores = particionado(vector)
    return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)
resultado = quicksort_descendente(vector)
print(resultado)
#Ordenar array using QuickSort
print('ARRAY DE PARES CON ORDEN ASCENDENTE')
def quicksort_ascendente(vector):
    if len(vector) < 2:
        return vector
    menores, pivote, mayores = particionado(vector)
    return quicksort_ascendente(menores) + [pivote] + quicksort_ascendente(mayores)
resultado = quicksort_ascendente(vector)
print(resultado)