print("encontrar el numero mayor")
cantidad_numeros = int(input("cuantos numeros desea ingresar"))
contador = 1
while contador <= cantidad_numeros:
    num = int(input("ingrese un numero"))
    if contador == 1:
        menor = num
        mayor = num
    else:
        if num>mayor:
            mayor=num
        if num<menor:
            menor=num
    
    contador += 1


print("numero mayor", mayor)
print("numero menor", menor)

    
    
        
