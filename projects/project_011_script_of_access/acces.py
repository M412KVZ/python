def acceso(intento=1):
	name = input("Access Name: ") # en Python 3.x input() hace lo mismo que raw_input() en Python 2.x
	if name != "miriam":
		if intento < 3:
			print("\nDenied")
			intento += 1
			acceso(intento) # Llamada recursiva
		else:
			print("To many attempt, session closed")
	else:
		print("Access garanted")

acceso()