#Programa que calcula un cateto o hipotenusa:

try:
    print('Calcular')
    print('1. Hipotenusa')
    print('2. Cateto')
    eleccion = int(input('Escoja 1 o 2 segun lo que desee calcular'))
    if eleccion == 1:
        cateto1 = int(input('Cuanto mide el primer cateto'))
        cateto2 = int(input('Cuanto mide el segundo cateto'))
        hipotenusa = 0
        hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)
        print('El valor de la hipotenusa es', hipotenusa)
    if eleccion == 2:
        hipotenusa = int(input('cuanto mide la hipotenusa'))
        cateto1 = int(input('Cuanto mide un cateto'))
        cateto2 = 0
        cateto2 = ((hipotenusa ** 2) - (cateto1 ** 2)) ** (1/2)
        print('El valor del otro cateto es: ', cateto2)
except ValueError:
    print('Ingrese un valor valido')