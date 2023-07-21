def numeros():
    numeros = []
    while True:
        num = input('presione "c" para terminar, Ingrese un numero: ')
        if num == "c":
            return numeros
        try:
            numeros.append(int(num))
        except ValueError:
            print("Ingrese un valor valido")

def particionado(numeros):
    comparador = numeros[0]
    menores = []
    mayores = []
    for i in range(1, len(numeros)):
        if numeros[i] < comparador:
            menores.append(numeros[i])
        else:
            mayores.append(numeros[i])
    return menores, comparador, mayores

def quicksort(numeros):
    if len(numeros) < 2:
        return numeros
    menores, comparador, mayores = particionado(numeros)
    return quicksort(menores) + [comparador] + quicksort(mayores)

numeros_ingresados = numeros()
resultado = quicksort(numeros_ingresados)
print(resultado)
