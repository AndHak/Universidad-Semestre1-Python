#3.	Se tiene un vector con datos numéricos eliminar los datos que sean primos y Fibonacci.

cantidad = int(input("Cantidad de numeros"))
contador = 1
vector_final = []
primos = []
fibonaccis = []
numeros = []

while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    numeros.append(num)
    contador += 1

for n in numeros:
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= n:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == n:
            fibonaccis.append(n)
    condicion = 1
    divisores = 0
    while condicion <= n:
        if n % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos.append(n)

vector_final = [n for n in numeros if n not in primos and n not in fibonaccis]

print("Los números que no son primos ni Fibonacci son:", vector_final)