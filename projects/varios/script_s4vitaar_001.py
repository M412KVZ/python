#!/usr/bin/python3

import request, signal, json, pdb, string

def_handler(sig, frame):
	print("\n\n[!] Saliendo...\n")
	sys.exit(1)

# Ctrl+c
# al hacer crtl+c salir del programa
signal.signal(signal.SIGINT, def_handler)

# Variables Globales
# string.ascii_letter -->  contempla letras minusculas y minusculas
# string.digits       -->  contempla digitos
# string.punctuation  -->  comtempla simbolos o carcateres especiales
# string.printable    -->  contempla todos los anteriones
# si los caracteres especiales dan comflicto:
# 		importar la libreria re "import re"
#		re.escape(string.punctuation)
characters = string.ascii_letters + string.digits

def getUsers():



	post_data = '{"username":{"$regex":"^ad"},"password":{"$ne":"pepe"}}'

if __name__ == '__main__':

	getusers()

https://www.twitch.tv/videos/1734034179
TIME 01:57:15
