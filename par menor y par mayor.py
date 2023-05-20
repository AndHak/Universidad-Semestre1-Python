cantidad = int(input("ingrese la cantidad de numeros que desea evaluar"))
contador = 1
contador_pares = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    if num % 2 == 0:
        if contador == 1:
            mayor = num
            menor = num
        if num > mayor:
            mayor = num
        else:
            if num < menor:
                menor = num
    contador = contador + 1

print("par mayor", mayor)
print("par menor", menor)
