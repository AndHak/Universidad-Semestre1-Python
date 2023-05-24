#Se tiene una cantidad de números dada. Encontrar el promedio de los números que son Fibonacci y los primos

cantidad = int(input("cantidad de numeros"))
contador = 1
primos = 0
fibonaccis = 0
suma_primos = 0
suma_fibonaccis = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores  += 1
        condicion += 1
    if divisores == 2:
        primos += 1
        suma_primos += num
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == num:
            fibonaccis += 1
            suma_fibonaccis += num
    contador += 1
suma_total = 0
promedio_total = 0
contador_total = 0
contador_total = primos + fibonaccis
suma_total = suma_primos + suma_fibonaccis
promedio_total = suma_total / contador_total

print("promedio total de primos y fibonaccis de los numeros ingresados es", promedio_total)