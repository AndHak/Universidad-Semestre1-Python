#programa que calcule la hipotenusa

try:
    cateto1 = int(input('Ingrese el valor del primero cateto:  '))
    cateto2 = int(input('Ingrese el valor del segundo cateto:  '))
    hipotenusa = 0

    hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)

except ValueError:
    print("Ingrese un valor valido")


print('El valor de la hipotenusa es: ', hipotenusa)