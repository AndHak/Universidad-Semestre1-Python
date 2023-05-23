#Se tiene una cantidad dada de numeros, hallar el primo mayor y el primo menor y determinar la suma de los factoriales de los numeros pares entre estos dos numeros
cantidad = int(input("cantidad de numeros"))
contador = 1
contador_primos = 0
while contador<=cantidad:
    num = int(input("ingrese un numero"))
    divisores_exactos = 0
    condcion = 1
    while condcion <= num:
        if num % condcion == 0:
            divisores_exactos = divisores_exactos + 1
        condcion = condcion + 1
    if divisores_exactos == 2:
        contador_primos = contador_primos + 1
        if contador_primos == 1:
            mayor = num
            menor = num
        else:
            if num>mayor:
                mayor=num
            if num<menor:
                menor=num
    contador = contador + 1
suma = 0
print("la suma de los factoriales pares entre", menor, "y", mayor)
while menor <= mayor:
    if menor % 2 == 0:
        condcion_factorial = 1
        resultado_factorial = 1
        while condcion_factorial <= menor:
            resultado_factorial = resultado_factorial * condcion_factorial
            condcion_factorial = condcion_factorial + 1
        suma = suma + resultado_factorial
    menor = menor + 1
print(suma)




            
