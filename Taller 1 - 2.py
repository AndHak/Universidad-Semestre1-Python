# -	Realizar un programa que calcule el área de un triángulo, un rectángulo y un cuadrado, y muestre las áreas en orden ascendente

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

if area_triangulo < area_cuadrado:
    if area_cuadrado < area_rectangulo:
        print(area_triangulo, area_cuadrado, area_rectangulo)
    else:
        if area_rectangulo < area_triangulo:
            print(area_rectangulo, area_triangulo, area_cuadrado)
        else:
            print(area_triangulo, area_rectangulo, area_cuadrado)
else:
    if area_cuadrado < area_triangulo:
        if area_triangulo < area_rectangulo:
            print(area_cuadrado, area_triangulo, area_rectangulo)
        else:
            if area_rectangulo < area_cuadrado:
                print(area_rectangulo, area_cuadrado, area_triangulo)
            else:
                print(area_cuadrado, area_rectangulo, area_triangulo)