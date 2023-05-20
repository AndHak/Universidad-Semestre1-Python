print("secuencia de fibonacci")
cantidad = int(input("cunatos numeros de fibonasci desea encontrar"))
numero1 = 0
numero2 = 1
contador = 1

print(numero1)
print(numero2)

while contador < cantidad:
    secuencia = numero1 + numero2
    print(secuencia)
    numero1 = numero2
    numero2 = secuencia
    contador = contador + 1        