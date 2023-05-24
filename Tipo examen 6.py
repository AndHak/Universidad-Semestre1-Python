#Se tiene una cantidad de números dada. Determinar la veces que se repite el segundo primos que se enuentra.

cantidad = int(input("ingrese la cantidad"))
contador = 1
primos = 0
repeticiones = 0
segundo = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        primos += 1
        if primos == 2:
            segundo = num
        else:
            if num == segundo:
                repeticiones += 1
    contador += 1

print("el primo", segundo, "se repite", repeticiones, "veces más")
