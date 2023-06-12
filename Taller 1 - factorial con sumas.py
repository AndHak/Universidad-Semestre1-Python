#Hallar el factorial de un número con sumas

num = int(input("Ingrese un número: "))
factorial = 1
contador = 1
suma = 0

while contador <= num:
    temp = factorial
    suma = 0
    while temp > 0:
        suma += contador
        temp -= 1
    factorial = suma
    contador += 1

print("El factorial de", num, "es:", factorial)