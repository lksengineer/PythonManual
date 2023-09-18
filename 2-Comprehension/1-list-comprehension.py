# List comprehension
# [expresion for variable in lista if condiction]
"""Esta instrucción genera la lista cuyos elementos son el resultado de evaluar la expresión expresion, para cada valor que toma la variable variable, donde variable toma todos los valores de la lista lista que cumplen la condición condición."""

list1 = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list1)

list2 = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
print(list2)

list3 = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
print(list3)

notas = {
    'Carmen': 5,
    'Antonio': 4,
    'Juan': 8,
    'Mónica': 9,
    'María': 6,
    'Pablo': 3
}
list4 = [f"{nombre}: {nota}" for (nombre, nota) in notas.items() if nota >= 5]
print(list4)
# ['Carmen', 'Juan', 'Mónica', 'María']
