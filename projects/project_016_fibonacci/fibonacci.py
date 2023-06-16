#! python3
# -*- coding: utf-8 -*-
# author: Guido van Rossum 
# links: http://tutorial.python.org.ar
# modificacion y mejora: glow 
# date: fri/16/jun/2023/1500
# description: sucesión de fibonacci
# v1.1.0 creación del archivo y codigo de inicio

# pendiente mejorar codigo, elección de un numero 

# ----- Inicio -----
a, b = 0, 1
while b < 1000:
#    print(b)  # vertical
    print(b, end=", ")  # horizontal
    a,b = b, a+b

# ----- Fin -----