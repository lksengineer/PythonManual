# Combinar los elementos de varias colecciones iterables (zip)

"""
zip(c1, c2, ...) : 
Devuelve un objeto iterable cuyos elementos son tuplas formadas por los elementos que ocupan la misma posición en las colecciones c1, c2, etc. 

El número de elementos de las tuplas es el número de colecciones que se pasen. Para convertir el objeto en una lista, tupla o diccionario hay que aplicar explícitamente las funciones list(), tuple() o dic() respectivamente.
"""

# Mode 1
asignaturas = ['Matemáticas', 'Física', 'Química', 'Economía']
notas = [6.0, 3.5, 7.5, 8.0]

lista = list(zip(asignaturas, notas))
print(lista)
# [('Matemáticas', 6.0), ('Física', 3.5), ('Química', 7.5), ('Economía', 8.0)]

tupla = tuple(zip(asignaturas, notas))
print(tupla)

dictionary = dict(zip(asignaturas, notas[:3]))
print(dictionary)
# {'Matemáticas': 6.0, 'Física': 3.5, 'Química': 7.5}


# Mode 2:  Without Zip(), With Dict Comprenhesion
dictionary = {asignaturas[i]: notas[i] for i in range(len(asignaturas))}
print(f"Dict: {dictionary}")

# Mode 3:  Without Zip(), Without Dict Comprenhesion
dictionary = {}
for i in range(len(asignaturas)):
  dictionary[asignaturas[i]] = notas[i]
print(f"Dictionaries: {dictionary}")