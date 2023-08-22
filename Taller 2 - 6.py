#6.	Leer una serie de datos numéricos y llenarlos en un vector los datos que sean primos y Fibonacci que vayan quedando ordenados descendentemente.
def taller_2_punto_6():
    def numeros():
        numeros = []
        while True:
            num = input('Precione "c" para terminar, Ingrese un numero')
            if num == "c":
                return numeros
            try:
                numeros.append(int(num))
            except ValueError:
                print('Ingrese un valor valido')
    numeros = numeros()

    def primos_y_fibonaccis():
        primos_y_fibonaccis = []
        for i in numeros:
            es_primo = False
            condicion = 1
            divisores = 0
            while condicion <= i:
                if i % condicion == 0:
                    divisores += 1
                condicion += 1
            if divisores == 2:
                es_primo = True
            es_fibonacci = False
            num1 = 0
            num2 = 1
            secuencia = 0
            while secuencia <= i:
                secuencia = num1 + num2
                num1 = num2
                num2 = secuencia
                if secuencia == i:
                    es_fibonacci = True
            if es_fibonacci or es_primo:
                primos_y_fibonaccis.append(i)
        return primos_y_fibonaccis
        
    primos_y_fibonaccis = primos_y_fibonaccis()

    def particionado(primos_y_fibonaccis):
        pivote = primos_y_fibonaccis[0]
        menores = []
        mayores = []
        for i in range(1, len(primos_y_fibonaccis)):
            if primos_y_fibonaccis[i] < pivote:
                menores.append(primos_y_fibonaccis[i])
            else:
                mayores.append(primos_y_fibonaccis[i])
        return menores, pivote, mayores

    def quicksort(primos_y_fibonaccis):
        if len(primos_y_fibonaccis) < 2:
            return primos_y_fibonaccis
        menores, pivote, mayores = particionado(primos_y_fibonaccis)
        return quicksort(mayores) + [pivote] + quicksort(menores)

    resultado = quicksort(primos_y_fibonaccis)
    print(resultado)
taller_2_punto_6()

 