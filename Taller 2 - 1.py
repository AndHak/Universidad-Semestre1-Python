#1.	Se tiene un vector con datos numéricos repetidos, determinar cuál es el primo que más se repite.

cantidad = int(input("Cantidad de numeros"))
numeros = []
archivo = []
repetidos = []
primos_repetidos = []
contador = 1

while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    numeros.append(num)
    contador += 1

for n in numeros:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)
    

for n in repetidos:
    condicion = 1
    divisores = 0
    while condicion <= n:
        if n % condicion == 0:
            divisores += 1
        condicion += 1
    if divisores == 2: 
        primos_repetidos.append(n)

if len(primos_repetidos) > 0:
    print("Los primos que se repiten son: ", primos_repetidos)
else:
    print("No hay primos repetidos")