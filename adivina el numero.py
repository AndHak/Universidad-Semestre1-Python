import random

numero = random.randint(1, 100)

print("Adivina el número, tienes 7 intentos")
print("El número está entre 1 y 100.")

intentos = 0
jugando = True

while jugando:
    try:
        num = int(input('Ingresa un número: '))
        if num == numero:
            intentos += 1
            print('¡Correcto! El número era', numero)
            print('Has ganado, necesitaste', intentos, 'intentos')
            jugando = False
        else:
            intentos += 1
            if num < numero:
                print('El número es mayor que', num)
            else:
                print('El número es menor que', num)
            print('Llevas', intentos, 'intentos')
        
        if intentos == 7:
            print('Has perdido. El número era', numero)
            jugando = False
    except ValueError:
        print('Entrada inválida. Por favor, ingresa un número válido.')

