texto = "constelation"
print(''.join([f"{letra:>4}" for letra in texto]))
valores = [ord(letra) for letra in texto]
print(''.join([f"{valor:4}" for valor in valores]))
print(' '.join([f"{sum(valores[0:i + 1])}" for i in range(len(valores))]))
