
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2 , 3, 4]

def soma_lista(lista1, lista2):
    max_rang = min(len(lista1), len(lista2))
    resultado = []
    for i in range(max_rang):
        soma = (float(lista1[i]) + float(lista2[i]))
        resultado.append(soma)
    return resultado


print(soma_lista(l1, l2))