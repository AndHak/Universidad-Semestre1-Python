print("\n\n¿Cuanto sabes de animales?\n\n")
animales = ["gato", "perro", "loro", "ornitorrinco", "ballena", "jirafa", "cebra", "guepardo", "morsa", "narval"]
puntos = 0
jugando = True

while jugando:
    if puntos == 0:
        pregunta = input("Le gusta la leche, es un animal domestico y muy comun, son habiles trepando")
        if pregunta in animales[0]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[0])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 1:
        pregunta = input("Es el mejor amigo del hombre")
        if pregunta in animales[1]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[1])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 2:
        pregunta = input("Puede hablar pero no sabe lo que dice")
        if pregunta in animales[2]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[2])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 3:
        pregunta = input("Lo conocen como Perry y es un agente secreto, que animal es?")
        if pregunta in animales[3]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[3])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 4:
        pregunta = input("Soy el animal mas grande del mundo")
        if pregunta in animales[4]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[4])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 5:
        pregunta = input("Tengo un cuello muy largo y vivo en sabana")
        if pregunta in animales[5]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[5])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 6:
        pregunta = input("Cuando naci, me imprimieron a blanco y negro")
        if pregunta in animales[6]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[6])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 7:
        pregunta = input("Soy el animal más rapido del mundo")
        if pregunta in animales[7]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nSiguiente pregunta, Pregunta dificil\n")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[7])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 8:
        pregunta = input("Soy algo torpe y vivo en el hielo, tengo dos grandes colmillos")
        if pregunta in animales[8]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nFelicidades has llegado a la ultima pregunta\n")
            print("RESPONDE LA SIGUIENTE PREGUNTA PARA SER UN VERDADERO GENIO DE LOS ANIMALES")
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[8])
            print("Has conseguido", puntos, "puntos")
            jugando = False
    if puntos == 9:
        pregunta = input("Soy un cetáceo, mi piel es moteada y vivo en el ártico")
        if pregunta in animales[9]:
            puntos += 1
            print("Felicidades, has ganado", puntos, "puntos")
            print("\nFELICIDADES GANASTE EL JUEGO, ERES REALMENTE UN GENIO\n")
            jugando = False
        else:
            print("Has perdido, la respuesta correcta era:  ", animales[9])
            print("Has conseguido", puntos, "puntos")
            jugando = False