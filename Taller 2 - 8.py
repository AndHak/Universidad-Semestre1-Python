#8.	Se tiene un vector con datos numéricos, ordenar la mitad del vector en orden ascendente y la otra mitad en orden descendente.

numeros = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]

def orden_ascendente_descendente(lista):
    mitad = len(lista) // 2

    # Ordenar la primera mitad en forma ascendente usando el algoritmo de burbuja
    for i in range(mitad):
        for j in range(mitad - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Ordenar la segunda mitad en forma descendente usando el algoritmo de burbuja
    for i in range(mitad, len(lista)):
        for j in range(mitad, len(lista) - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

resultado = orden_ascendente_descendente(numeros)
print(resultado)  # Resultado: [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
