# En Python las funciones son objetos de primera clase, es decir, que pueden pasarse como argumentos de una función, al igual que el resto de los tipos de datos.


def apply(func, n):
  """Function to apply a function"""
  return func(n)

def square(n):
  """Function to calculate a square"""
  return n*n

def cube(n):
  """Function number ** 3"""
  return n**3

if __name__ == '__main__':
  print(apply(square, 2))
  
  cube = apply(cube, 3)
  print(cube)