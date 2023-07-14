print("ADIVINA LOS 5 COLORES DE LA LISTA")
Jugando = True
colores = ["amarillo", "azul", "rojo", "blanco", "negro"]
puntos = 0
while Jugando:
    color = str(input("Escribe un color:  "))
    color = color.lower()
    if color in colores:
        puntos += 1
        print("El color", color, "Esta en la lista")
        print("tienes", puntos, "puntos")
        if puntos == 5:
            print("Has ganado el juego, adivinaste todos los colores, tienes", puntos, "puntos")
            Jugando = False
    else:
        print("Ese color no esta en la lista has perdido")
        print("Has conseguido", puntos, "puntos")
        Jugando = False
    