# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Lista de Preços____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_produtos = []


def informacoes_preco():
    nome_produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco_produto = float(input('Digite o preço do produto: '))
    return {'nome_produto': nome_produto,
            'preco_produto': preco_produto}


contar = 0
while True:
    contar += 1
    print(f'Digite as informações do {azul}{contar}º{FIM_COR} produto')
    produto = informacoes_preco()
    lista_produtos.append(produto)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N] ')).strip().upper()

    if continuar == 'N':
        break

print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)

for produto in lista_produtos:
    nome_produto = produto["nome_produto"]
    preco_produto = produto["preco_produto"]

    print(f'{nome_produto:.<30} R${preco_produto:>7.2f}')

print('_' * 40)
