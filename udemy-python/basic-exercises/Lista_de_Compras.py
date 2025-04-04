print('\n------ Lista de Compras -----\n')


lista = []

for i in range(5):
    comprar = input('O que deseja adicionar na sua lista de compras? \n')
    lista.append(comprar)

print('\nAqui está a sua lista de compras: \n')
for item in lista:
    print(f'- {item}')

