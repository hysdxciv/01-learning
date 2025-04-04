frase = 'O Python é uma linguagem de programação'\
    'multiparadigma'\
    'Python foi criado por Guido Van Rossum'

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    repeticao_letra = frase.count(letra_atual)

    if apareceu_mais_vezes < repeticao_letra:
        apareceu_mais_vezes = repeticao_letra
        letra_que_apareceu_mais_vezes = letra_atual
        
    i += 1
    
    
print('A letra que mais apareceu foi o '
    f'"{letra_que_apareceu_mais_vezes}", que apareceu {apareceu_mais_vezes}x.'
)
