edades = [20, 30, 32, 27, 19]

#Recoriendo los elementos
for edad in edades:
    print(edad)

#Recoriendo los indices
print("")
for i in range(len(edades)):
    print(edades[i])

#Con while y los indices
indice = 0

print("")
while indice < len(edades):
    print(edades[indice])
    indice += 1
