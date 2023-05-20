print("Calcular el promedio de los numeros impares")

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("ingrese el tercer numero"))
n4 = int(input("ingrese el cuarto numero"))

contador = 0
contador2 = 0

if n1 % 2 == 1:
    contador = contador + n1
    contador2 = contador2 + 1
if n2 % 2 == 1:
    contador = contador + n2
    contador2 = contador2 + 1  
if n3 % 2 == 1:
    contador = contador + n3
    contador2 = contador2 + 1   
if n4 % 2 == 1:
    contador = contador + n4
    contador2 = contador2 + 1  

if contador2 == 0:
    print("no hay numeros impares, por lo tanto no se puede hacer promedio")
    contador2 = 1

promedio = (contador/contador2)

print(promedio,"es el promedio de los numeros impares")  