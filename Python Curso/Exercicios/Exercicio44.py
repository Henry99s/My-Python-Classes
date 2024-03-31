from time import sleep

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
fundo_vermelho = '\033[41m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Escolhendo O Metodo De Pagamento____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Nome da loja
print(f'{"Lojas Guanabara":=^40}')

# Escolhendo o produto e seu valor
produto = str(input('Qual o nome do produto? ')).capitalize().strip()
valor_produto = float(input('Qual o valor do produto? '))

# Escolhendo a forma de pagamento
condicao_pagamento = int(input(f'''
[ {verde}1{FIM_COR} ] A vista em Dinheiro/Cheque (10% de Desconto)
[ {verde}2{FIM_COR} ] A vista no Cartão (5% de Desconto)
[ {verde}3{FIM_COR} ] Até 2x no Cartão de Crédito (Sem juros)
[ {verde}4{FIM_COR} ] 3x ou mais no Cartão de Crédito (20% de Juros)

Digite o numero para escolher a opção de pagamento: '''))

# Resultado das Escolhas
if condicao_pagamento == 1:
    novo_valor = valor_produto - (10 * valor_produto / 100)  # Novo valor com Desconto
    print(f'Pagamento a vista no {azul}Dinheiro/Cheque{FIM_COR}, escolhindo!')
    print(f'{azul_underline}Calculando Desconto de 10%...{FIM_COR}')
    sleep(2)
    print(f'{verde}PARABENS, DESCONTO APLICADO!{FIM_COR}')
    sleep(1)
    print(f'''O novo valor do produto {azul}{produto}{FIM_COR} é de {verde}R${novo_valor:.2f}{FIM_COR} 
       {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

elif condicao_pagamento == 2:
    novo_valor = valor_produto - (5 * valor_produto / 100)  # Novo valor com Desconto
    print(f'Pagamento a vista no {azul}Cartao{FIM_COR}, escolhido!')
    print(f'{azul_underline}Calculando Desconto de 5%...{FIM_COR}')
    sleep(2)
    print(f'{verde}PARABENS, DESCONTO APLICADO!{FIM_COR}')
    sleep(1)
    print(f'''O novo valor do produto {azul}{produto}{FIM_COR} é de {verde}R${novo_valor:.2f}{FIM_COR} 
          {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

elif condicao_pagamento == 3:
    parcela = valor_produto / 2
    print(f'Pagamento de ate 2x no {azul}Cartão de Crédito{FIM_COR} escolhido!')
    print(f'{azul_underline}Calculando parcelas...{FIM_COR}')
    sleep(2)
    print(f'''As parcelas do produto {azul}{produto}{FIM_COR} serão de {verde}R${parcela:.2f}{FIM_COR} por mês.
             {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

elif condicao_pagamento == 4:
    # Escolhas de parcelamento
    parcelas = int(input(f'''
        [ {verde}1{FIM_COR} ] {azul}3x{FIM_COR} no Cartão de Crédito
        [ {verde}2{FIM_COR} ] {azul}6x{FIM_COR} no Cartão de Crédito
        [ {verde}3{FIM_COR} ] {azul}12x{FIM_COR} no Cartão de Crédito

        Escolha em até 3 opções de parcelamento: '''))

    # Resultado das escolhas de parcelamento
    if parcelas == 1:
        valor_final = valor_produto + (valor_produto * 0.20 * 3)  # Novo Valor com Juros
        parcela = valor_final / 3
        print(f'Pagamento de ate 3x no {azul}Cartão de Crédito{FIM_COR} escolhido!')
        print(f'{azul_underline}Calculando parcelas com juros de 20%...{FIM_COR}')
        sleep(2)
        print(f'''As parcelas do produto {azul}{produto}{FIM_COR} serão de {verde}R${parcela:.2f}{FIM_COR} por mês.
         O valor final do produto sera de: {verde}R${valor_final:.2f}{FIM_COR}
                     {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

    elif parcelas == 2:
        valor_final = valor_produto + (valor_produto * 0.20 * 6)  # Novo Valor com Juros
        parcela = valor_final / 6
        print(f'Pagamento de ate 6x no {azul}Cartão de Crédito{FIM_COR} escolhido!')
        print(f'{azul_underline}Calculando parcelas com juros de 20%...{FIM_COR}')
        sleep(2)
        print(f'''As parcelas do produto {azul}{produto}{FIM_COR} serão de {verde}R${parcela:.2f}{FIM_COR} por mês.
                    O valor final do produto sera de: {verde}R${valor_final:.2f}{FIM_COR}
                                {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

    elif parcelas == 3:
        valor_final = valor_produto + (valor_produto * 0.20 * 12)  # Novo Valor com Juros
        parcela = valor_final / 12
        print(f'Pagamento de ate 12x no {azul}Cartão de Crédito{FIM_COR} escolhido!')
        print(f'{azul_underline}Calculando parcelas com juros de 20%...{FIM_COR}')
        sleep(2)
        print(f'''As parcelas do produto {azul}{produto}{FIM_COR} serão de {verde}R${parcela:.2f}{FIM_COR} por mês.
                    O valor final do produto sera de: {verde}R${valor_final:.2f}{FIM_COR}
                                {azul_marinho}MUITO OBRIGADO!!!{FIM_COR}''')

    # Erro caso nao seja escolhindo uma das 3 opcoes
    else:
        print(f'{fundo_vermelho}ERRO: NÃO FOI ESCOLHIDO UMA DAS 3 OPÇÕES{FIM_COR}')

# Erro caso nao seja escolhindo uma das 4 opcoes
else:
    print(f'{fundo_vermelho}ERRO: NÃO FOI ESCOLHIDO UMA DAS 4 OPÇÕES{FIM_COR}')
