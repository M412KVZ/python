# Archivo: 6 Tuplas.py
# Autor: ----------
# Fecha: 28 de Abril del 2017
# Editor de Codigo: Sublime Text 3 Built 3126
# Descripcion: Ejercicio 001.
#              Tuplas, Funcion "len()", Operaciones con Tuplas.

# Introduccion

# En Python una tupla es un conjuto ordenado e inmutable (que no 
# se pueden modificar) de elementos de un mismo tipo o  de diferente 
# tipo, pero es muy importante que esten separadas por comas, para 
# que Python la reconozca como una tupla. 
# En Pyrhon las tuplas se delimitan con parentesis "()".

print "Ejemplo de Tupla"

a = 1, "hola", 3.14 

print a
print ""

# Al escribir una tupla en Python la devuelve entre parentesis, 
# aunque no los pongamos, pero es muy recomendable que pongamos
# los parentesis y el contenido separado por comas para que 
# cuando estemos ecribiendo codigo sepamos que es una tupla.
# En este caso esta tupla contiene un numero entero, una cadena de 
# texto y un flotante (numero con decimales).

# La funcion "len()" devuelve la cantidad de elementos de una tupla.

print "Funcion \"len\""

a = (1, "hola", 3.14)
b = len((a))

print b # Se debe imprimir el numero "3".
print ""

# Una tupla puede no contener ningun elemento, es decir ser una tupla
# vacia.

print "Ejemplo de Tupla vacia"

a = ()
b = len((a))

print b # Se debe imprimir el numero "0".
print "" 

# Una tupla puede incluir un unico elemento, pero para que Python 
# entienda que nos estamos refiriendo a una tupla es necesario escribir 
# al menos una coma.

print "Ejemplo de tupla con un unico elemento"

a = (3,)
b = len((a))

print b # Se debe imprimir el numero "1".
print ""

# Python escribe una coma al final de las tuplas de un unico elemento
# para indicar que se trata de una tupla de un unico elemento.

print "Ejemplos de tupla con un unico elemento"

a = (3,)
b = len((a))

print a
print b # Se debe imprimir el numero "1".
print ""

# Tupla dentro de otra tupla

print "Tupla dentro de otra tupla"

a = ("uno", 2, 3.0, False, ("uno", 2, 3.0, False)) 
b = len((a))

print a
print b # Se debe imprimir el numero "5".
print ""

# Operaciones con Tuplas

# Las operaciones con tuplas son: Indexion de elementos, acceso a los 
# elementos de la tupla y concatenacion de tuplas.

# La indexion de elementos de una tupla se realiza con la funcion 
# "nombre_variable.index()" y nos servira para aprender a indexar solo de
# izquierda a derecha una tupla y saber acceder a los elementos de ella 
# posteriormenete. Si elegimos buscar un elemento que no se encuentra en 
# nuestra tupla nos marcara error.

print "Indexion de elementos de una tupla"

a = ("uno", 2, 3.0, False, "cinco", 6, 7.0, True)
b = a.index("uno")
c = a.index(2)

print b # Debe de dar el numero "0" ya que es el primer elemento de la tupla.
print c # Debe de car el numero "1" ya que es el segundo elemento de la tupla.
print ""

# Y asi sucesivamente con todos los elementos de la tupla para saber cual es
# el numero de indice de cada elemento. 

# Existen 2 formas de idexar los elementos de una tupla:
# 	* La primera es indexarlos de izquierda a derecha como anteriormente hemos 
#     visto, pero sin ocupar la funcion. desde donde se abre el primer 
#     parentesis de la tupla y asignando el numero "0" cero al primer elemento,
#     el numero "1" al segundo y asi sucesivamente hasta indexar todos los 
#     elementos de una tupla.
#	* La segunda es indexarlos de derecha a izquierda desde donde donde se 
#     cierra el ultimo parentesis de la tupla y asignarle el numero "-1" a ese 
#     elemento, el numero "-2" al segundo y asi sucesivamente hasta indexar 
#     todos los lementos de la tupla.

# Podemos acceder o referirnos a los elementos undividuales o en 
# conjunto de una tupla usando corchetes "[]" para un solo 
# elemento y dos puntos entre corchetes "[:]", "[::]" para indicar 
# el indice al cual se desea accesar.

print "Acceso a los elementos de una tupla de izquierda a derecha"

a = ("uno", 2, 3.0, False) # Tupla de 4 elemntos indexados (0,1,2,3).
b = a[0] # Aqui accedemos al indice "0" de nuestra tupla.

print a 
print b # Se debe imprimir el primer elemento de nuestra tupla ("uno").

a = ("uno", 2, 3.0, False) # Tupla de 4 elementos indexados (0,1,2,3).
b = a[1] # Aqui accedemos al segundo elemento de nuestra tupla (0,1).

