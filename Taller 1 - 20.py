#Se tiene una cantidad de números dada. Encontrar el promedio de los números pares que se encuentran entre el  primo mayor y el Fibonacci menor7
def taller_1_punto_19():
    cantidad = int(input("ingrese la cantidad de numeros"))
    contador = 1
    primos = 0
    fibonaccis = 0

    while contador <= cantidad:
        num = int(input("ingrese un numero"))
        divisores = 0
        condicion = 1
        while condicion <= num:
            if num % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            primos += 1
            if primos == 1:
                mayor = num
            else:
                if num>mayor:
                    mayor=num
        num1 = 0
        num2 = 1
        secuencia = 0
        while secuencia <= num:
            secuencia = num1 + num2
            num1 = num2
            num2 = secuencia
            if secuencia == num:
                fibonaccis += 1
                if fibonaccis == 1:
                    menor = num
                else:
                    if num<menor:
                        menor=num
        contador += 1
    print("primo mayor", mayor)
    print("fibnacci menor", menor)
    print("el promedio de los pares que estan entre", menor, "y", mayor, "es:")
    pares = 0
    suma = 0
    while menor < mayor:
        if menor % 2 == 0:
            pares += 1
            suma += menor
        menor += 1
    promedio = suma/pares
    print("=",promedio)
taller_1_punto_19()