# Archivo: 4 Booleanos.py
# Autor: **********.
# Fecha: 21 de Abril del 2017
# Editor de Codigo: Sublime Text 3 Built 3126
# Descripcion: Ejercicio 001.
#              Booleanos, Operadores Logicos, Operaciones 
#              Compuestas y Comparaciones.

# Introduccion

# Las variables booleanas o los booleanos son datos de tipo logico y 
# solo pueden tomar dos posibles valores, verdadero o falso 
# ("True" o "False"). Al escribir los booleanos "True o False" la
# primera letra debe ser mayuscula para que se reconozca como un 
# booleano, de lo contrario dara un error.

# Booleanos

# En Python cualquier variable (en general, cualquier objeto) puede 
# considerarse como una variable booleana.
# Ejemplos de False 

print("Ejemplos de False")

a = bool(0)
b = bool("")
c = bool(None)
d = bool(())
e = bool([])
f = bool({})

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Ejemplos de True

print("Ejemplos de \'True\'")

a = bool(25)
b = bool(-9.5)
c = bool("abc")
d = bool((1, 2, 3))
e = bool([27, "Octubre", 1997])
f = bool({27, "Octubre", 1997})

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Operadores Logicos

# Los operadores logicos son operaciones que trabajan con 
# operadores booleanos. Existen 3 tipos de operadores logicos que son
# "and", "or" y "not", (y, o, negacion, respectivamente)

# "and"
# Este operador da como resultado "True" si, y solo si, sus dos operandos
# son "True" Ejemplos:

print("Ejemplos \'and\'")

a = True and True
b = True and False
c = False and True
d = False and False

print(a)
print(b)
print(c)
print(d)

# Como podran ver solo el primer resultado fue "True", ya que solo la
# primera operacion contiene sus dos operandos "True".

# "or"
# Este operador da como resultado "True" si algun operando es "True"

print("Ejemplos \'or\'")

a = True or True
b = True or False
c = False or True
d = False or False

print(a)
print(b)
print(c)
print(d)

# Como podran ver los 3 primeros resultados fueron "True" ya que en
# estas operaciones existia al menos un operando "True".

# "not"
# Negacion. Este Operador da como resultado "True", solo y solo si
# su argumento es "False".

print("Ejemplos \'not\'")

a = not True
b = not False

print(a)
print(b)

# Es como la ley de los signos en multiplicacion, 
# menos * mas = menos, en este caso "False"
# menos * menos = mas, en este caso "True"

# Operaciones Compuestas
# Son operaciones con 2 o mas operandos "and", "or" o "not".

# ***NOTA***

# Si no se esta acostumbrado a realizar operacions logicas compuestas
# se recomienda utilizar parentesis para asegurar el orden de las 
# operaciones

# ***NOTA***
# Existe una regla de como Python evalua los operadores logicos
# "not" antes que "and" y "or"
# "and" antes que "or"
# Veamos unos ejemplos de "not" antes que "and"

print("Ejemplos de Operaciones Compuestas \'not\' antes que \'and\'")

a = not True and False
b = (not True) and False
c = not (True and False)

print(a)
print(b)
print(c)

a = not False and True
b = (not False) and True
c = not (False and True)

print(a)
print(b)
print(c)

# Aplicando lal ley de multiplicacion de signos comprobaremos que 
# los resultados son correctos

# Ahora veamos unos ejemplos de "not" antes que "or"

print("Ejemplos de Operaciones compuestas \'not\' antes que \'or\'")

a = not True or False
b = (not True) or False
c = not (True or False)

print(a)
print(b)
print(c)

a = not False or True
b = (not False) or True
c = not (False or True)

print(a)
print(b)
print(c)

# Aplicando lal ley de multiplicacion de signos comprobaremos que 
# los resultados son correctos

# Ahora veamos unos ejemplos de "and" antes que "or"

print("Ejemplos de Operaciones compuestas \'and\' antes que \'or\'")

a = False and True or True
b = (False and True) or True
c = False and (True or True)

print(a)
print(b)
print(c)

a =  True and False or True
b = (True and False) or True
c = True and (False or True)

print(a)
print(b)
print(c)

a = True or True and False
b = (True or True) and False
c = True or (True and False)

print(a)
print(b)
print(c)

# Si en las expresiones logicas se utilizan valores distintos de
# "True" o "False", Python Utiliza esos valores en vez de "True"
# o "False".

print("""Ejemplos de Python utilizando valores distintos de 
\"True\" o \"False\"""")

a = 3 or 4
b = 7 or 8
c = 1 or -7

print(a)
print(b)
print(c)

a = bool (3)
b = bool (0)

c = a or b 
d = b or c

print(a)
print(b)
print(c)

# Las comparaciones tambien dan como resultados valores 
# booleanos.

# Mayor que ">" o menor que "<"

print("Ejemplos de comparaciones mayor que \">\" y menor que \"<\"")

a = 3 > 2
b = 3 < 2

print(a)
print(b)

# Mayor o igual que ">=" y menor o igual que "<="

print("""Ejemplos de comparaciones mayor o igual que \">=\" y menor
o igual que \"<=\"""")

a = 2 >= 1 + 1
b = 4 - 2 <= 1

print(a)
print(b)

# Igual que "==" y distinto de "!="

print("Ejemplos de Igual que \"==\" y distinto de \"!=\"")

a = 2 == 1 + 1
b = 6 / 2 != 3

print(a)
print(b)

# Es importante decir que en matematicas el signo igual se utiliza 
# tanto en las asignaciones como en las compraciones, mientras que en
# Python, y en muchos otros lenguajes de programacion:
# 	*Un signo igual "=" significa asignacion, es decir almacenar el
#  	 valor en una variable.
# 	*Mientras que dos signos seguidos "==" significan comparacion, es
# 	 decir que si es verdad o mentira que dos expresiones son iguales.

# Python permite encadenar varias comparaciones y el resultado 
# sera verdadero si y solo si todos las comparaciones lo son.

print("Ejemplos de encadenamiento de varias comparaciones")

a = 4 == 3 + 1 > 2
b = 2 != 1 + 1 > 0

print(a)
print(b)

# Encadenar comparaciones no esta permitido en otros lenguajes de 
# programacion como PHP en los que las comparaciones deben combinarse
# mediante operasdores logicos como "and", lo que tambien puede
# hacerse en Python.

print("""Ejemplos de encadenamientos de comparaciones y operadores
y operadores logicos""")

a = 4 == 3 + 1 and 3 + 1 > 2
b = 2 != 1 + 1 and 1 + 1 > 0

print(a)
print(b)

# Fin del ejercicio.