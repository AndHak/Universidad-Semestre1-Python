#Salir del bucle si se pasa de la temperatura

print('Temperaturas permitidas desde 5 hasta 12 C°')

def temperaturas():
    temperaturas = []
    while True:
        num = input('Presione "c" para terminar. Ingrese una temperatura: ')
        if num == "c":
            return temperaturas
        else:
            temperaturas.append(float(num))

temperaturas = temperaturas()
print(temperaturas)

for temperatura in temperaturas:
    if temperatura >= 5 and temperatura <= 12:
        print(temperatura, 'Temperatura permitida')
    else:
        print('ALERTA:', temperatura, 'Hay una temperatura no permitida')
        break
