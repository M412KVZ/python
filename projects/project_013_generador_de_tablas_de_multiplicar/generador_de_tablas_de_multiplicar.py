#! python3
# -*- coding: utf-8 -*-
# author: Antonio Alfonso Martínez
# modificacion y mejora: glow 
# date: wed/07/jun/2023
# links: https://programacionpython80889555.wordpress.com/2018/04/22/generando-tablas-de-multiplicar-en-python-ejercicio-basico/
# description: generador de tablas de multiplicar con cualquir numero entero
# v1.1.0 creación del archivo

# ----- Inicio -----
numero = int(input("Introduce un numero entero: "))

for i in range(0,11):
    resultado = i * numero
    print(("%d x %d = %d") % (numero, i, resultado))


# ----- Fin -----