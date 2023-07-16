#Registro de personas y conteo de asistencias

import datetime

registro = []
registrando = True

while registrando:
    nombre = input("\nNombre: ")
    hora_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro.append((nombre, hora_registro))
    continuar = input("¿Desea registrar otro usuario? (si/no): ")
    if continuar.lower() == "si":
        registrando = True
    else:
        registrando = False

print("\nLAS ASISTENCIAS FUERON\n")
contador = {}

for nombre, _ in registro:
    if nombre in contador:
        contador[nombre] += 1
    else:
        contador[nombre] = 1

for nombre, asistencias in contador.items():
    print(f"{nombre} asistió {asistencias} veces.")

print("\nDETALLES DE REGISTRO\n")
for nombre, hora_registro in registro:
    print(f"{nombre}: Registrado el {hora_registro}")
