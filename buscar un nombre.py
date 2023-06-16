nombres = ["Andres", "Felipe", "Stiven", "Juan"]
nombres = [nombre.lower() for nombre in nombres]
buscar = input("Buscar persona: ").lower()
esta = False

if buscar in nombres:
    esta = True

if esta:
    print("La persona llamada", buscar, "sí está en la lista.")
else:
    print("Esta persona no está en la lista.")
