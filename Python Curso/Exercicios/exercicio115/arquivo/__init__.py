from exercicio115 import interface

# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
FIM_COR = '\033[m'


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'{vermelho}Houve um ERRO na criação do arquivo!{FIM_COR}')
    else:
        print(f'Arquivo {azul}{nome}{FIM_COR} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{vermelho}Erro ao ler o arquivo!{FIM_COR}')
    else:
        interface.cabecalho('CONTEUDO DO ARQUIVO')
        print(a.read())
