Nombres = ["Andres", "Luis", "Miguel", "Mateo", "Stiven", "Pablo"]
identificaciones = [1004509807, 92817282, 222222222, 33333333, 444444444444, 555555555555]

for nombre, identificacion in zip(Nombres, identificaciones):
    print(f"Nombre: {nombre}, Identificación: {identificacion}")
