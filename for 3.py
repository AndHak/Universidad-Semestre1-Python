#suma de numeros tanas veces como dice el usuario pero si se pasa de 100 para

cantidad = int(input("Cuantos numeros va a sumar? "))
suma = 0

for i in range(cantidad):
    if suma <= 100:
        num = int(input("Ingrese un numero:  "))
        suma += num
        i+= 1
    else:
        i = cantidad

print(suma)
