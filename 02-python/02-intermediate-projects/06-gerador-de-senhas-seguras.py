# gerador de senhas Seguras!

def criar_gerador_senha(nivel_seguranca):
    def gerar_senha(tamanho):
        import random
        import string

        if nivel_seguranca == 'fraca':
            caracteres = string.digits
        elif nivel_seguranca == 'media':
            caracteres = string.ascii_letters + string.digits
        else:
            caracteres = string.ascii_letters + string.digits + '!@#$%&*'
        return ''.join(random.choice(caracteres) for _ in range(tamanho))
    return gerar_senha

senha_fraca = criar_gerador_senha('fraca')
senha_media = criar_gerador_senha('media')
senha_forte = criar_gerador_senha('forte')

print(senha_fraca(6))
print(senha_media(6))
print(senha_forte(8))

