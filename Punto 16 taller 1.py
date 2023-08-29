# Se tiene una cantidad de números dada donde hay varios primos determinar 
# si el primo 2 y el primo 3 de acuerdo al orden de entrada si son consecutivos.
# Son consecutivos si entre los dos no hay otro número primo
cantidad=int(input("Digite la cantidad de datos, debe contener al menos 3 primos"))
primo2=primo3=0
cantidad_primos=0
consecutivo=True
contador=1
while contador<=cantidad:
    num=int(input(f"digite el dato{contador}->"))
    divisores=0
    z=1
    while z<num:
        if num%z==0:
            divisores+=1
        z+=1
    if divisores==2:
        cantidad_primos+=1
        if cantidad_primos==2:
            primo2=num
        elif cantidad_primos==3:
            primo3=num
    contador+=1
print("segundo primo", primo2)
print("tercer primo", primo3)