print("Inserte los siguiente datos para determinar cuales son pares")

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("ingrese el tercer numero"))
n4 = int(input("ingrese el cuarto numero"))

contador = 0

if n1 % 2 == 0:
    contador = contador + 1
if n2 % 2 == 0:
    contador = contador + 1   
if n3 % 2 == 0:
    contador = contador + 1   
if n4 % 2 == 0:
    contador = contador + 1  

print(contador,"es la cantidad de numeros pares que hay")  
