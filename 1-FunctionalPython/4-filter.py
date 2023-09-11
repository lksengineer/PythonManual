# Filtrar los elementos de una colección iterable (filter)

"""filter(f, c) : Devuelve una objeto iterable con los elementos de la colección c que devuelven True al aplicarles la función f. Para convertir el objeto en una lista, tupla o diccionario hay que aplicar explícitamente las funciones list(), tuple() o dic() respectivamente.

 f debe ser una función que recibe un argumento y devuelve un valor booleano.
"""

# Mode 1
def par(n):
  return n % 2 == 0

pars = list(filter(par, range(10))) # [0, 2, 4, 6, 8]
print(pars)


# Mode 2: With Lambda
pars = list(filter(lambda num: num % 2 == 0, range(10)))
print(pars)