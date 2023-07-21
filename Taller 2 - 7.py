#7.	Se tiene un vector con datos numéricos, ordenar las posiciones pares en orden ascendente y las impares en orden descendente.
def ordenar_posiciones_pares_impares(vector):
    # Función de ordenamiento de burbuja para las posiciones pares
    def bubble_sort_pares(lista):
        for i in range(len(lista)- 1):
            for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    # Función de ordenamiento de burbuja para las posiciones impares
    def bubble_sort_impares(lista):
       for i in range(len(lista)- 1):
            for j in range(len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    # Obtener los valores en posiciones pares e impares
    pares = [vector[i] for i in range(len(vector)) if i % 2 == 0]
    impares = [vector[i] for i in range(len(vector)) if i % 2 != 0]
    # Ordenar los valores en posiciones pares e impares
    bubble_sort_pares(pares)
    bubble_sort_impares(impares)
    # Construir el vector resultante manteniendo las posiciones pares e impares
    vector_resultante = []
    pares_index = 0
    impares_index = 0
    for i in range(len(vector)):
        if i % 2 == 0:
            vector_resultante.append(pares[pares_index])
            pares_index += 1
        else:
            vector_resultante.append(impares[impares_index])
            impares_index += 1
    return vector_resultante
#Prueba para probar si la funcion sirve
numeros = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
vector_resultante = ordenar_posiciones_pares_impares(numeros)
print(vector_resultante)  #[1, 10, 3, 8, 5, 6, 7, 4, 9, 2] Tiene que dar
