def valor_de_compra():
	compra = input("Compra:$ ")
	if compra <= 100:
		print("La compra es menor a $100, por favor pague en efectivo")
	elif compra > 100 and compra < 1000:
		print("""La compra es mayor a $100, Debe pagar con Tarjeta de Debito o Credito""")
	else:
		print("La compra es mayor a $1000, Por favor pague con tarjeta de credito")

valor_de_compra()