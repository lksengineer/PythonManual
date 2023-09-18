# Operar todos los elementos de una colección iterable (reduce)
"""
reduce(f, l) : Aplicar la función f a los dos primeros elementos de la secuencia l. Con el valor obtenido vuelve a aplicar la función f a ese valor y el siguiente de la secuencia, y así hasta que no quedan más elementos en la lista. Devuelve el valor resultado de la última aplicación de la función f.

La función reduce está definida en el módulo functools.
"""

# Import reduce
from functools import reduce


def producto(n, m):
  return n * m


lista = reduce(producto, range(1, 5))  # 24
print(lista)
