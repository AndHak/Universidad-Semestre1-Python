#-	Realizar un programa que calcule el área de un triángulo, un rectángulo y un cuadrado, y muestre el área mayor y el área menor.

lado_cuadrado = int(input("¿Cuánto mide el lado del cuadrado? "))
lado_rectangulo1 = int(input("¿Cuánto mide uno de los lados del rectángulo? "))
lado_rectangulo2 = int(input("¿Cuánto mide el otro lado del rectángulo? "))
base = int(input("¿Cuánto mide la base del triángulo? "))
altura = int(input("¿Cuánto mide la altura del triángulo? "))

area_cuadrado = lado_cuadrado * lado_cuadrado
print("Área del cuadrado:", area_cuadrado)

area_rectangulo = lado_rectangulo1 * lado_rectangulo2
print("Área del rectángulo:", area_rectangulo)

area_triangulo = (base * altura) / 2
print("Área del triángulo:", area_triangulo)

area_mayor = area_cuadrado
area_menor = area_cuadrado

if area_mayor < area_rectangulo:
    area_mayor = area_rectangulo
if area_mayor < area_triangulo:
    area_mayor = area_rectangulo
if area_menor > area_rectangulo:
    area_menor = area_rectangulo
if area_menor > area_triangulo:
    area_menor = area_triangulo

print("El área mayor es:", area_mayor)
print("El área menor es:", area_menor)
