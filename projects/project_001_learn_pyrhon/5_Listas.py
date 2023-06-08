# -*- coding: utf-8 -*-
# Archivo: 5 Listas.py
# Autor: ----------
# Fecha: 27 de Abril del 2017
# Editor de Codigo: Sublime Text 3 Built 3143
# Descripcion: Listas.
# Ejercicio: 001.

# Introduccion

# Las listas son conjuntos ordenados de elementos [2.0, "Tres", [1], etc.].
# Las listas se delimitan por corchetes "[]" y se separan por comas "[,]"
# En Python las listas son elementos mutables (osea que pueden cambiar).
# En otros lenguajes se les conoce como arreglos o vectores.

print "Ejemplo de lista"

a = [1, "hola", 3.14]

print a
print ""

# Debemos recordar que una lista siempre debe estar entre corchetes "[]"
# y separada por comas, ya que si no estan bien estructuradas esto ocasiona
# muchos errores al ejecutar codigo.
# En este caso esta lista contiene un numero entero, una cadena de texto y un
# flotante (numero con decimales).

# La funcion "len()" devuelve la cantidad de elementos de una lista.

print "Funcion \"len\""

a = [1, "hola", 3.14]
b = len(a)

print b  # Se debe imprimir el numero "3".
print ""

# Una lista puede no contener ningun elemento, es decir ser una tupla vacia.

print "Ejemplo de lista vacia"

a = []
b = len(a)

print b  # Se debe imprimir el numero "0".
print ""

# Una tupla puede incluir un unico elemento.

print "Ejemplo de lista con un unico elemento"

a = [3]
b = len(a)

print b  # Se debe imprimir el numero "1".
print ""

# Lista dentro de otra lista.

print "Ejemplo de lista dentro de otra lista"

a = ["uno", 2, 3.0, False, ["uno", 2, 3.0, False]]
b = len(a)

print a
print b  # Se debe imprimir el numero "5".
print ""

# Operaciones con listas

# Las operaciones con lista son: Indexion de elementos, acceso a los
# elementos de la lista, concatenacion de listas,

# La indexion de elementos de una lista se realiza con la funcion
# "nombre_variable.index()" y nos servira para aprender a indexar solo de
# izquierda a derecha una lista y saber acceder a los elementos de ella
# posteriormenete. Si elegimos buscar un elemento que no se encuentra en
# nuestra lista nos marcara error.

print "Indexion de elementos de una lista"

a = ["uno", 2, 3.0, False, "cinco", 6, 7.0, True]
b = a.index("uno")
c = a.index(2)

print b  # Dara el numero "0" ya que es el primer elemento de la lista.
print c  # Dara el numero "1" ya que es el segundo elemento de la lista.
print ""

# Y asi sucesivamente con todos los elementos de la lista para saber cual es
# el numero de indice de cada elemento.

# Existen 2 formas de idexar los elementos de una lista:
# 	* La primera es indexarlos de izquierda a derecha como anteriormente hemos
#     visto, pero sin ocupar la funcion. desde donde se abre el primer
#     corchete de la lista y asignando el numero "0" cero al primer elemento,
#     el numero "1" al segundo y asi sucesivamente hasta indexar todos los
#     elementos de una lista.
#   * La segunda es indexarlos de derecha a izquierda desde donde donde se
#     cierra el ultimo corchete de la lista y asignarle el numero "-1" a ese
#     elemento, el numero "-2" al segundo y asi sucesivamente hasta indexar
#     todos los lementos de la lista.

# Podemos acceder o referirnos a los elementos undividuales o en conjunto de
# una lista usando corchetes "[]" para un solo
# elemento y dos puntos entre corchetes "[:]", "[::]" para indicar
# el indice al cual se desea accesar.

print "Acceso a los elementos de una lista de izquierda a derecha"

a = ["uno", 2, 3.0, False]  # Lista de 4 elemntos indexados [0,1,2,3].
b = a[0]  # Aqui accedemos al indice "0" de nuestra lista.

print a
print b  # Se debe imprimir el primer elemento de nuestra lista "uno".

