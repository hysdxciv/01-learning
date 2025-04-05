#DADOS DE ENTRADA
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
#DADOS MANIPULADOS
quantidade_letras = len(nome)
nome_invertido = nome[::-1]
primeira_letra = nome[0:1:]
ultima_letra = nome[quantidade_letras-1:quantidade_letras:]

if nome and idade:
    print(f'Seu nome é "{nome}"')
    print(f'Seu nome invertido é "{nome[::-1]}"')
    if " " in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem "{quantidade_letras}" letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A ultima letra do seu nome é {ultima_letra}')
else:
    print('Desculpe, você deixou campos vazios')