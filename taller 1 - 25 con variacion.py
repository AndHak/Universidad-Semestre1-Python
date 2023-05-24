#Se tiene una cantidad de números dada. Encontrar el promedio de los números que son Fibonacci y primos a la vez

cantidad = int(input("cantidad de numeros"))
contador = 1
fibonaccis_y_primos = 0
suma_ambos = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores  += 1
        condicion += 1
    if divisores == 2:
        num1 = 0
        num2 = 1
        secuencia = 0
        while secuencia <= num:
            secuencia = num1 + num2
            num1 = num2
            num2 = secuencia
            if secuencia == num:
                suma_ambos += num
                fibonaccis_y_primos += 1
    contador += 1

promedio_total = suma_ambos/fibonaccis_y_primos


print("promedio total de primos y fibonaccis de los numeros ingresados es", promedio_total)