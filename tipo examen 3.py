#Se tiene una cantidad dada de numeros, determinar si el segundo primo y el cuarto primo son consecutivos

cantidad = int(input("Cantidad de numeros"))
contador = 1
contador_primos = 0
segundo = 0
cuarto = 0
consecutivo = True

while contador <= cantidad:
    num = int(input("Ingrese un numero: "))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        contador_primos += 1
        if contador_primos == 2:
            segundo = num
        elif contador_primos == 4:
            cuarto = num
    contador += 1

print("Segundo primo:", segundo)
print("Cuarto primo:", cuarto)

if segundo < cuarto:
    contador = segundo + 1
    while contador < cuarto:
        condicion = 1
        divisores = 0
        while condicion <= contador:
            if contador % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            consecutivo = False
            break
        contador += 1
if consecutivo:
    print("el primo", cuarto, "es consecutivo del primo", segundo)
else:
    print("No son consecutivos")
