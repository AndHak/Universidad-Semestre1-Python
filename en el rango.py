#Agregar numeros mientras sean menores que 45 y mayores que 18

numeros = []
contador = 1
n = int(input("Di un numero entre 18 y 45:  "))

while n in range(18,45):
    print("Esta en el rango")
    n = int(input("Di un numero entre 18 y 45:  "))
else:
    print("Fuera del rango")
