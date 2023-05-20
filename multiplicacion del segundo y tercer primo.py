#Se tiene una cantidad de numero, hallar la miltiplicacion con sumas del segundo y tercer primo en el orden de entrada

cantidad = int(input("¿Cuantos numeros va a ingresar?"))
print("Acontinuacion")

contador = 1
contador_primos = 0


while contador <= cantidad:
    num = int(input("ingrese un numero"))
    condicion = 1
    divisores_exactos = 0
    while condicion <= num:
        if num % condicion == 0:
            divisores_exactos = divisores_exactos + 1
        condicion = condicion + 1
    if divisores_exactos == 2:
        contador_primos = contador_primos + 1
        if contador_primos == 2:
            segundo = num
        if contador_primos == 3:
            tercero = num
    contador = contador + 1

print("segundo =", segundo, "tercero=", tercero)

#funciona correctamente, ahora la multiplicacion con sumas del segundo por el tercero

multiplicacion = 0

if tercero < segundo:
    condicion = 1
    while condicion <= segundo:
        multiplicacion = multiplicacion + tercero
        condicion = condicion + 1
    print("la multiplicacion de",segundo,"x",tercero,"=",multiplicacion)

if segundo < tercero:
    condicion = 1
    while condicion <= tercero:
        multiplicacion = multiplicacion + segundo
        condicion = condicion + 1
    print("la multiplicacion de",segundo,"x",tercero,"=",multiplicacion)