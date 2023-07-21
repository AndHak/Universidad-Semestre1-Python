#14.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente
#y el otro ordenado descendentemente, formar un tercer vector por mezcla
#de tal forma que quede ordenado descendentemente.

#Random arrays
import random
numbers1 = []
numbers2 = []
for i in range(20):
    num = random.randint(1,30)
    numbers1.append(num)
for i in range(20):
    num = random.randint(1,30)
    numbers2.append(num)
print(numbers1)
print(numbers2)
#Formar QuickSort para llamar a las funciones
#Particionado
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
#Definir Quicksort para ascendente y descedente
def quicksort_ascendente(vector):
    if len(vector) < 2:
        return vector
    menores, pivote, mayores = particionado(vector)
    return quicksort_ascendente(menores) + [pivote] + quicksort_ascendente(mayores)
#Quicksort descendente
def quicksort_descendente(vector):
    if len(vector) < 2:
        return vector
    menores, pivote, mayores = particionado(vector)
    return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)
#Una vez determinadas las respectivas funciones sera mas facil llamarlas para ordenar vectores, algo mas parecido a usar sort
print('UNION DE LOS ANTERIORES VECTORES')
numbers3 = numbers1 + numbers2
print(numbers3)
vector = numbers3
resultado = quicksort_ascendente(vector)
print('VECTOR ORDENADO DE FORMA ASCENDENTE')
print(resultado)
print('VECTOR ORDENADO DE FORMA DESCENDENTE')
resultado = quicksort_descendente(vector)
print(resultado)
