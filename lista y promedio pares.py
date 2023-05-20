#Pedir al usuario que ingrese una lista de números y luego imprimir el promedio de los números pares en la lista.

cantidad = int(input("Cuantos nunmeros va a ingresar: "))

contador = 1
contadorpares = 0
sumador = 0

while contador <= cantidad:
    num = int(input("ingrese un numero"))
    if num % 2 == 0:
        sumador = sumador + num
        contadorpares = contadorpares + 1
    contador = contador + 1
    if contadorpares == 0:
        contadorpares = 1
promedio = sumador/contadorpares
print("el promedio de la suma de los numeros pares es", promedio)

 