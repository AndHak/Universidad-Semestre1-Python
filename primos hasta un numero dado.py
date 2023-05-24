num = int(input("ingrese un numero"))
condicion = 1
contador = 1
divisores = 0
primos = 0

while contador <= num:
    condicion = 1
    divisores = 0
    while condicion <= contador:
        if contador % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        print(contador)
    contador += 1
    

    