a = ["uno", 2, 3.0, False]  # Lista 4 elementos indexados [0,1,2,3].
b = a[1]  # Aqui accedemos al segundo elemento de nuestra lista [0,1].

print a
print b  # Se debe imprimir el segundo elemento de nuestra lista "2".
print ""

print "Acceso a los elementos de una lista de derecha a izquierda"

a = ["uno", 2, 3.0, False]  # lista de 4 elementos indexados [0,1,2,3].
b = a[-1]  # Aqui accedemos al ultimo elemento de nuestra lista "False".

print a
print b  # Se debe imprimir el ultimo elemento de nuestra lista "False".

a = ["uno", 2, 3.0, False]  # Lista de 4 elementos indexados [0,1,2,3].
b = a[-2]  # Aqui accedemos al ultimo penelemento de nuestra lista "3.0".

print a
print b  # Se debe imprimir el penultimo elemento de nuestra lista "3.0".
print ""

# Acceso a multiples elementos de nuestra lista

# Para acceder a un conjunto de elementos de nuestra lista se hace mediante
# "[:]" que devolvera el rango de esos numeros, el primer numero significa el
# numero de indice, "[0:" (Recordemos que al indexar una lista el numero "0"
# hace refrencia al primer elemento de la lista y el segundo numero ":4]"
# devolvera hasta el elemento que queremos, contando los elementos de
# izquierda a derecha.
# 	* [0:2], devolvera desde el primer elemento hasta el segundo
#     elemento de la lista.
#   * otro ejemplo seria [2:5] que devolveria desde el tercer elemento
#     hasta el quinto de la lista.
# Veamos algunos ejemplos

print "Accediendo a multiples elementos de una lista de izquierda a derecha"

a = [3, "Hola", False, 5.165]
b = a[0:4]

print "Se deben imprimir todos los elementos de nuestra lista"
print b  # Se deben imprimir todos los elementos de nuestra lista.

a = [3, "Hola", False, 5.165, 9]
b = a[2:5]

print "Se deben imprimir los ultimos 3 elementos de nuestra lista"
print b  # Se deben imprimir los 3 elementos de nuestra lista [false, 5.165,
#           9].
# Si al acceder a una lista el comienzo no es especificado, "[:9]" por
# defecto es 0.
# Si el fin no es especificado, "[5:]" por defecto es la cantidad de
# elementos que contenga la lista.

a = [3, "Hola", False, 5.165]
b = a[:4]  # Accediendo a una lista con comienzo no especificado.

print "Se deben imprimir todos los elementos de nuestra lista"
print b  # Se deben imprimir todos los elementos de nuestra lista.

a = [3, "Hola", False, 5.165]
b = a[0:]  # Accediendo a una lista con final no especificado.

print "Se deben imprimir todos los elementos de nuestra lista"
print b  # Se deben imprimir todos los elementos de nuestra lista.

# Debemos recordar que al momento de accesar a elementos de una lista que
# sean menores o iguales al indice, el resultado estara vacio "[]".
# Una vez que se especifica un indice de inicio, digamos el valor "[1:",
# para que accedamos a un valor, el limite del rango tiene que ser al
# menos 1 mayor que el indice, como en el ejemplo "[1:2]", esto devolvera
# el elemento de 2 de una lista y si el indice es el ultimo elemento de la
# lista, si queremos que se imprima debemos dejar en blanco el limite del
# rango de la lista a la que queremos acceder ejemplo de una lista de 4
# elementos se debera escribir "[3:]".
# Veamos algunos ejemplos

print "Ejemplos de [], al acceder a una lista de izquierda a derecha"

a = [3, "Hola", False, 5.165]
b = a[1:1]

print "Se debe imprimir [], al acceder a nuestra lista"
print b  # No devolvera ningun valor.

a = [3, "Hola", False, 5.165]
b = a[3:3]

print "Se debe imprimir [], al acceder a nuestra lista"
print b  # No devolvera ningun valor.

a = [3, "Hola", False, 5.165]
b = a[1:2]

