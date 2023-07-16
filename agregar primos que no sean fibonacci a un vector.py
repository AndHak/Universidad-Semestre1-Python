#Se tiene varios numeros, agregar a un vector los primos que no sean fibonacci

def numeros():
    numeros = []
    while True: 
        num = input('Presione "c" para terminar. Ingrese un número: ')
        if num == "c":
            return numeros
        else:
            numeros.append(int(num))

numeros = numeros()
print(numeros)

primos = []
for n in numeros:
    condicion = 1
    divisores = 0
    while condicion <= n:
        if n % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos.append(n)

fibonaccis = []
for n in primos:
    num1, num2 = 0, 1
    secuencia = 0
    while secuencia <= n:
        secuencia = num1 + num2
        num1, num2 = num2, secuencia
        if secuencia == n:
            fibonaccis.append(n)

primos_no_fibonaccis = [n for n in primos if n not in fibonaccis]

print(primos_no_fibonaccis)
