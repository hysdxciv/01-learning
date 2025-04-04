#Soma de números pares:

numero = int(input('Informe um número: '))
soma = 0

for n in range(0, numero + 1, 2):
    soma += n
print(soma)