print "Se debe imprimir el segundo elemento, de nuestra lista"
print b  # Se debe imprimir "Hola".
print ""

# Acceder a los elementos de una lista de derecha a izquierda

# Al igual que accedemos a elementos individiales de derecha a izquierda en
# nuestra lista, podemos acceder a un conjunto de elementos de nuestra lista.
# Recordemos que que el ultimo elemento de nuestra lista es "[-1:", pero para
# asignar el rango hasta el cual queremos llegar, debemos asignar este numero
# como positivo, "[-8:8]" esto devolvera todos los elementos de la lista.
# Veamos algunos ejemplos.

print "Accediendo a multiples elementos de una lista de derecha a izquierda"

a = ["uno", 2, 3.0, True, "cinco", 6, 7.0, False]
b = a[-8:8]

print "Se deben imprimir todos los elementos de nuestra lista"
print b  # Se imprimiran todos los elementos de la lista.

a = ("uno", 2, 3.0, True, "cinco", 6, 7.0, False)
b = a[-6:3]

print "Se debe imprimir el elemento 3 de la lista"
print b  # Se debe imprimir "3.0".
print ""

# Al igual que cuando queremos acceder de izquierda a derecha a un elemento
# menor que el indice, la lista no nos devuelve ningun valor "[]", vemos un
# fecto similar al momento de querer acceder de derecha a izquierda a una
# lista, y observamos que debemos escoger un limite menor al indice, si
# tenemos una lista de 8 elementos y queremos acceder a ella de derecha a
# izquierda, por ejemplo "[-7:, que seria el segundo elemento de 8
# elementos de nuestra lista, solo quedarian para acceder los elementos
# 3,4,5,6,7,8 y no se podria acceder al primer elemento de nuestra lista.

print "Ejemplos de [], al acceder a una lista de derecha a izquierda"

a = ["uno", 2, 3.0, True, "cinco", 6, 7.0, False]
b = a[-7:0]

print "Se debe imprimir [], al acceder a nuestra lista"
print b  # No devolvera ningun valor.

a = ["uno", 2, 3.0, True, "cinco", 6, 7.0, False]
b = a[-1:0]

print "Se debe imprimir [], al acceder a nuestra lista"
print b  # No devolvera ningun valor.
print ""

# Accediendo a lista dentro de otras listas
# Para acceder al elemento de una lista que de encuentra de dontro de otra
# lista, se hace referencia de la siguiente forma "[5][3]", el numero "[5]"
# indica que es el sexto elemento de nuestra lista y el numero "[3]" indica
# que accesara al ultimo elemento de nuestra segunda lista.

print "Accediendo a una lista dentro de otra lista"

a = ["uno", 2, 3.0, False, "cinco", [6, 7.0, True, "ocho"]]
b = a[5][3]

print b  # Se imprimira "ocho".
print ""

# Accesiendo a un rango especifico de elementos en una lista

# Para acceder a un rango de elementos especificos dentro de otro rango en una
# lista se hace de la forma "[ : : ]", donde el primer numero es el indice y
# por ello el inicio del rango (si no se escribe nada se tomara como indice
# "0" o primer elemento de la lista), el segundo  numero  es el limite y final
# del rango (si no se escribe un numero se tomara como limite el ultimo
# ellemento de nuestra lista), y el tercer numero indica el rango de numeros
# queremos que sean de la forma un numero si, un numero no, o de la forma un
# numero si, dos numeros no y asi sucesivamente.
# [::2] esto indicara que de todos los numero de la lista, queremos acceder a
# un numero si y un mumero no [1,3,5,7... etc].
# [:20:2] lo mismo indica esto y esto [0::2].
# [::-5] esto indicara que queremos acceder desde el ultimo numero hacia el
# primero de 5 en 5 numeros osea el resultado seria [20,15,10,5].

print "Accediendo a un rango especifico de elementos en una lista"

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = a[::2]

print b  # Se deben imprimir los numero [1,3,5,7,9,11,13,15,17,19].
print ""

# Modificacion de listas
# En una lista se pueden modificar uno o varios elementos de ella o tambien
# pueden sustituirse un elemento por varios de ella o viceversa.

