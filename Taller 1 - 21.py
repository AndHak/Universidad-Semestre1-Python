#Hallar la potencia de dos números con sumas
num1 = int(input("Ingrese un número: "))
num2 = int(input("Elevado a la potencia: "))

potencia = 1
contador = 1

while contador <= num2:
    suma = 0
    condicion = 1
    while condicion <= num1:
        suma += potencia
        condicion += 1
    potencia = suma
    contador += 1

print("El resultado de", num1, "elevado a la potencia", num2, "es:", potencia)
