# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
roxo = '\033[1;35m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Unindo Dicionarios e Listas____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_cadastro = list()
lista_mulheres = list()
lista_idade_acima_media = list()


def cadastro():
    nome = str(input('Nome: ')).strip().capitalize()
    while True:
        sexo = str(input(f'Sexo [{azul}M{FIM_COR}/{roxo}F{FIM_COR}]: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        print(f'{vermelho}Erro! Por Favor, digite M ou F!{FIM_COR}')
    idade = int(input('Idade: '))
    return {'nome': nome, 'sexo': sexo, 'idade': idade}


soma_idade = 0

while True:
    pessoas = cadastro()
    lista_cadastro.append(pessoas)
    soma_idade += pessoas["idade"]

    if pessoas["sexo"] == 'F':
        lista_mulheres.append(pessoas)

    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente Novamente! Quer continuar? '
                              f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    if continuar == 'N':
        break

media_idade = soma_idade / len(lista_cadastro)

for pessoa in lista_cadastro:
    if pessoa["idade"] > media_idade:
        lista_idade_acima_media.append(pessoa.copy())

print(f'{azul}-={FIM_COR}' * 40)

print(f'Foram cadastradas {azul_underline}{len(lista_cadastro)}{FIM_COR} pessoas.')
print(f'A media de idade do grupo é {azul_underline}{media_idade:.1f}{FIM_COR}.')
print(f'A lista apenas com mulher cadastradas é {verde}{lista_mulheres}{FIM_COR}')
if not lista_mulheres:
    print(f'{vermelho}Nenhuma mulher foi cadastrada!{FIM_COR}')
print(f'A lista de pessoa com idade acima da media do grupo é {verde}{lista_idade_acima_media}{FIM_COR}.')
