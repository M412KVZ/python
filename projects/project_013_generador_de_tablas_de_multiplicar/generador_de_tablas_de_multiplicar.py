#! python3
# -*- coding: utf-8 -*-
# author: Antonio Alfonso Martínez
# links: https://programacionpython80889555.wordpress.com/2018/04/22/generando-tablas-de-multiplicar-en-python-ejercicio-basico/|
# modificacion y mejora: glow 
# date: wed/07/jun/2023
# description: generador de tablas de multiplicar con cualquir numero entero
# v1.1.0 creación del archivo
# v1.1.1 agregado manejo de timepos, títulos y elección de numeros de inicio y final de la tabla 
# v1.1.2 agregar color al texto

# pendiente
#   bucle para elección de una nueva tabla o salir

# ----- Inicio -----

import time  # v1.1.1 se agrega el modulo time para gestion de tiempos

# Definiendo la función menu
def menu():
    print("\033[;32m" + "\nBienvenido al Generador de Tablas de Multiplicar" + "\033[0;m")  # v1.1.1 se agrego un titulo, v1.1.2
    print("\n¿Que desea Hacer?")
    print("\n[1] Generar Tabla")
    print("[2] Salir")
    global hacer
    hacer = input()
    hacer = int(hacer)
    if (hacer == 1):
        tabla()
    elif (hacer == 2):
        print("Saliendo...")
        time.sleep(1)
        exit
    else:
        print("\nLa opcionque elegiste no es correcta")
        menu()

# Definiendo la Función Tabla
def tabla():
    numero = int(input("\033[;33m" + "\nIntroduce un numero entero:" + " \033[0;m"))  # introducir cualquier numero para generar la tabla, v1.1.2

    numero_inicio = int(input("\nIntroduce el numero de inicio de la Tabla: "))  # v1.1.1 introducir cualquier numero entero desde el que se quiere iniciar la tabla

    numero_final = int(input("\nIntroduce el numero final de la Tabla: "))  # v1.1.1 introducir cualquier numero entero hasta el que se quiere generar la tabla

    print("\033[;36m" + "\nGenerando Tabla..." + "\033[0;m\n")  # v1.1.1 titulo, v1.1.2

    time.sleep(2)  # v1.1.1 tempo de retraso 2 segundos

    for i in range(numero_inicio,numero_final+1):  # codigo para la generacion de la tabla v1.1.1 cambio de nombre de las variables
        time.sleep(.2)  # v1.1.1 tiempo de retraso entre la generacion de un resultado y otro
        resultado = i * numero  # generación del cálculo
        print(("%d x %d = %d") % (numero, i, resultado))  # impresión del resultado 

    print("\033[;35m" + "\nTabla Generada..." + "\033[0;m\n")  # v1.1.1 mensaje de termino y salida del programa, v1.1.2
    pregunta_1()

def pregunta_1():
    print("¿Desea generar otra Tabla?\n")
    print("[1] Si")
    print("[2] No, Salir")
    global pregunta_3
    pregunta_3 = input()
    pregunta_3 = int(pregunta_3)
    if (pregunta_3 == 1):
        tabla()
    elif (pregunta_3 == 2):
        print("Saliendo...")
        time.sleep(2)
        exit
    else:
        print("\nLa opcionque elegiste no es correcta")
        pregunta_1()

# Llamando a la funcion menu 
menu()
# ----- Fin -----