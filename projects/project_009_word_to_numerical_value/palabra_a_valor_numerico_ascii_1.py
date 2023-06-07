[print('', x, end='\t') for x in "123456789+-¡?=)(/&%$#[]{}^"]; print()

suma = 0
for x in '123456789+-¡?=)(/&%$#[]{}^':
    suma = suma + ord(x)
    print(suma, end='\t')
