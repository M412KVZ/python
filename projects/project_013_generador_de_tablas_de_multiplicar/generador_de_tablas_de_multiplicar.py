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
# v1.1.3 bucle para elección de una nueva tabla o salir

# ----- Inicio -----

import time  # v1.1.1 se agrega el modulo time para gestion de tiempos


print("\033[;32m" + "\nBienvenido al Generador de Tablas de Multiplicar" + "\033[0;m")  # v1.1.1 se agrego un titulo, v1.1.2

def menu():  # definiendo la función menu
    print("\033[;34m" + "\n¿Que desea Hacer?" + "\033[0;m") 
    print("\033[;32m" + "\n[1] " + "\033[0;m" "Generar Tabla")
    print("\033[;32m" + "[2] " + "\033[0;m" "Salir")
    global hacer 
    hacer = int(input("\033[;34m" + "\nPor favor elija una opción: " + " \033[0;m"))
    if (hacer == 1):
        tabla()  # llamando a la función tabla
    elif (hacer == 2):  # salir
        print("\033[;36m" + "\nSaliendo..." + " \033[0;m")
        time.sleep(1)  # tiempomde espera antes de salir
        exit
    else:  # 
        print("\033[;31m" + "\nLa opcionque elegiste no es correcta" + "\033[;0m")  # v1.1.2, v1.1.3
        menu()  # llamando a la función menu

# Definiendo la Función Tabla
def tabla():
    numero = int(input("\033[;33m" + "\nIntroduce un numero entero:" + " \033[0;m"))  # introducir cualquier numero para generar la tabla, v1.1.2

    numero_inicio = int(input("\033[;33m" + "\nIntroduce el numero de inicio de la Tabla: " + " \033[0;m"))  # v1.1.1 introducir cualquier numero entero desde el que se quiere iniciar la tabla

    numero_final = int(input("\033[;33m" + "\nIntroduce el numero final de la Tabla: " + " \033[0;m"))  # v1.1.1 introducir cualquier numero entero hasta el que se quiere generar la tabla

    print("\033[;36m" + "\nGenerando Tabla..." + "\033[0;m\n")  # v1.1.1 titulo, v1.1.2

    time.sleep(2)  # v1.1.1 tempo de retraso 2 segundos

    for i in range(numero_inicio,numero_final+1):  # codigo para la generacion de la tabla v1.1.1 cambio de nombre de las variables
        time.sleep(.2)  # v1.1.1 tiempo de retraso entre la generacion de un resultado y otro
        resultado = i * numero  # generación del cálculo
        print(("%d x %d = %d") % (numero, i, resultado))  # impresión del resultado 

    print("\033[;35m" + "\nTabla Generada..." + "\033[0;m")  # v1.1.1 mensaje de termino y salida del programa, v1.1.2
    time.sleep(1)  # tiempo de espera antes de salir
    pregunta()  # llamando a la función pregunta v1.1.3

def pregunta():  # definiendo la función pregunta v1.1.3
    print("\033[;34m" + "\n¿Desea generar otra Tabla?\n" + "\033[0;m")
    print("\033[;35m" + "[1] " + "\033[0;m" + "Si")
    print("\033[;35m" + "[2] " + "\033[0;m" +  "No, Salir")
    global pregunta1
    pregunta1 = int(input("\033[;34m" + "\nPor favor elija una opción: " + "\033[0;m"))
    if (pregunta1 == 1):
        tabla()  # llmanado a la función tabla
    elif (pregunta1 == 2):
        print("\033[;36m" + "\nSaliendo..." + " \033[0;m")
        time.sleep(1)  # tiempo de espera antes de salir del programa
        exit
    else:
        print("\033[;31m" + "\nLa opcionque elegiste no es correcta" + "\033[;0m")  # v1.1.2, v1.1.3
        pregunta()

# Llamando a la funcion menu 
menu()
# ----- Fin -----