print "Modificacion de listas"

a = [1, 2, 3, 4, 5, 6]
a[0:2] = [7, 8]  # Se sustituyen los elementos 1 y 2 por los numeros 7 y 8.

print a  # Se deben imprimir los valores 7,8,3,4,5,6.

a = [1, 2, 8, 9, 10, 11]
a[2:] = [3]  # Se indica que se deben sustituir varios elementos por uno solo.

print a  # Se debe imprimir "1,2,3".
print""

# Tambien hay que tener en cuenta que algunos metodos de sustitucion, adicion
# de elementos pueden afectar o no el resultado.

# Agregar elementos a las listas
# Se pueden agregar elementos a una lista utilizando los siguientes operandos.
# El metodo "append()" agrega el elemento al final de la lista. Cabe mencionar
# que este metodo afecta el resultado si se hace referencia a el en 2 o mas
# variables al momento de concatenarlas.

# Concatenacion de listas
# Se pueden concatenar 2 o mas listas y en el orden que nosotros queramos y
# se creara una lista mas grande. veamos algunos ejemplos:

print "Concatenacion de listas"

a = [1, 2, 3, 4, 5, 6]
b = [12, 13, 14, 15]
c = [7, 8, 9, 10, 11]

print a + c  # Debe imprimir [1,2,3,4,5,6,7,8,9,10,11].
print a + c + b  # Debe imprimir [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15].
print ""

# Podemos agregar un elemento a una lista o concatenarla con otra lista, sin
# necesidad de modifcar las demas listas que dependan de la primera.

print """Concatenacion y modificacion de una lista sin modificar las demas
listas"""

a = [1, 2, 3]
b = a  # Aqui indicamos que nuestra variable "b" es lo mismo que "a".
c = b  # Aqui indicamos que nuestra variable "c" es lo mismo que "b".

print a, b  # Se debe  imprimir [1,2,3] [1.2.3].
print a, b, c  # Se debe  imprimir [1,2,3] [1.2.3] [1,2,3].

a = a + [4]  # Aqui indicamos que agregamos un elemento a nuestra variable "a"
#              y que solo nuestra variable "a" se modificara y las demas
#              variables seguiran teniendo los mismos elementos que se han
#              designado en nuestra primera variable "a" al principio.

print a  # Se debe imprimir [1,2,3,4].
print a, b  # Se debe imprimir [1,2,3,4] [1,2,3].
print a, b, c  # Se debe imprimir [1,2,3,4] [1,2,3] [1,2,3].

# Esto es muy util al momento de hacer actualizaciones de las versiones
# software, ya que nos ahorra  mucho tiempo al estar ecribiendo codigo, pero
# debemos recordar que si no lo hacemos bien u ocupamos otro operador o metodo
# de adicion de elementos o concatenacion de listas, estas modificaran todas
# las variables que de ella dependan como veremos adelante.

print ""

# Tambien se puede utilizar el operador += para agregar elementos a una lista
# aunque en estos ejemplos, los operadores + y += den el mismo resultado, no
# son equivalentes,como otros que veremos ya que pueden cambiar la estructura
# del resultado como se explicara mas adelante al concatenar varias listas que
# hacen referencia a variables que dependen de otras.

print "Concatenacion de listas con el operando \"+=\""

a = [1, 2, 3,]
a += [4]  # Se agregara el numero "4" al final de la lista.

print a  # Se debe imprimir [1,2,3,4].
print ""

print "Operando \"+=\" modificando una concatenacion de listas"

a = [1, 2, 3]
b = a  # Aqui indicamos que nuestra variable "b" es lo mismo que "a".
c = b  # Aqui indicamos que nuestra variable "c" es lo mismo que "b".
d = c  # Aqui indicamos que nuestra variable "d" es lo mismo que "c".

print a, b  # Se debe  imprimir [1,2,3],[1.2.3].
print a, b, c  # Se debe  imprimir [1,2,3],[1.2.3],[1,2,3].
print a, b, c, d  # Se debe  imprimir [1,2,3],[1.2.3],[1,2,3],[1,2,3].

