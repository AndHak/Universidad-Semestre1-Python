#Agregar a diferentes vectores los pares, impares, primos y fibonaccis

pares = []
impares = []
primos = []
fibonaccis = []
contador = 0
menor = 0
mayor = 0

def super_funcion():
    super_funcion = []
    global contador, mayor, menor
    while True:
        try:
            num = input('Precione "c" para cancelar,  Ingrese un numero:  ')
            if num == "c":
                return super_funcion
            else:
                num = int(num)
                if num % 2 == 0:
                    pares.append(num)
                if num % 2 == 1:
                    impares.append(num)
                num1, num2 = 0, 1
                secuencia = 0
                while secuencia <= num:
                    secuencia = num1 + num2
                    num1 = num2
                    num2 = secuencia
                    if secuencia == num:
                        fibonaccis.append(num)
                condicion = 1
                divisores = 0
                while condicion <= num:
                    if num % condicion == 0:
                        divisores += 1
                    condicion += 1
                if divisores == 2:
                    primos.append(num)
                contador += 1
                if contador == 1:
                    mayor = num
                    menor = num
                else:
                    if num < menor:
                        menor = num
                    if num > mayor:
                        mayor = num
        except ValueError:
            print("Caracter no valido, pruebe con otro valor")
            
super_funcion()

print("\nNumeros primos:  ", primos)
print("\nNumeros fibonaccis:  ", fibonaccis)
print("\nNumeros pares:  ", pares)
print("\nNumeros impares:  ", impares)
print("\nEl numero mayor es", mayor, "Y el numero menor es", menor)