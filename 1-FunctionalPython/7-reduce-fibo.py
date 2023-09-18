# Import reduce
from functools import reduce


# 0 1 1 2 3 5 8 13 21
def fibonacci(n):
  if n == 0:
    return n


# response = reduce(fibonacci, range(5 + 1))
number = input("Serie Fibonacci number: ")
fibonacci(number)
