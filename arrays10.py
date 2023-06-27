#Numeros que se repiten
cantidad = int(input("Cuantos numeros va a ingresar"))
numeros = []
repetidos = []
archivo = []
contador = 1
while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    numeros.append(num)
    contador += 1
    
for n in numeros:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)

print("Los numeros que se repiten son: ",repetidos)
