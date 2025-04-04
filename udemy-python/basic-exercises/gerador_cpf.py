import random



nove_digitos = ''

contador_regressivo_01 = 10
contador_regressivo_02 = 11
somatorio_01 = 0
somatorio_02 = 0
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

for digito in nove_digitos:

    somatorio_01 += int(digito) * contador_regressivo_01

    contador_regressivo_01 -= 1

digito_01 = (somatorio_01 * 10) % 11
digito_01 = digito_01 if digito_01 <= 9 else 0
# print(digito_01)

dez_digitos = nove_digitos + str(digito_01)

for digito in dez_digitos:
    somatorio_02 += int(digito) * contador_regressivo_02
    contador_regressivo_02 -= 1

digito_02 = (somatorio_02 * 10) % 11
digito_02 = digito_02 if digito_02 <= 9 else 0

cpf_calculado = f'{nove_digitos}{digito_01}{digito_02}'

print(cpf_calculado)