a += [4]  # Se establece que agregamos un elemento a nuestra variable "a".

print a  # Se debe imprimir [1,2,3,4], ya que estamos indicando
#          mediante este operando "+=" que se modifique la variable "a "y
#          por ende todas las demas en las que dependan de la variable
#          modificadase, tambien se modificaran.

print a, b  # Se debe imprimir [1,2,3,4] [1,2,3,4].
print a, b, c  # Se debe imprimir [1,2,3,4] [1,2,3,4] [1,2,3,4].
print a, b, c, d  # Se debe imprimir [1,2,3,4] [1,2,3,4] [1,2,3,4] [1,2,3,4].
print ""

# El metodo "extend()"" concatena dos listas haciendola una sola.
# Cabe mencionar que este metodo afecta el resultado si se hace referencia a
# el en 2 o mas variables al momento de concatenarlas como se explicara mas
# adelante.
# Para utilizar este metodo se hace del siguiente modo:
# nombre_de_la_lista.extend(["Elemento o lista que se desea agregar entre
# corchetes"]) y se agregara esta lista al final de esta lista y de todas las
# listas que hagan referencia a la variable en la que esta.

print "Concatenacion de listas metodo \"extend()\""

a = [1, 2, 3]
a.extend([4, 5, 6])  # Aqui establecemos que se agregara la lista [4,5,6] a la
#                    variable "a".

print a  # Se debe imprimir [1,2,3,4,5,6].
print ""

print "Metodo \"extend()\", modificando una concatenacion de listas"

a = [1, 2, 3, 4]
b = a  # Aqui establecemos que nuestra variable "b" es lo mismo que "a".
print a, b  # Se debe imprimir [1,2,3,4] [1,2,3,4].

a.extend([5, 6, 7])  # Aqui establecemos que en "a" se adicionara la lista
#                    [5,6,7], y como "b" es una variable que depende de "a"
#                    la cual se ha modificado, tambien se modificara "b" o las
#                    listas que dependan de "a".

print a, b  # Se debe imprimir [1,2,3,4,5,6,7] [1,2,3,4,5,6,7].
print ""

# El metodo "append()", agrega un elemento al final de la lista o una lista
# al final de otra lista. Es muy parecido al metodo "extend()", pero hay que
# recordar que el metodo "extend()" como su nombre lo indica "extiende" la
# lista osea de dos listas hace una sola, mientras que el metodo "append()"
# concatena la lista en una sola cuando se agrega un solo elemento, y cuando
# son mas elementos crea una lista dentro de otra.

print "Concatenacion de listas metodo \"append()\""

a = [1, 2, 3, 4, 5, 6]
a.append(7)  # Se establece que se agregara un elemento al final de la lista.

print a  # Se debe imprimir [1,2,3,4,5,6,7].
print ""

print "Metodo \"append()\", modificando una concatenacion de listas"

a = ["uno", 2, 3.0, False, "cinco"]
a.append([6, 7.0, True])  # Insertara la lista [6, 7.0, True] al final de la
#                           lista.

print a  # Se debe imprimir ['uno', 2, 3.0, False, 'cinco', [6, 7.0, True].
print ""

a = [1, 2, 3]
b = a  # Se establece que nuestra variable "b" es lo mismo que "a".
c = b  # Se establece que nuestra variable "c" es lo mismo que "b".

print a, b, c  # Se debe imprimir [1,2,3] [1,2,3] [1,2,3].

a.append([4, 5, 6])  # Establecemos que queremos agregar una lista con los
#                   elementos [4,5,6] al final de nuestra lista y recordemos
#                   que otras variables dependen de la variable que estamos
#                   modificando, tambien se modificaran.

print a, b, c  # Se imprimira [1,2,3,[4,5,6] [1,2,3,[4,5,6] [1,2,3,[4,5,6].
print ""

