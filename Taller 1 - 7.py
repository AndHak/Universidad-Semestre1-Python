#7.	Determinar si un número es primo sin utilizar el operador residuo.

num1 = int(input("ingrese un numero"))
primos = 0
condicion = 1
divisores = 0
while condicion <= num1:
    suma = 0
    while suma <= num1:
        suma += condicion
        if suma == num1:
            divisores += 1
    condicion += 1
if divisores == 2:
    print(num1,"es primo")
else:
    print(num1,"no es primo")
        
        
    