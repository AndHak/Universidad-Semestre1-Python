#Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos,
#determinar cuántos triángulos equiláteros, escalenos e isósceles se encuentran en estos triángulo
#y la suma de los triángulos isósceles Sin utilizar condiciones compuestas.

#equilatero todos lados iguales
#isosceles dos lados iguales
#escaleno todos lados diferentes

cantidad = int(input("ingrese la cantidad de triangulo"))
contador = 1
equilateros = 0
isosceles = 0
escalenos = 0
suma_isosceles = 0
while contador <= cantidad:
    print("")
    lado1 = int(input("ingrese el 1 lado del triangulo"))
    lado2 = int(input("ingrese el 2 lado del triangulo"))
    lado3 = int(input("ingrese el 3 lado del triangulo"))
    
    if lado1 == lado2 == lado3:
        equilateros += 1
    elif lado1 != lado2 != lado3 != lado1:
        escalenos += 1
    else:
        isosceles += 1
        suma_isosceles += lado1 + lado2 + lado3
    contador += 1

print("")
print("Cantidad de triángulos equiláteros:", equilateros)
print("Cantidad de triángulos escalenos:", escalenos)
print("Cantidad de triángulos isósceles:", isosceles)
print("Suma de los perímetros de los triángulos isósceles:", suma_isosceles)
