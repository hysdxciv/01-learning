"""Lista de Tarefas com comandos de lista, desfazer e refazer"""
import json
import os

ARQUIVO_TAREFAS = 'tarefas.json'

# Definição das Funções do Programa:
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar!')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer!')
        return
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista!')
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer!')
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa} adicionada na lista!')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa adicionada!')
        return
    print(f'{tarefa} adicionada a sua lista!')
    tarefas.append(tarefa)
    print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe!')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'lista_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos disponivéis: listar, desfazer e refazer')
    tarefa = input('Digite um comando ou uma tarefa: ').lower()

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'cls': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']

    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)