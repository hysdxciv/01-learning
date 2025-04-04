#Tabuada
print('\n----- Tabuada -----\n')
numero = int(input('Digite um número: '))

for n in range(1, 11):
    resultado = n * numero
    print(f'{numero} x {n} = {resultado}')
