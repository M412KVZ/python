# -*- coding: utf-8 -*-
# Archivo: Find.py
# Autor: ----------.
# Fecha: 13 de Diciembre del 2017.
# Editor de Codigo: Sublime Text 3 Built 3143.
# Descripcion: Ejemplos de Programas en Python.
# Ejercicio: 010.

import os, sys  # Importamos estos modulos que vienen por defecto al instalar
#  Python.

buscar = ".pdf"  # Entre las comillas va el nombre del archivo que se desea
#  buscar.
directorio = os.getcwd()  #  El método getcwd() devuelve el directorio de
#  trabajo actual de un proceso.
total = 0  # Numero total de archivos que se han encontrado.

if(len(sys.argv) > 1):  # sys.argv es una lista en Python, que contiene los
#  argumentos de línea de comandos pasados al script. Con la función len
#  (sys.argv) puede contar el número de argumentos. Si vas a trabajar con
#  argumentos de línea de comandos, probablemente quieras usar sys.argv.
#  Parausar sys.argv, primero deberá importar el módulo sys.
    if(not os.path.isdir(sys.argv[1])):
        print(sys.argv[1], "no se reconoce como directorio")
        sys.exit(1)
    directorio = sys.argv[1]

for root, dir, ficheros in os.walk(directorio):
    for fichero in ficheros:
        if(buscar in fichero.lower()):
            print(root+"\\"+fichero)
            total += 1

print("En total hay", total, "archivos con", buscar)