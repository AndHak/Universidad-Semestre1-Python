cantidad = int(input("Ingrese la cantidad: "))
numeros = []
repeticiones = {}
max_repeticiones = 0
moda = []

contador = 1
while contador <= cantidad:
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    contador += 1

for n in numeros:
    if n in repeticiones:
        repeticiones[n] += 1
    else:
        repeticiones[n] = 1

for n, cantidad in repeticiones.items():
    if cantidad > max_repeticiones:
        max_repeticiones = cantidad

for n, cantidad in repeticiones.items():
    if cantidad == max_repeticiones:
        moda.append(n)

print("La moda es:", moda, "y se repite", max_repeticiones, "veces.")
