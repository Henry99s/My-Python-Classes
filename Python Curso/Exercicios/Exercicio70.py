# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Estatisticas em Produtos____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

print('_' * 40)
print('LOJAS BARATÃO')
print('_' * 40)

lista_produtos = []


def produtos():
    nome_produto = str(input(f'Nome do {verde}{produto}º{FIM_COR} produto? ')).strip().capitalize()
    preco_produto = float(input(f'Preço do {verde}{produto}º{FIM_COR} produto? R$'))
    while preco_produto < 0:
        print('Erro! Tente novamente')
        preco_produto = float(input(f'Preço do {verde}{produto}º{FIM_COR} produto? R$'))
    return {'nome_produto': nome_produto,
            'preco_produto': preco_produto}


produto = 0
soma = 0
mais_mil = 0
while True:
    produto += 1
    add_produtos = produtos()
    lista_produtos.append(add_produtos)

    continuar = str(input(f'Quer continuar?[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('Erro! Tente novamente')
        continuar = str(input(f'Quer continuar?[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    soma += add_produtos["preco_produto"]

    if add_produtos['preco_produto'] > 1000:
        mais_mil += 1

    produto_mais_barato = None
    for add_produtos in lista_produtos:
        if produto_mais_barato is None or add_produtos['preco_produto'] < produto_mais_barato['preco_produto']:
            produto_mais_barato = add_produtos

    if continuar == 'N':
        print('_' * 40)
        print(f'O Valor total da compra é de {azul_underline}R${soma}{FIM_COR}')
        print(f'{azul_underline}{mais_mil}{FIM_COR} ultrapassaram o valor de R$1000.')
        print(f'O produto mais barato é {azul}{produto_mais_barato["nome_produto"]}{FIM_COR}, '
              f'que custa {azul_underline}R${produto_mais_barato["preco_produto"]}{FIM_COR}')
        break
