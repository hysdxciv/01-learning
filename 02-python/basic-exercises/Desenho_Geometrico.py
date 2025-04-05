#Desenho de Padrões:
#Dados de Entrada
print('\n----- Vamos Desenhar?-----')
print('Das opções abaixo, qual você quer que eu desenhe?')
print('1 - Quadrado')
print('2 - Triângulo')
forma = input('\n--- Qual forma geometrica você gostaria de desenhar? ---\n')
caracter = input('Qual carácter você quer usar (* ou .)? ')
#Validação do caracter!
if caracter not in ['.', '*']:
    print('\n------Caracter INVÁLIDO! "*" Definido como padrão------\n')
    caracter = '*'
#Dados do Triângulo
altura_triangulo = 3
largura_triangulo = 3
#Dados do Quadrado
altura_quadrado = 3
largura_quadrado = 3

if forma == '1':
    print('\nAqui está seu quadrado: \n')
    for linha in range(altura_quadrado):
        print(caracter * altura_quadrado)
elif forma == '2':
    print('\nAqui está seu triângulo: \n')
    for linha in range(1, largura_triangulo + 1):
        print(caracter * linha)
