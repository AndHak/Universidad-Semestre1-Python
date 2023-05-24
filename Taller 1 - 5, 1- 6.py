#-	Determinar si un número es múltiplo de otro sin utilizar el operador residuo.

num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))
multiplo = False
suma = 0
while suma <= num2:
    suma += num1
    if suma == num2:
        multiplo = True
if multiplo:
    print(num1, "es multiplo de", num2)
else:
    print("no es multiplo")
