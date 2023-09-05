"""
Aplicar una función a todos los elementos de una colección iterable (map)

map(f, c) : Devuelve un objeto iterable con los resultados de aplicar la función f a los elementos de la colección c. 

Si la función f requiere n argumentos entonces deben pasarse n colecciones con los argumentos.

Para convertir el objeto en una lista, tupla o diccionario hay que aplicar explícitamente las funciones list(), tuple() o dic() respectivamente.
"""

def square(n):
  return n*n

result = list(map(func, [1, 2, 3]))
print(result)