#suma hasta un numero dado con for

num = int(input("Ingrese el numero: "))
suma = 0

for i in range(num+1):
    suma += i
    i += 1

print(suma)


