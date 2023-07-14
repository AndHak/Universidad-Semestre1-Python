#pedir numeros tantas veces como diga el usuario con for y sumarlos

num = int(input("Cuantos numeros va a sumar:  "))
suma = 0

for i in range(num):
    num = float(input("Ingrese un numero: "))
    suma += num

print(suma)