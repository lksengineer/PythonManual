"""
Aplicar una función a todos los elementos de una colección iterable (map)

map(f, c) : Devuelve un objeto iterable con los resultados de aplicar la función f a los elementos de la colección c. 

Si la función f requiere n argumentos entonces deben pasarse n colecciones con los argumentos.

Para convertir el objeto en una lista, tupla o diccionario hay que aplicar explícitamente las funciones list(), tuple() o dic() respectivamente.
"""

# Mode 1
def square(n):
  return n * n

result = list(map(square, [1, 2, 3]))
print(result)

# Mode 2 with lambda
square = list(map(lambda n: n * n, [1, 2, 3]))
print(square)


# Mode 1: Rectangle with two(2) iterables
def rectangle(x, y):
  return x * y
  
rentangle = tuple(map(rectangle, (1, 2, 3), (2, 3, 4)))
print(rentangle)


# Mode 2: Rectangle with two(2) iterables and lambda
rentangle = tuple(map(lambda x, y: x * y, (1, 2, 3), (2, 3, 4)))
print(rentangle)
