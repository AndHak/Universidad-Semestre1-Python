print("Comparador de datos numericos")

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("ingrese el tercer numero"))
n4 = int(input("ingrese el cuarto numero"))

contador_pares = 0
contador_impares = 0

if n1 % 2 == 0:
    contador_pares = contador_pares + 1
else:
    contador_impares = contador_impares + 1
if n2 % 2 == 0:
    contador_pares = contador_pares + 1
else:
    contador_impares = contador_impares + 1
if n3 % 2 == 0:
    contador_pares = contador_pares + 1
else:
    contador_impares = contador_impares + 1    
if n4 % 2 == 0:
    contador_pares = contador_pares + 1
else:
    contador_impares = contador_impares + 1

if contador_impares > contador_pares:
    print("la cantidad de impares es", contador_impares, "por lo tanto es mayor que la cantidad de pares que es", contador_pares)
if contador_impares < contador_pares:
    print("la cantidad de impares es", contador_impares, "por lo tanto es menor que la cantidad de pares que es", contador_pares)
if contador_impares == contador_pares:
    print("la cantidad de impares es", contador_impares, "por lo tanto es igual que la cantidad de pares que es", contador_pares) 

