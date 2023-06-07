mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

mensaje += " Carrera"
print(mensaje)

mensaje_1 = "Hola"
mensaje_2 = " "
mensaje_3 = "Carrera"
mensaje_4 = "Ernesto"
print(mensaje_1 + mensaje_2 + mensaje_4 + mensaje_2 + mensaje_3)

numero_1 = 2
numero_2 = 4
resultado = numero_1 + numero_2
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda:")
mensaje1 = "Hola Ernesto"
buscar_subcadena = mensaje1.find("Ernesto")
print(buscar_subcadena)

mensaJE = "Hola Ernesto"
extraer_subcadena = mensaJE[5:12]
print(extraer_subcadena)

print("Comparacion:")
mensaJE = "Hola"
mensAJE = "Hola"
var = mensaJE == mensAJE
print(mensaJE == mensAJE)

print("Comparacion:")
mensaJE: str = "Hola"
mensAJE = "Hoa"
var1: bool = mensaJE == mensAJE
print(mensaJE == mensAJE)
