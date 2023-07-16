#5.	Leer una serie de datos numéricos y llenarlos en un vector de tal forma que vayan quedando ordenados ascendentemente

def numeros():
    numeros = []
    while True:
        num = input('presione "c" para terminar, Ingrese un numero:  ')
        if num == "c":
            return numeros
        else:
            numeros.append(int(num))
numeros = numeros()
print(numeros)

numeros_ordenados = []

while len(numeros) > 0:
    min_num = numeros[0]
    min_index = 0
    for i in range(1, len(numeros)):
        if numeros[i] < min_num:
            min_num = numeros[i]
            min_index = i
    numeros_ordenados.append(min_num)
    del numeros[min_index]
    
print(numeros_ordenados)

