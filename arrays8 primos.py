

cantidad = int(input("Ingrese la cantidad"))
Numeros = []
contador = 1

while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    condicion = 1
    divisores = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2:
        Numeros.append(num)
    contador += 1

Numeros = sorted(Numeros)
print("Los numeros primos son: ", Numeros)
