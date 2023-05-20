#se tiene una cantidad dada de numeros, determinar el contador de pares por el contador de impares con sumas

num = int(input("ingrese el numero numero"))
contador_pares = 1
contador_impares = 1
suma = 0

while suma <= num:
    suma = suma + 1
    contador_impares = contador_impares + 1
    contador_pares = contador_pares + 1
    