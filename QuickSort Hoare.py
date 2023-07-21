def numeros():
    numeros = []
    while True:
        num = input('Presione "c" para terminar, Ingrese un numero:  ')
        if num == "c":
            return numeros
        try:
            numeros.append(int(num))
        except ValueError:
            print('Ingrese un valor valido')
numeros = numeros()

