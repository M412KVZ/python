#! python3
# -*- coding: utf-8 -*-
# author:
# links:
# modificacion y mejora: glow
# date: wed/14/jun/2023
# description: generador de contraseñas
# v1.1.0 creación del archivo y codigo de inicio

# ----- Inicio -----

# importacion de modulos

import time  # impotar el modulo time
import random  # importar el modulo random para el manejo de caracteres al azar

print("\nWelcome to PassGen")

# definiendo la funcion menu
def menu():
    print("\033[;32m" + "\n[1] " + "\033[0;m" "Generate Password")
    print("\033[;32m" + "[2] " + "\033[0;m" "Exit")
    global option
    option = int(input("\033[;34m" + "\nPlease choose an option: " + " \033[0;m"))
    if (option == 1):
        passgen()  # llamando a la función passgen
    elif (option == 2):  # salir
        print("\033[;36m" + "\nExiting..." + " \033[0;m")
        time.sleep(1)  # tiempo de espera antes de salir
        exit
    else:  #
        print("\033[;31m" + "\nWrong option, please try again" + "\033[;0m")
        menu()  # llamando a la función menu

# definiendo la funcion passgen

def passgen():

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;.:!¡¿?'\^#$%&(){}[]+-_*/~"
    password = ""
    length = int(input("\n[*] Input Password Length: "))
    while len(password) != length:
        password = password + random.choice(chars)
        if len(password) == length:
            print("\nPassword: %s" % password)
    question()

def question():  # definiendo la función question
    print("\033[;34m" + "\nDo you want to generate other password?\n" + "\033[0;m")
    print("\033[;35m" + "[1] " + "\033[0;m" + "Yes")
    print("\033[;35m" + "[2] " + "\033[0;m" + "No, Exit")
    global option_1
    option_1 = int(input("\033[;34m" + "\nPlease choose an option: " + "\033[0;m"))
    if (option_1 == 1):
        passgen()
    elif (option_1 == 2):
        print("\033[;36m" + "\nExiting..." + " \033[0;m\n")
        time.sleep(1)
        exit
    else:
        print("\033[;31m" + "\nWrong option, please try again" + "\033[;0m")
        question()

menu()  # llamando a la funcion menu

# ----- Fin -----