#Contar cuantos o hay en un texto

cadena = """Muchos años después, frente al pelotón de fusilamiento, el coronel
Aureliano Buendía había de recordar aquella tarde remota en que su
padre lo llevó a conocer el hielo."""

numero_de_letras = len(cadena)
n = 0
repeticiones = 0

while n <= numero_de_letras-1:
    if cadena[n] == "o" or cadena[n] == "ó":
        repeticiones += 1
    n+=1

print(repeticiones)
