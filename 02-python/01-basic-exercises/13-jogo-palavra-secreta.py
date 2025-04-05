#Jogo da Palavra Secreta

import os


palavra_secreta = 'perfume'
numeros = '0123456789'
letras_acertadas = ''
quantidade_tentativas = 0


while True:

    quantidade_tentativas += 1
    letra_digitada = input('Digite uma letra: ').lower()
    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra!')
        continue

    elif letra_digitada in numeros:
        print('Digite apenas LETRAS!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
    
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!')
        print(f'A palavra secreta era "{palavra_secreta}"')
        print(f'Você acertou com "{quantidade_tentativas}" tentativas!')
