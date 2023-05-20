#se tiene una cantidad de numeros, determinar la cantidad de primos y multiplos de 3 y hallar las tablas de multiplicar de los pares que estan entre estos dos caracteres

cantidad_numeros = int(input("cuantos numeros desea ingresas: "))

condicion = 1
contador =  1
contador_primos = 0
contador3 = 0
divisores_exactos = 0
divisor = 1

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