# Elementos en una posicion especifica.
# El metodo "insert()" agrega un elemento a una posicion en especifico en una
# lista. Donde el primer numero del parentesis indica el indice donde sera
# colocado el numero y separado de una coma indicara que elemento se desea
# ingresar, "insert(2, 3.0)". Cabe mencionar que este metodo afecta el
# resultado si se hace referencia a el en 2 o mas variables al momento de
# concatenarlas.

print "Agregar elementos en una posicion especifica \"insert()\""

a = ["uno", 2, False, "cinco"]
a.insert(2, 3.0)  # Insertara el numero 3.0 entre el 2 y el False.

print a  # Se debe imprimir ['uno', 2, 3.0, False, 'cinco'].
print ""

print """Agregando elementos a una posicion especifica y modificando las listas
que dependen de ella \"insert()\""""

a = ["uno", 2, False]
b = a  # Aqui establecemos que la variable "b" es lo mismo que "a".

print a, b  # Se debe imprimir ['uno', 2, False]  ['uno', 2, False].

a.insert(2, 3.0)  # Aqui establecemos que queremos insertar el elemento
#                  "3.0" en el indice 2 osea que sera el tercer elemento de
#                  nuestra lista, si quisieramos agegar mas elementos
#                  recordemos que tendrian que ser una lista y esta seria una
#                  lista que estaria dentro de otra pero en la posisicon que
#                  querramos asignarle.

print a, b  # Se debe imprimir ['uno', 2, 3.0, False]  ['uno', 2, 3.0, False].
print ""

# Remover y Eliminar Elementos de una lista.

# Para eliminar un elemento de una lista Python pone a nuestra disposicion el
# metodo "remove()", con este metodo solo podemos eliminar un elemento a la
# vez y debemos recordar que si el elemento que que deseamos eliminar esta en
# una variable de la cual dependen otras, estas tambien se modificaran.
# Lo utilizamos de la siguiente forma:
# "nombre_de_la_lista_o_variable.remove(elemento que se desea eliminar)".

print "Remover elementos de una lista, metodo \"remove()\""

a = [9, 269, 3, True, "Lista", 5, 6]

print a  # Se imprimira una lista para comparar los elementos que se desean
#          eliminar

a.remove(269)  # Aqui establecemos que deseamos eliminar el numero 269.
a.remove("Lista")  # Aqui establecemos que deseamos eliminar "Lista".
a.remove(True)   # Aqui establecemos que queremos eliminar True.

print a  # Se debe imprimir [ 9, 3, 5, 6].
print ""

# Eliminar elementos de una lista "del"

# "del" es una palabra reservada que permite eliminar uno o varios elementos
# (dentro de un ragi [1:3], [07], etc.) de una lista e incluso la misma lista.
# Debemos recordar que si el elemento o los elementos que que deseamos
# eliminar esta en una variable de la cual dependen otras, estas tambien se
# modificaran.

print "Eliminar un elementos especifico de una lista \"del\""

a = [1, 2, 3, 4, 5]

print a  # Imprimir la lista de referencia.

del a[2]  # Indicamos el numero de indice del elemento a eliminar.

print a  # Se debe imprimir [1,2,4,5]
print ""

print "Eliminar varios elementos de una lista \"del\""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print a  # Imprimir la lista de referencia.

del a[::2]  # Indicamos que se elimine un elemento si y uno no.

print a  # Se debe imprimir [2,4,6,8].
print ""

# Busqueda de elementos en una lista

# Para realizar la busqueda de un elemento especifico o dos en una lista
# Utlizaremos las funciones; "in" para buscar un solo elemento y "and"
# para buscar 2 elementos.
# Recordemos que para que "and" arroje un valor "True" los dos elementos a
# buscar deben existir en la lista, de lo contrario dara false.

print "Busqueda de elementos en una lista"

a = ["Nombre", "SegundoNombre", "ApellidoPaterno", "ApellidoMaterno", "Edad"]
b = "Nombre" in a
c = "Nombre" and "SegundoNombre" in a
d = "XXXXX" in a
e = "Edad" and 56.98 in a

print b  # Se debe imprimir True.
print c  # Se debe imprimie True.
print d  # Se debe imprimie False
print e  # Se debe imprimie False
print ""

# Fin del ejercicio.
