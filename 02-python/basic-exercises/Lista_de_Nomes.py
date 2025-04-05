#Dados:
lista = ['Maria', 'Helena', 'Luiz'] #Lista existente no sistema;
i = 0 #Indice referente a posição de cada nome, começa no 0 = Maria;


while True: #Enquanto o while for verdadeiro, ele vai ficar rodando meu código
    i = 0
    for nome in lista:   #para cada 'nome' na lista
        print(f'{i} - {nome}')    #De saída temos o indice (posição) e o nome da lista
        i += 1    #Aqui eu vou sempre somar mais um na lista, ou seja, 0, 1, 2....
    opcao = input('Deseja acrescentar, deletar nomes ou sair? [A]crescentar [D]deletar [S]air: ').lower() #Opções
    if opcao in ['a', 's', 'd']: #Validando entradas
        if opcao == 'a':    #Se o usuário escolher adicinar nome na lista
            novo_nome = input('Digite um novo nome: ')
            lista.append(novo_nome)
        
        elif opcao == 'd':    #Se o usuário quiser deletar um nome da lista
            deletar_nome = input('Digite um nome para deletar: ')
            if deletar_nome in lista:
                lista.remove(deletar_nome)
                print(f'A lista atual é essa: {lista}')
            else:    #Validando para saber se o usuário digitou um nome da lista!
                print(f'Nome "{deletar_nome}" não faz parte da lista!')
        elif opcao == 's':    #Se o usuário desejar sair, o programa se encerra
            print('Saindo.....')
            break
    else:
        print('Opção inválida! Digite apenas "A", "D" ou "S".')

