#Programa que identifica los verbos de un texto
texto = str(input("Escriba el texto: "))
verbos = ["ar", "er", "ir"]
numero_de_verbos = 0

# Convertir el texto a minúsculas para una comparación más sencilla
texto = texto.lower()

# Dividir el texto en palabras
palabras = texto.split()

# Verificar si cada palabra es un verbo
for palabra in palabras:
    if palabra.endswith(tuple(verbos)):
        numero_de_verbos += 1

print("El número de verbos es:", numero_de_verbos)
