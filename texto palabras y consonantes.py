#Programa que cuenta las vocales y las consnantes de un texto, muestra el numero total de letras

texto = str(input("Ingrese el texto:  "))
i = 0
vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnñpqrstvwxyz"
repeticiones_vocales = 0
repeticiones_consonantes = 0
total_letras = 0

while i <= len(texto)-1:
    if texto.lower()[i] in vocales:
        repeticiones_vocales += 1
    if texto.lower()[i] in consonantes:
        repeticiones_consonantes += 1
    i += 1

total_letras = repeticiones_consonantes + repeticiones_vocales

print("NUMERO DE VOCALES:  ", repeticiones_vocales)
print("NUMERO DE CONSONANTES:  ", repeticiones_consonantes)
print("NUMERO TOTAL DE LETRAS:  ", total_letras)
