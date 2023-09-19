"""
Tipos de excepciones
Los principales excepciones definidas en Python son:

TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
ImportError : Ocurre cuando falla la importación de un módulo.
Consultar la documentaciónde Python para ver la lista de exepciones predefinidas.

Control de excepciones
try - except - else
Para evitar la interrución de la ejecución del programa cuando se produce un error, es posible controlar la exepción que se genera con la siguiente instrucción:
"""
"""
try:
     bloque código 1
except excepción:
     bloque código 2
else:
     bloque código 3
"""
"""
Esta instrucción ejecuta el primer bloque de código y si se produce un error que genera una excepción del tipo excepción entonces ejecuta el segundo bloque de código, mientras que si no se produce ningún error, se ejecuta el tercer bloque de código.
"""


# Control de excepciones
def division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    print('¡No se puede dividir por cero!')
  else:
    print(result)


division(1, 0)
# ¡No se puede dividir por cero!
division(1, 2)
# 0.5

try:
  f = open('fichero.txt')  # El fichero no existe
except FileNotFoundError:
  print('¡El fichero no existe!')
else:
  print(f.read())
# ¡El fichero no existe!
