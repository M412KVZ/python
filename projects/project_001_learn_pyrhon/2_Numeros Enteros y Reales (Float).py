# Archivo: 2 Numeros Enteros y Reales (Float).py
# Autor: **********.
# Fecha: 20 de Abril del 2020
# Editor de Codigo: Visual Studio Code v1.47.2
# Descripcion: Ejercicio 001. Video 2 del curso aprender a programar
#              en Python. 
#              Descripcion de Numeros Enteros y Reales (float).

# Introdicion

# Numeros enteros 
# En Python existen 2 formas de representar los numeros enteros

# De tipo int en plataformas de 32 bits (x32) va de -2.147.483.648 hasta 2.147.483.647, 
# y en plataformas de 64 bits (x64) va de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807
# Y de tipo long, este tipo permite almacenar numeros mas grandes y esta limitado solo 
# por la memoria del sistema.

# Numeros Reales. O del tipo float son los que tienen punto decimal ejemplo: 
# 1.4, 1.5, 1.6, 1.7, 2.5, 2.9, 15.98, 1256.9874, etc., como variable real = 0.657 
# (esta es una variable de tipo float)
# Si se escribe una coma "," como separador entre la parte entera y la decimal, (3,5) Python no lo entiende
# como separador, sino como una pareja de números (concretamente, lo entiende como una tupla de dos elementos.

# Ejercicio: 001.
# Numero entero

print(1)
print(2)
 # Etc.

# Ejercicio: 002.
# Numero Real o del tipo loat

real = 0.658
print (real)

# Ejercicio: 002.
# Operaciones basicas
 # Definimos nuestras variables

a = 26
b = 11.3

# SUMA
Suma = a + b
print(Suma)
# El resultado debe ser 37.3

# RESTA
c = 5
# a=26  ya que "a" ya estaba definina anteriormente en el apartado de suma

Resta = c - a
print(Resta)
# El resultado debe ser -21

# Multiplicacion (se representa con un asterisco)

d = 3.5
# c=5  ya que "c" ya estaba definina anteriormente en el apartado de resta

Multiplicacion = d * c
print(Multiplicacion)
# El resultado debe ser 17.5

# Exponente (son 2 asteriscos juntos seguidos del numero al cual lo queremos elevar)
Exponente = c ** 2
print(Exponente)
# El resultado debe ser 25

# Division
# a=26  ya que "a" ya estaba definina anteriormente en el apartado de suma
# c=5  ya que "c" ya estaba definina anteriormente en el apartado de resta

Division = c / a
print(Division)
# El resultado debe ser 0.19230769230769232

# Dividir "0/5" o entre cualquier otro numero siempre dara "0", pero con 
# decimales "0.0"

numero1 = 0
numero2 = 7
Division1 = numero1 / numero2
print(Division1)

# Dividir por cero genera un error. Ejemplo "5/0" ZeroDivisionError: division by zero

# Al realizar operaciones con decimales, los resultados pueden presentar errores de redondeo

numero3 = 100
numero4 = 3
Division2 = numero3 /  numero4
print(Division2)
# El rsultado sera 33.333333333333336
# Este error se debe a que Python almacena los números decimales en binario y pasar de decimal
# a binario provoca errores de redondeo. Es un error que sufren casi todos los lenguajes de 
# programación. Si necesitamos precisión absoluta, debemos utilizar bibliotecas específicas.
# Debido a los errores de redondeo, dos operaciones que debieran dar el mismo resultado pueden 
# dar resultados diferentes

# Fin del ejercicio.