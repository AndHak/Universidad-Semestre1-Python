num = int(input("Ingrese un número: "))

contador = 0
condicion = 1

while condicion <= num:
    if num % condicion == 0:
        contador = contador + 1
    condicion = condicion + 1

print("El número", num, "tiene", contador, "divisores exactos.")