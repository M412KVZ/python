# Archivo: 3 Cadenas y comillas.py
# Autor: ----------.
# Fecha: 21 de Abril del 2020
# Editor de Codigo: Visual Studio Code v1.47.2
# Descripcion: Cadenas, Tipos de Comillas, Repeticion y Concatenacion
#              de Cadenas.

# Introduccion

# Ejercicio 001
# En python existen varias formas de almacenar texto o una cadenas
# de texto que se conocen como "cadenas" o variables
# de tipo "string".
# La variable 'cads' la utilizaremos para encadenar un texto con
# comillas simples.
# La Variable "cadd" la utilizaremos para encadenar un texto con
# comillas dobles.

# 1 Comillas simples ('')
cads = "\'Texto entre comillas simples\'"

print (cads)

# 2 Comillas dobles ("")
cadd = "\"Texto entre Comillas dobles\""

print (cadd)

# Para hacer un salto de linea o interlineado se utilizan los caracteres
# de escape. El caracter "\n" es salto de linea y el caracter "\t" sirve 
# para hacer una tabulacion, aqui algunos ejemplos.

# Caracter \n 
cads = "\'Texto con salto \nde linea sin espacio (comillas simples)\'"
cadd = "\"Texto con salto \n de linea con espacio (comillas dobles)\""

print (cads)
print (cadd)

# Caracter \t
cads = '\tTexto con tabulacion Inicial'
cads1 = 'Texto tabulado \tsin espacio(comillas simples)'
cads2 = 'Texto tabulado \t con espacio(comillas simples)'
cads3 = 'Textto con doble \t\tTabulacion'

print (cads)
print (cads1)
print (cads2)
print (cads3)

cadd = "Texto con salto de \n\tlinea y tabulacion (Comillas dobles)"

print (cadd)

# Para hacer varios saltos de linea en una cadena de texto ocupamos 
# las comillas Triples (""")
# Las comillas triples permiten que las cadenas ocupen más de una línea-
cadc = """Saltos de lineas Linea 1
Linea 2
Linea 3
Linea 4
...
..
.
Linea N"""

print (cadc)

# Otro ejemplo
cadc = """Meses del Ano
Enero
Febrero
Marzo
Abril
...
..
.
Diciembre"""

print (cadc)

# Comillas dentro de comillas
# Se puede escribir comillas simples dentro de comillas dobles y 
# viceversa, pero si ponemos comillas dobles dentro de comillas dobles 
# nos marcara un error. Ejemplos (no se ponen ejemplos de error, ya que si
# se hace no se podria correr este archivo, pero usted puede sustituir las
# comillas en alguno de las casos siguientes para observar dicho error)
# "Las comillas dobles " delimitan cadenas" (el texto antes escrito dara un eeor
#  de sintaxis.)

cads = "Comillas simples '' dentro de comillas dobles"
cads1 = 'Comillas dobles "" dentro de comillas simples'

print (cads)
print (cads1) 

# Otra forma de escribir comillas en una cadena es utilizar los 
# caracteres especiles \' y \" que representan los caracteres comillas
# simples y dobles y que Python no interpreta en ningun caso como 
# delimitadores de cadenas, Ejemplos:

cads = 'Comillas simples \' dentro de comillas simples'
cads1 = "Comillas dobles\" dentro de comillas dobles"
cads2 = "\"Comillas dobles\" dentro de comillas dobles\""

print (cads)
print (cads1)
print (cads2)

# Deacuerdo con la guia de estilo oficial de Python las lineas de codigo
# no deben de contener mas de 79 caracteres para facilitar su 
# legibilidad y si contiene mas de 79 caracteres se debe partir en varias
# lineas.

# Repeticion y Concatenacion
# Repeticion de Cadenas

print ("Repeticion de Cadenas")

cad = "Cadena" * 3

print (cad)

print ("Concatenacion de Cadenas")

cad = "\nCadena" * 3

print (cad)

# Concatenacion de cadenas

cadena1 = ("Numero 1")
cadena2 = (" y Numero 2")
numeros = cadena1 + cadena2

print(numeros)

# Otro ejemplo de como imprimir una cadena

cad = "Numero 1"
cad2 = " y Numero 2"
cad3 = cad + cad2

print(cad3)

cad = "Nombre"
cad1 = " Apellido"
cad2 = cad + cad1

print (cad2)

# Fin del ejercicio.