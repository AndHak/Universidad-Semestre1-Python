#Pedir al usuario que ingrese un número y luego imprimir si es divisible por 3 y no es divisible por 5.

num = int(input("numero"))

if num % 3 == 0 and num % 5 != 0:
    print("el", num, "es multiplo de 3 y no de 5")
else:
    print("el", num, "no es multiplo de 3 y no de 5")