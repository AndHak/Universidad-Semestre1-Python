print("encontrar el mayor y menor de los numeros primos ingresados por el usuario")
cantidad = int(input("cantidad a calcular"))
contador = 1
contador_primos = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    divisores = 0
    condicion = 1
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
            if num > mayor:
                mayor = num
            if num < menor:
                menor = num

    contador = contador + 1

print(mayor, menor)

resultado = mayor - menor

condicion = 1
divisores = 0

while condicion <= resultado:
    if resultado % condicion == 0:
        divisores = divisores + 1
    condicion = condicion + 1

if divisores <=2:
    print("la resta de", mayor, "-", menor, "=", resultado, "que es un numero primo")
else:
    print("la resta de", mayor, "-", menor, "=", resultado, "No es un numero primo")
    

