n = int(input("Ingrese un número: "))

c = 1
suma5 = 0
contador5 = 0
suma3 = 0
contador3 = 0

while c <= n:
    if c % 5 == 0:
        suma5 = suma5 + c
        contador5 = contador5 + 1
    if c % 3 == 0:
        suma3 = suma3 + c
        contador3 = contador3 + 1
    c = c + 1

promedio5 = suma5 / contador5
promedio3 = suma3 / contador3

if promedio5 > promedio3:
    print("El promedio de los múltiplos de 5 es mayor que el promedio de los múltiplos de 3.")
if promedio5 < promedio3:
    print("El promedio de los múltiplos de 5 es menor que el promedio de los múltiplos de 3.")
if promedio5 == promedio3:
    print("El promedio de los múltiplos de 5 es igual al promedio de los múltiplos de 3.")
