#! python3
# -*- coding: utf-8 -*-
# author: MasterHeheGar
# links: https://www.youtube.com/watch?v=_fiY9P-lPEc
# modificacion y mejora: glow 
# date: sun/11/jun/2023
# description: conversor de divisas
# v1.1.0 creación del archivo

# ----- Inicio -----

def menu():
    print("Cuánto tienes en pesos mexicanos")
    global pesos
    pesos = input()
    pesos = float(pesos)
    print("Que tipo de cambio deseas realizar")
    print("[1] Dólar")
    print("[2] Dólar Canadiense")
    print("[3] Euro")
    print("[4] Libra Esterlina")
    print("[5] Centenario")
    
    global cambio
    cambio = input()
    cambio = int(cambio)
    # evaluando tipo de cambio
    if (cambio == 1):
        # llamando a la funcion Dolares
        Dolares()
    elif (cambio == 2):
        # llamando a la funcion DolaresCan
        DolaresCan()
    elif (cambio == 3):
        # llamando a la funcion Euro
        Euros()
    elif (cambio == 4):
        # llamando a la funcion Libras
        Libras()
    elif (cambio == 5):
        # llamando a la funcion Centenario
        Centenario()
    else:
        print("\nLa opcionque elegiste no es correcta")
    print("\n¿Deseas hacer otro tipo de cambio? Si/No\n")
    global resp
    resp = input()
    resp = resp.lower()
    otravez()

# definiendo la funcion Dólares
def Dolares():
    print("\n¿Cuál es el precio del Dólar el dia de hoy?")
    global precioD
    precioD = input()
    precioD = float(precioD) 
    global dinerito
    dinerito = pesos/precioD
    print("\nTienes:", dinerito, "Dólares")

# definiendo la funcion DolaresCan
def DolaresCan():
    print("\n¿Cuál es el precio del Dólar Canadiense el dia de hoy?")
    global precioDC
    precioDC = input()
    precioDC = float(precioDC) 
    global dinerito
    dinerito = pesos/precioDC
    print("\nTienes:", dinerito, "Dólares Canadienses")

# definiendo la funcion Euros
def Euros():
    print("\n¿Cuál es el precio del Euro el dia de hoy?")
    global precioEU
    precioEU = input()
    precioEU = float(precioEU) 
    global dinerito
    dinerito = pesos/precioEU
    print("\nTienes:", dinerito, "Euros")

# definiendo la funcion Libras
def Libras():
    print("\n¿Cuál es el precio de la Libra el dia de hoy?")
    global precioL
    precioL = input()
    precioL = float(precioL) 
    global dinerito
    dinerito = pesos/precioL
    print("\nTienes:", dinerito, "Libras")

# definiendo la funcion Centenario
def Centenario():
    print("\n¿Cuál es el precio del Centenario el dia de hoy?")
    global precioC
    precioC = input()
    precioC = float(precioC) 
    global dinerito
    dinerito = pesos/precioC
    print("\nTienes:", dinerito, "Centenarios")

# definiendo la funcion otravez
def otravez():
        while (resp != "no"):
            menu()

# llamando a la funcion menu
menu()

# ----- Fin -----