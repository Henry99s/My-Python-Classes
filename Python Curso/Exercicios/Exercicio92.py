from datetime import date

# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Cadastro de Trabalhador em Python____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_trabalhador = list()


def trabalhador():
    nome = str(input('Nome: ')).strip().capitalize()
    ano_nascimento = int(input('Ano de Nascimento: '))
    idade = date.today().year - ano_nascimento
    ctps = int(input(f'Carteira de Trabalho {vermelho}(0 não tem){FIM_COR}: '))
    if ctps != 0:
        contratacao = int(input('Ano de contratação:  '))
        salario = int(input(f'Salario: {verde}R${FIM_COR}'))
        idade_contratacao = contratacao - ano_nascimento
        aposentadoria = idade_contratacao + 35
        return {'nome': nome, 'nascimento': ano_nascimento, 'idade': idade, 'ctps': ctps,
                'contratacao': contratacao, 'salario': salario, 'aposentadoria': aposentadoria}
    else:
        return {'nome': nome, 'nascimento': ano_nascimento, 'idade': idade, 'ctps': ctps}


pesquisa = trabalhador()
lista_trabalhador.append(pesquisa)


print('-=' * 30)
print(f'{azul}Nome{FIM_COR} tem o valor {azul_underline}{pesquisa["nome"]}{FIM_COR}')
print(f'{azul}Idade{FIM_COR} tem o valor {azul_underline}{pesquisa["idade"]}{FIM_COR}')
print(f'{azul}Ctps{FIM_COR} tem o valor {azul_underline}{pesquisa["ctps"]}{FIM_COR}')

if pesquisa["ctps"] != 0:
    print(f'{azul}Contratacao{FIM_COR} tem o valor {azul_underline}{pesquisa["contratacao"]}{FIM_COR}')
    print(f'{azul}Salario{FIM_COR} tem o valor {azul_underline}{pesquisa["salario"]}{FIM_COR}')
    print(f'{azul}Aposentadoria{FIM_COR} tem o valor {azul_underline}{pesquisa["aposentadoria"]}{FIM_COR}')
