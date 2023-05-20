#Se tiene una cantidad dada de numeros, hallar el primo mayor y el primo menor y determinar la suma de los factoriales de los numeros pares entre estos dos numeros

cantidad = int(input("¿cuantos numeros va a ingresar?"))
print("A continuacion:")
contador = 1
contador_primos = 0

while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores = divisores + 1
        condicion = condicion + 1
    if divisores == 2:
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

#print(mayor, menor)
#funciona bien, ahora determinar la suma de los factoriales de los pares entre estos dos numeros

print("la suma de los factoriales de los pares entre",mayor,"y",menor, "es")
suma = 0
while menor <= mayor:
    if menor % 2 == 0:
        condicion_factorial = 1
        resultado_factorial = 1
        while condicion_factorial <= menor:
            resultado_factorial = resultado_factorial * condicion_factorial
            condicion_factorial = condicion_factorial + 1
        suma = suma + resultado_factorial
    menor = menor + 1
print(suma)