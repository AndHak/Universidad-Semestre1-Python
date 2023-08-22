numero1 = None
numero2 = None
numero3 = None

def juego():
    global numero1, numero2, numero3
    while numero1 is None or numero2 is None or numero3 is  None:
        print("1. jugador1")
        print("2. jugador2")
        print("3. jugador3")
        respuesta = int(input("Escoja un jugador: "))
        if respuesta == 1:
            if numero1 is not None:
                print("Este jugador ya ha elegido")
            else: 
                numero1 = int(input("Ingrese un numero: "))
        if respuesta == 2:
            if numero2 is not None:
                print("Este jugador ya ha elegido")
            else: 
                numero2 = int(input("Ingrese un numero: "))
        if respuesta == 3:
            if numero3 is not None:
                print("Este jugador ya ha elegido")
            else: 
                numero3 = int(input("Ingrese un numero: "))

juego()
print("El jugador 1 ha elegido:", numero1)
print("El jugador 2 ha elegido:", numero2)
print("El jugador 3 ha elegido:", numero3)
