nombre = str(input("Ingrese su primer nombre"))
nombre2 = str(input("Ingrese su segundo nombre"))
apellido = str(input("Ingrese su primer apellido"))
apellido2 = str(input("Ingrese su segundo apellido"))

nombre_completo = [nombre, nombre2, apellido, apellido2]

nombre_completo.pop(1)
nombre_completo.pop(-1)

print("Se mostrara en su perfil como: ", nombre_completo)