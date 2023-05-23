#Escribe un programa que solicite al usuario ingresar un número entero positivo. A continuación,
#calcula la suma de todos los números pares que sean múltiplos de 5 y estén en el rango desde 1 hasta el número ingresado por el usuario.
#A continuación, encuentra el número factorial del último número par que se sumó. 
#El número factorial se calcula multiplicando todos los números desde 1 hasta el número dado.
#Finalmente, muestra la suma obtenida y el número factorial calculado.

num = int(input("ingrese un entero positivo"))
condicion = 1
suma = 0
ultimo = 0
while condicion <= num:
    if condicion % 2 == 0:
        if condicion % 5 == 0:
            suma += condicion
            ultimo = condicion
    condicion += 1

print("la suma de los pares multiplos de 5 es:",suma, "y el ultimo numero sumado es:", ultimo)
condicion = 1
resultado = 1
while condicion <= ultimo:
    resultado *= condicion
    condicion += 1
print("el factorial de", ultimo, "es", resultado)