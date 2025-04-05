#Menu Interativo:
#Dados
saldo = 45.55


while True:

    print('------ BEM VINDO!! ------')
    print('1 - Ver Saldo')
    print('2 - Sacar')
    print('3 - Depósitar')
    print('4 - Sair')

    menu = input('O que desja? ')
    
    if menu == '1':
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
    elif menu == '2':
        valor_saque = float(input('Quanto gostaria de sacar? '))
        if valor_saque > saldo:
            print('Saldo insulficiente!')
        else:
            saldo -= valor_saque
            print('Saque realizado com sucesso!')
            print(f'Seu saldo atual é de: R$ {saldo:.2f}')
    elif menu == '3':
        deposito = float(input('Quanto gostaria de depósitar? '))
        saldo += deposito
        print(f'Seu saldo atual é de: R$ {saldo:.2f}')

    elif menu == '4':
        print('Saindo...')
        break
    else:
        print('Escolha apenas uma opção do MENU!')