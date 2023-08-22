#4.	Se tiene un vector ordenado con datos numéricos, insertar varios datos en la posición que le corresponde

array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10]

array1 += array2

lista = array1

#BurbleSort
def taller_2_punto_4():
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                temporal = lista[j]    
                lista[j] = lista[j+1]
                lista[j+1] = temporal
    print(lista)
taller_2_punto_4()

#SelectionSort

for i in range(len(lista)-1):
    menor = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    temporal = lista[menor]
    lista[menor] = lista[i]
    lista[i] = temporal
print(lista)

#InsertionSort

for i in range(1, len(lista)):
    actual = lista[i]
    indice = i
    while indice > 0 and lista[indice - 1] > actual:
        lista[indice] = lista[indice - 1]
        indice -= 1
    lista[indice] = actual
print(lista)

