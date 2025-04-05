#Contagem de Vogais

print('\n------ Contagem de Vogais -----\n')

palavraX = input('Digite uma palavra: ').lower()
contador_vogal = 0
vogais = 'aeiou'

for vogal in palavraX:
    if vogal in vogais:
        contador_vogal += 1
print(f'\nA palavra "{palavraX}" tem "{contador_vogal}" vogais!')
