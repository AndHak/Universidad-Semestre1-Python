cantidad_numeros = int(input("Ingrese la cantidad de números: "))
condicion = 1
divisores_exactos = 0
sumador = 0
divisor_sumador = 0
contador = 1

while contador<=cantidad_numeros:
    num = int(input("Ingrese un numero"))
    while condicion <= num:
        if num % condicion == 0:
            divisores_exactos = divisores_exactos + 1
        condicion = condicion + 1
    if divisores_exactos == 2:
        sumador = sumador + num
        divisor_sumador = divisor_sumador + 1
    
    divisores_exactos = 0
    condicion = 1
    dividendo = 1
    contador = contador + 1

    if divisor_sumador == 0:
        divisor_sumador = 1

promedio = sumador/divisor_sumador
print("el promedio de los primos es",   promedio)







