#5.	Leer una serie de datos numéricos y llenarlos en un vector de tal forma que vayan quedando ordenados ascendentemente

def ordenar_numeros_ascendente():
    numeros = []
    while True:
        num = input('Presione "c" para terminar, ingrese un número: ')
        if num == "c":
            break
        else:
            numeros.append(int(num))
    
    print("Números ingresados:", numeros)
    
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    
    print("Números ordenados ascendentemente:", numeros)

ordenar_numeros_ascendente()



