#Se tiene una cantidad de datos, deterinar el primo mayor y el primo menor y sacar los pares que hay entre estos dos numeros

cantidad = int(input("ingrese la cantidad de datos que va a ingresar"))
contador = 1
contador_primos = 0
while contador <= cantidad:
    num = int(input("ingrese el numero"))
    divisores = 0
    condicion = 1
    while condicion <= num:
        if num % condicion == 0:
            divisores = divisores + 1
        condicion = condicion + 1
    if divisores == 2:
        contador_primos = contador_primos + 1
        if contador_primos == 1:
            mayor = num
            menor = num
        else:
            if num>mayor:
                mayor=num
            if num<menor:
                menor=num
    contador = contador + 1

#print(mayor, menor)

#funciona bien ahora a sacar los pares entre estos dos numeros

print("lista de los numeros pares que hay entre", mayor, "y", menor)

while menor<=mayor:
    if menor % 2 == 0:
        print(menor)
    menor = menor + 1
