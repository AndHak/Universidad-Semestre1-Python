#Usar continue para no agregar los impares a un vector

def numeros_no_impares():
    numeros_no_impares = []
    while True:
        num = input('precione "c" para terminar, Agregue un número:  ')
        if num == "c":
            return numeros_no_impares
        else:
            if int(num) % 2 == 1:
                continue
            else:
                numeros_no_impares.append(int(num))

numeros_no_impares = numeros_no_impares()

print(numeros_no_impares)
