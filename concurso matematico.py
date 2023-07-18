#operaciones aleatorias, con tiempo de 20 segundos, quien tenga mas puntos durante ese tiempo gana

import time
import random

puntos = 0
print('\n\n    CONCURSO MATEMATICO    \n\n')

def jugando():
    global puntos
    inicio = time.time()
    while True:
        operador = random.choice(["*", "+", "-"])
        numero1 = random.randint(1, 20)
        numero2 = random.randint(1, 20)
        if operador == "+":
            operacion = numero1 + numero2
        elif operador == "-":
            operacion = numero1 - numero2
        elif operador == "*":
            operacion = numero1 * numero2
        print(numero1, operador, numero2, "=")
        num = int(input("Ingrese el resultado: "))
        if num == operacion:
            puntos += 5
            print("Correcto, tienes", puntos, "puntos")
        else:
            print("Incorrecto, tienes", puntos, "puntos")
        final = time.time()
        if final - inicio >= 20:
            print("Se acabó el tiempo, conseguiste", puntos, "puntos")
            break

jugando()
