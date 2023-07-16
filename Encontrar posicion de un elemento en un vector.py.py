#Encontrar posicion de un elemento de un vector

def insertar_numero():
    lista = []
    while True:
        num = input('Ingrese un numero, presione "c" para finalizar: ')
        if num == "c":
            return lista
        else:
            lista.append(int(num))
        
lista = insertar_numero()

print(lista)
        
buscar_posicion = int(input("ingrese el numero para buscar su posicion"))

for i in range(len(lista)):
    if lista[i] == buscar_posicion:
        print("El elemento", buscar_posicion, "se encunetra en la posicion", i+1)