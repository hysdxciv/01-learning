#Dados
nome = 'Hygor'
altura = 1.74
peso = 90.00
imc = peso/(altura*altura)
#Utilizando formatação = f-strings...
...
linha_01 = f'{nome} tem {altura:.2f} de altura'
linha_02 = f'E pesa {peso:.2f} quilos e seu IMC é'
linha_03 = f'{imc:.2f}'
texto_completo = 'Meu nome é {n}m e tenho {h} de altura! Atualmente eu peso {kg:.2f}kg e meu IMC é de {i:.2f}'
formato = texto_completo.format(n=nome, h=altura, kg=peso, i=imc)
print(formato)

