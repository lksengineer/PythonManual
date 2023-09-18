# Dict Comprehension

# {expresion-clave:expresion-valor for variables in lista if condicion}
"""Esta instrucción genera el diccionario formado por los pares cuyas claves son el resultado de evaluar la expresión expresion-clave y cuyos valores son el resultado de evaluar la expresión expresion-valor, para cada valor que toma la variable variable, donde variable toma todos los valores de la lista lista que cumplen la condición condición."""

dict1 = {palabra: len(palabra) for palabra in ['I', 'love', 'Python']}
# {'I': 1, 'love': 4, 'Python': 6}
print(dict1)

notas = {
    'Carmen': 5,
    'Antonio': 4,
    'Juan': 8,
    'Mónica': 9,
    'María': 6,
    'Pablo': 3
}

dict2 = {name: note + 1 for (name, note) in notas.items() if note >= 5}
print(dict2)
# {'Carmen': 6, 'Juan': 9, 'Mónica': 10, 'María': 7}

# Con if Else
dict3 = {
    nombre: nota if nota == 10 else nota + 1
    for (nombre, nota) in notas.items()
}
# {'Carmen': 6, 'Antonio': 5, 'Juan': 9, 'Mónica': 10, 'María': 7, 'Pablo': 4}
print(dict3)
