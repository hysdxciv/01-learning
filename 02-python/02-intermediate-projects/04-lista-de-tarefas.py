"""Lista de Tarefas com comandos de lista, desfazer e refazer"""

import os
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

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos disponivéis: listar, desfazer e refazer')
    tarefa = input('Digite um comando ou uma tarefa: ').lower()

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas,tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'cls':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue








