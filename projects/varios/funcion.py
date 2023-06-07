def mi_funcion():
	num = input("Numero: ")
	if num < 10:
		print("El numero ingresado es menor a 10")
	elif num > 10 and num < 200:
		print("El numero ingresado es mayor a 10, pero menor que 200")
	else:
		print("El numero ingresado es mayor que 200")
	
mi_funcion()