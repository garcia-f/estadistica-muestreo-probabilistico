import json
import random
import statistics


poblacion = json.load(open("edades.json"))

edades = []
muestra = []




for individuo in poblacion:
    edades.append(individuo["age"])



edades_auxiliares = edades.copy()

for _ in range(0, 20):
    indice_random = random.randint(0, len(edades_auxiliares) - 1)
    valor = edades_auxiliares.pop(indice_random)
    muestra.append(valor)

print(muestra)
print( sum(muestra)/len(muestra) )
print( f'El promedio de la muestra es {statistics.mean(muestra)}' )


# muestreo sistematico

acc = 0
cantidad_muestra = 20

k = round( len( edades ) / cantidad_muestra  )
i = random.randint(1, k)

muestra_sistematica = []
muestra_sistematica.append(edades[i])


for j in range(0, 20):
    acc = i + (j + k)

    if acc <= len(edades) - 1:
        muestra_sistematica.append(edades[acc])
    else:
        muestra_sistematica.append( edades[acc - len(edades) ] )

print(muestra_sistematica)
print(statistics.mean(muestra_sistematica))


