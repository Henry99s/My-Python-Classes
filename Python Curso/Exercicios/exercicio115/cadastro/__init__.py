from tabulate import tabulate

# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'


def cadastrar():
    while True:
        try:
            nome = str(input('Digite o nome: ')).strip().capitalize()
            idade = int(input('Digite a idade: '))

            return {'Nome': nome, 'Idade': idade}

        except (ValueError, TypeError):
            print(f'{vermelho}ERRO! Digite corretamente as informações.{FIM_COR}')


lista_cadastros = list()


def listar():
    while True:
        print(f'Digite as informações do {azul}próximo{FIM_COR} cadastrante.')
        lista_cadastros.append(cadastrar())

        try:
            continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
            while continuar != 'S' and continuar != 'N':
                continuar = str(input(f'{vermelho}Tente Novamente!{FIM_COR} Quer continuar? '
                                      f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
            if continuar == 'N':
                break

        except (ValueError, TypeError):
            print(f'{vermelho}ERRO! Tente novamente.{FIM_COR}')
    return lista_cadastros


def mostrar_pessoas_cadastradas():
    if not lista_cadastros:
        print(f'{vermelho}Nenhuma pessoa cadastrada.{FIM_COR}')
        return

    dados_formatados = []

    for pessoa in lista_cadastros:
        dados_formatados.append([pessoa['Nome'], pessoa['Idade']])

    cabecalho = ["Nome", "Idade"]

    print(tabulate(dados_formatados, headers=cabecalho, tablefmt="fancy_grid"))
