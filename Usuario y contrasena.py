#Introducir el usuario y la contraseña
print("\n\n                BIENVENIDO AL SISTEMA                 \n\n")

user = "AndHak"
password = "0000"
intentos = 1

while intentos <= 5:
    user_login = input("INGRESE EL USUARIO: ")
    password_login = input("INGRESE LA CONTRASEÑA: ")

    if user_login == user and password_login == password:
        print("\nBIENVENIDO AL SISTEMA SR ANDHAK\n")
        print("NUMERO DE INTENTOS PARA INGRESAR AL SISTEMA: ", intentos)
        intentos = 5  # Se establece en 5 para salir del bucle
    else:
        print("Usuario o contraseña incorrectos")
        print("Vas", intentos, "intentos. A los 5 intentos, se bloqueará el sistema")
        intentos += 1

if intentos > 5:
    print("\nEL SISTEMA SE HA BLOQUEADO. INTÉNTELO MÁS TARDE")
