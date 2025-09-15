# sistema de desconto progressivo

def criar_calculadora_desconto_progressivo():
    total_compras = 0
    def calcular_desconto(valor_compra):
        nonlocal total_compras
        total_compras += valor_compra
        if total_compras > 1000:
            desconto = 0.15
        elif total_compras > 500:
            desconto = 0.10
        elif total_compras > 200:
            desconto = 0.05
        else:
            desconto = 0
        valor_final = valor_compra * (1 - desconto)
        return f'Desconto: {desconto*100:.2f}% - Total: R$ {valor_final:.2f}'
    return calcular_desconto

cliente = criar_calculadora_desconto_progressivo()

print(cliente(800))

