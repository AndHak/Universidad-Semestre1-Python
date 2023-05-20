#se tiene una cantidad de numeros, determinar la cantidad de primos y multiplos de 3 y hallar las tablas de multiplicar de los pares entre estos dos caracteres

cantidad_numeros = int(input("cuantos numeros desea ingresas: "))

condicion = 1
contador =  1
contador_primos = 0
contador3 = 0
divisores_exactos = 0
divisor = 1
pares = 0

while contador <= cantidad_numeros:
    num = int(input("ingrese el numero"))
    
    divisores_exactos = 0
    divisor = 1
    
    while divisor <= num:
        if num % divisor == 0:
            divisores_exactos = divisores_exactos + 1
        divisor = divisor + 1

    if divisores_exactos <= 2:
            contador_primos = contador_primos + 1

    if num % 3 == 0:
        contador3 = contador3 + 1

    contador = contador + 1

print(contador3, contador_primos)

if contador3 < contador_primos:
    while contador3 <= contador_primos:
        condicion = 1
        while condicion <= 10:
            resultado = contador3 * condicion
            if contador3 % 2 == 0:
                print(contador3,"x",condicion,"=",resultado)
            condicion = condicion + 1
        contador3 = contador3 + 1
else:
    if contador_primos < contador3:
        while contador_primos <= contador3:
            condicion = 1
            while condicion <= 10:
                resultado = contador_primos * condicion
                if contador_primos % 2 == 0:
                    print(contador_primos,"x",condicion,"=",resultado)
                condicion = condicion + 1
            contador_primos = contador_primos + 1