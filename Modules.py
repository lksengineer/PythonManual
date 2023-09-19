"""Módulos
El código de un programa en Python puede reutilizarse en otro importándolo. Cualquier fichero con código de Python reutilizable se conoce como módulo o librería.

Los módulos suelen contener funciones reutilizables, pero también pueden definir variables con datos simples o compuestos (listas, diccionarios, etc), o cualquier otro código válido en Python.

Python permite importar un módulo completo o sólo algunas partes de él. Cuando se importa un módulo completo, el intérprete de Python ejecuta todo el código que contiene el módulo, mientras que si solo se importan algunas partes del módulo, solo se ejecutarán esas partes.

Importación completa de módulos (import)
import M : Ejecuta el código que contiene M y crea una referencia a él, de manera que pueden invocarse un objeto o función f definida en él mediante la sintaxis M.f.

import M as N : Ejecuta el código que contiene M y crea una referencia a él con el nombre N, de manera que pueden invocarse un objeto o función f definida en él mediante la sintaxis N.f. Esta forma es similar a la anterior, pero se suele usar cuando el nombre del módulo es muy largo para utilizar un alias más corto.

Importación parcial de módulos (from import)
from M import f, g, ... : Ejecuta el código que contiene M y crea referencias a los objetos f, g, ..., de manera que pueden ser invocados por su nombre. De esta manera para invocar cualquiera de estos objetos no hace falta precederlos por el nombre del módulo, basta con escribir su nombre.

from M import * : Ejecuta el código que contiene M y crea referencias a todos los objetos públicos (aquellos que no empiezan por el carácter _) definidos en el módulo, de manera que pueden ser invocados por su nombre.

Cuando se importen módulos de esta manera hay que tener cuidado de que no haya coincidencias en los nombres de funciones, variables u otros objetos.

>>> import calendar
>>> print(calendar.month(2019, 4))
April 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
>>> from math import *
>>> cos(pi)
-1.0
Módulos de la librería estándar más importantes
Python viene con una biblioteca de módulos predefinidos que no necesitan instalarse. Algunos de los más utilizados son:

sys: Funciones y parámetros específicos del sistema operativo.
os: Interfaz con el sistema operativo.
os.path: Funciones de acceso a las rutas del sistema.
io: Funciones para manejo de flujos de datos y ficheros.
string: Funciones con cadenas de caracteres.
datetime: Funciones para fechas y tiempos.
math: Funciones y constantes matemáticas.
statistics: Funciones estadísticas.
random: Generación de números pseudo-aleatorios.
Otras librerías imprescindibles
Estas librerías no vienen en la distribución estándar de Python y necesitan instalarse. También puede optarse por la distribución Anaconda que incorpora la mayoría de estas librerías.

NumPy: Funciones matemáticas avanzadas y arrays.
SciPy: Más funciones matemáticas para aplicaciones científicas.
matplotlib: Análisis y representación gráfica de datos.
Pandas: Funciones para el manejo y análisis de estructuras de datos.
Request: Acceso a internet por http."""