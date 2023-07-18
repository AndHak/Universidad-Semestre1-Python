#Juego de adivinar el orden de los colores

import time
import random
import os

colores = ["amarillo", "azul", "rojo", "verde", "blanco", "negro", "morado", "rosado", "gris", "cian", "cafe", "naranja"]
lista = []
dificultad = 3
nivel = 1

print("RECUERDA LOS COLORES")
print("""Descripcion:  Recuerda los colores, con tiempo de 5 segundo, la
      dificultad ira aumntando a medida que avances el juego""")
def juego():
    global dificultad, nivel
    jugando = True
    while jugando:
        print("Nivel", nivel)
        colores_a_recordar = random.sample(colores, dificultad)
        print(colores_a_recordar)
        time.sleep(5)
        os.system("clear")
        contador = 1
        lista.clear()
        while contador <= dificultad:
            pregunta = input("Ingrese un color: ")
            lista.append(pregunta.lower())
            contador += 1
        if lista == colores_a_recordar:
            dificultad += 1
            nivel += 1
            print("Muy bien, haz subido al nivel")
            if dificultad == 12:
                print("Llegaste al nivel maximo")
                print("FELICIDADES")
                jugando = False
        else:
            print("los colores correctos eran: ", colores_a_recordar)
            print("Llegaste hasta el nivel", nivel)
            print("GAME OVER")
            jugando = False
juego()