print a 
print b # Se debe imprimir el segundo elemento de nuestra tupla (2).
print ""

print "Acceso a los elementos de una tupla de derecha a izquierda"

a = ("uno", 2, 3.0, False) # Tupla de 4 elementos indexados (0,1,2,3).
b = a[-1] # Aqui accedemos al ultimo elemento de nuestra tupla (False).

print a 
print b # Se debe imprimir el ultimo elemento de nuestra tupla (False).

a = ("uno", 2, 3.0, False) # Tupla de 4 elementos indexados (0,1,2,3).
b = a[-2] # Aqui accedemos al ultimo penelemento de nuestra tupla (3.0).

print a 
print b # Se debe imprimir el penultimo elemento de nuestra tupla (3.0).
print ""

# Acceso a multiples elementos de nuestra tupla

# Para acceder a un conjunto de elementos de nuestra tupla se hace 
# mediante "[:]" que devolvera el rango de esos numeros, el primer 
# numero significa el numero de indice, "[0:" (Recordemos que al indexar 
# una tupla el numero "0" hace refrencia al primer elemento de la tupla 
# y el segundo numero ":4]" devolvera hasta el elemento que queremos, 
# contando los elementos de izquierda a derecha.
# 	* [0:2], devolvera desde el primer elemento hasta el segundo 
#     elemento de la tupla, 
#   * otro ejemplo seria [2:5] que devolveria desde el tercer elemento 
#     hasta el quinto.
# Veamos algunos ejemplos

print "Accediendo a multiples elementos de una tupla de izquierda a derecha"

a = (3, "Hola", False, 5.165)
b = a[0:4]

print "Se deben imprimir todos los elementos de nuestra tupla"
print b # Se deben imprimir todos los elementos de nuestra tupla.

a = (3, "Hola", False, 5.165, 9)
b = a[2:5]

print "Se deben imprimir los ultimos 3 elementos de nuestra tupla"
print b # Se deben imprimir los 3 elementos de nuestra tupla (false, 5.165, 9).

# Si al acceder a una tupla el comienzo no es especificado, "[:9]" por 
# defecto es 0. 
# Si el fin no es especificado, "[5:]" por defecto es la cantidad de 
# elementos que contenga la tupla

a = (3, "Hola", False, 5.165)
b = a[:4] # Accediendo a una tupla con comienzo no especificado.

print "Se deben imprimir todos los elementos de nuestra tupla"
print b # Se deben imprimir todos los elementos de nuestra tupla.

a = (3, "Hola", False, 5.165)
b = a[0:] # Accediendo a una tupla con final no especificado.

print "Se deben imprimir todos los elementos de nuestra tupla"
print b # Se deben imprimir todos los elementos de nuestra tupla.

# Debemos recordar que al momento de accesar a elementos de una tupla que
# sean menores o iguales al indice, el resultado estara vacio "()".
# Una vez que se especifica un indice de inicio, digamos el valor "[1:",
# para que accedamos a un valor, el limite del rango tiene que ser al 
# menos 1 mayor que el indice, como en el ejemplo "[1:2]", esto devolvera 
# el elemento de 2 de una tupla y si el indice es el ultimo elemento de la
# tupla, si queremos que se imprima debemos dejar en blanco el limite del
# rango de la tupla a la que queremos acceder ejemplo de una tupla de 4 
# elementos se debera escribir "[3:]".
# Veamos algunos ejemplos

print "Ejemplos de (), al acceder a una tupla de izquierda a derecha"

a = (3, "Hola", False, 5.165)
b = a[1:1]

print "Se debe imprimir (), al acceder a nuestra tupla"
print b # No devolvera ningun valor. 

a = (3, "Hola", False, 5.165)
b = a[3:3]

print "Se debe imprimir (), al acceder a nuestra tupla"
print b # No devolvera ningun valor. 

a = (3, "Hola", False, 5.165)
b = a[1:2]

print "Se debe imprimir el segundo elemento, de nuestra tupla"
print b # Se debe imprimir (Hola).
print ""

# Acceder a los elementos de una tupla de derecha a izquierda

# Al igual que accedemos a elementos individiales de derecha a izquierda en 
# nuestra tupla, podemos acceder a un conjunto de elementos de nuestra tupla.
# Recordemos que que el ultimo elemento de nuestra tupla es "[-1:", pero para 
# asignar el rango hasta el cual queremos llegar, debemos asignar este numero 
# como positivo, "[-8:8]" esto devolvera todos los elementos de la tupla.
# Veamos algunos ejemplos.

print "Accediendo a multiples elementos de una tupla de derecha a izquierda"

a = ("uno", 2, 3.0, True, "cinco", 6, 7.0, False)
b = a[-8:8]

print "Se deben imprimir todos los elementos de nuestra tupla"
print b # Se imprimiran todos los elementos de la tupla.

