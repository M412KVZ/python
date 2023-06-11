#! python3
# -*- coding: utf-8 -*-
# author: MasterHeheGar
# links: https://www.youtube.com/watch?v=_fiY9P-lPEc
# modificacion y mejora: glow 
# date: wsun/11/jun/2023
# description: conversor de divisas
# v1.1.0 creación del archivo

# ----- Inicio -----

def menu():
    print("[1] Dólar")
    print("[2] Dólar Canadiense")
    print("[3] Euro")
    print("[4] Libra Esterlina")
    print("[5] Centenario")
    print("Que tipom de cambio deseas realizar")
    global cambio
    cambio = input()
    cambio = input (cambio)

# llamando a la funcion menu
menu()