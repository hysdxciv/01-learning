#Gerador de Sequência Fibonacci:
print('------ Fibonacci ------\n')

numero_01 = int(input('Insira um número inteiro: '))
lista_fibo = [0]
n1 = 1
n2 = 0
n3 = 0

while n1 <= numero_01:
    lista_fibo.append(n1)
    n3 = n1 + n2
    n2 = n1
    n1 = n3
print(f'A sequência de Fibonacci com o teto de "{numero_01}" é: {lista_fibo}')