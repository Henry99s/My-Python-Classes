# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Lista Composta e Analise de Dados____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_pessoas = []


def info_pessoas():
    nome = str(input('Nome: ')).capitalize().strip()
    peso = float(input('Peso: '))
    return {'nome': nome, 'peso': peso}


while True:
    pessoa = info_pessoas()
    lista_pessoas.append(pessoa)
    continuar = str(input(f'Quer continuar? [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente Novamente! Quer continuar? '
                              f'[{azul}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    if continuar == 'N':
        break

maior_peso = []
for pessoa in lista_pessoas:
    if not maior_peso or pessoa["peso"] > maior_peso[0]["peso"]:
        maior_peso = [pessoa]
    elif pessoa["peso"] == maior_peso[0]["peso"]:
        maior_peso.append(pessoa)

menor_peso = []
for pessoa in lista_pessoas:
    if not menor_peso or pessoa["peso"] < menor_peso[0]["peso"]:
        menor_peso = [pessoa]
    elif pessoa["peso"] == menor_peso[0]["peso"]:
        menor_peso.append(pessoa)


print(f'Total foram cadastrados {azul_underline}{len(lista_pessoas)}{FIM_COR} pessoa.')

if maior_peso:
    print(f'O(s) maior(es) peso(s) foi(ram) de {azul_underline}{maior_peso[0]["peso"]}Kg{FIM_COR}. Peso de:', end=' ')
    for pessoa in maior_peso:
        print(f'{azul}{pessoa["nome"]}{FIM_COR}',end=', ')
else:
    print(f'{vermelho}Não foi possivel obter o maior peso dos dados cadastrados!{FIM_COR}')

if menor_peso:
    print(f'\nO(s) menor(es) peso(s) foi(ram) de {azul_underline}{menor_peso[0]["peso"]}Kg{FIM_COR}. Peso de:', end=' ')
    for pessoa in menor_peso:
        print(f'{azul}{pessoa["nome"]}{FIM_COR}', end=', ')
else:
    print(f'{vermelho}Não foi possível obter o menor peso dos dados cadastrados!{FIM_COR}')
