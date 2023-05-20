print("encontrar el mayor y menor de los numeros primos ingresados por el usuario")
cantidad = int(input("cuantos numeros desea ingresar"))
contador = 1
contadorprimos = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores_exactos = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores_exactos = divisores_exactos + 1
        condicion = condicion + 1
    if divisores_exactos == 2:
        contadorprimos = contadorprimos + 1
        if contadorprimos == 1:
            mayor = num
            menor = num
        else:
            if num > mayor:
                mayor = num
            if num < menor:
                menor = num
    contador = contador + 1

print("el primo mayor es", mayor)
print("el primo menor es", menor)