a = ("uno", 2, 3.0, True, "cinco", 6, 7.0, False)
b = a[-6:3]

print "Se debe imprimir el elemento 3 de la tupla"
print b # Se debe imprimir (3.0).
print ""

# Al igual que cuando queremos acceder de izquierda a derecha a un elemento 
# menor que el indice, la tupla no nos devuelve ningun valor "()", vemos un 
# fecto similar al momento de querer acceder de derecha a izquierda a una 
# tupla, y observamos que debemos escoger un limite menor al indice, si 
# tenemos una tupla de 8 elementos y queremos acceder a ella de derecha a 
# izquierda, por ejemplo "[-7:, que seria el segundo elemento de 8 
# elementos de nuestra tupla, solo quedarian para acceder los elementos 
# 3,4,5,6,7,8 y no se podria acceder al primer elemento de nuestra tupla.

print "Ejemplos de (), al acceder a una tupla de derecha a izquierda"

a = ("uno", 2, 3.0, True, "cinco", 6, 7.0, False)
b = a[-7:0]

print "Se debe imprimir (), al acceder a nuestra tupla"
print b # No devolvera ningun valor. 

a = ("uno", 2, 3.0, True, "cinco", 6, 7.0, False)
b = a[-1:0]

print "Se debe imprimir (), al acceder a nuestra tupla"
print b # No devolvera ningun valor.
print ""

# Accediendo a tuplas dentro de otras tuplas
# Para acceder al elemento de una tupla que de encuentra de dontro de otra
# tupla, se hace referencia de la siguiente forma "[5][3]", el numero "[5]"
# indica que es el sexto elemento de nuestra tupla y el numero "[3]" indica 
# que accesara al ultimo elemento de nuestra segunda tupla. 

print "Accediendo a una tuplas dentro de otra tupla" 

a = ("uno", 2, 3.0, False, "cinco", (6, 7.0, True, "ocho"))
b = a[5][3]

print b # Se imprimira "ocho".
print ""

# Accesiendo a un rango especifico de elementos en una tupla

# Para acceder a un rango de elementos especificos dentro de otro rango en una
# tupla se hace de la forma "[ : : ]", donde el primer numero es el indice y 
# por ello el inicio del rango (si no se escribe nada se tomara como indice 
# "0" o primer elemento de la tupla), el segundo  numero  es el limite y final 
# del rango (si no se escribe un numero se tomara como limite el ultimo 
# ellemento de nuestra tupla), y el tercer numero indica el rango de numeros 
# queremos que sean de la forma un numero si, un numero no, o de la forma un 
# numero si, dos numeros no y asi sucesivamente.
# [::2] esto indicara que de todos los numero de la tupla, queremos acceder a
# un numero si y un mumero no (1,3,5,7... etc).
# [:20:2] lo mismo indica esto y esto [0::2].
# [::-5] esto indicara que queremos acceder desde el ultimo numero hacia el 
# primero de 5 en 5 numeros osea el resultado seria [20,15,10,5].

print "Accediendo a un rango especifico de elementos en una tupla"

a = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
b = a[::2]

print b # Se deben imprimir los numero (1,3,5,7,9,11,13,15,17,19).
print ""

# Concatenacion de Tuplas
# Se pueden concatenar 2 o mas tuplas y en el orden que nosotros que ramos y
# se creara una tupla mas grande. veamos algunos ejemplos:

print "Concatenacion de tuplas" 

a = (1,2,3,4,5,6)
b = (12,13,14,15)
c = (7,8,9,10,11)

print a + c # Debe imprimir (1,2,3,4,5,6,7,8,9,10,11).
print a + c + b # Debe imprimir (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15).
print ""

# Busqueda de elementos en una tupla
# Para realizar la busqueda de un elemento especifico o dos en una tupla
# Utlizaremos las funciones; "in" para buscar un solo elemento y "and"
# para buscar 2 elementos.
# Recordemos que para que "and" arroje un valor "True" los dos elementos a 
# buscar deben existir en la tupla, de lo contrario dara false.

print "Busqueda de elementos en una tupla"

a = ("Nombre", "SegundoNombre", "ApellidoPaterno", "ApellidoMaterno", "Edad")
b = "Nombre" in a
c = "Nombre" and "SegundoNombre" in a
d = "XXXXX" in a
e = "Edad" and 56.98 in a

print b # Se debe imprimir True.
print c # Se debe imprimie True.
print d # Se debe imprimie False
print e # Se debe imprimie False

# *****NOTA*****
# DEBEMOS DE RECORDAR QUE LA TUPLAS SON ELEMENTOS INMUTABLES Y NO SE PUEDEN
# CAMBIAR O AGREGAR MAS ELEMENTOS A LAS TUPLAS COMO EN LAS LISTAS.

# Fin del ejercicio.