#Lista de Compras:
import os

lista_compras = []

while True:
    print('\nSelecione a opção desejada:')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if opcao == 'i':
        os.system('cls')
        item = input('Insira um item: ')
        os.system('cls')
        lista_compras.append(item)
    elif opcao == 'a':
        os.system('cls')
        apagar = input('O que você gostaria de apagar da lista? ').lower()
        if apagar in lista_compras:
            lista_compras.remove(apagar)
            os.system('cls')
        else:
            print('Este item não existe! Por favor informar apenas os itens presentes na lista!')
    elif opcao == 'l':
        os.system('cls')

        if lista_compras == []:
            print('Lista de compras vazia!')
        else:
            for indice, item_lista in enumerate(lista_compras):
                print(f'{indice} - {item_lista}')
    elif opcao == 's':
        os.system('cls')
        break
    else:
        print('Opção inválida! Escolha entre [i]-inserir; [a]-pagar [l]-listar ou [s] para sair!')')