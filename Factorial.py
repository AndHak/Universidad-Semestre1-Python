num = int(input("ingrese un numero para calcular su factorial"))
contador = 1
resultado = 1
while contador <= num:
    resultado = resultado * contador
    contador = contador + 1
print(resultado)