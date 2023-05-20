num = int(input("Ingrese un número: "))
suma = 0
contador = 1
while contador <= num:
    if contador % 2 == 0:
        suma = suma + contador
    contador = contador + 1
print("La suma de los números pares es:", suma)


