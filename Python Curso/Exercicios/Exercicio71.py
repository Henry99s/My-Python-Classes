# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Simulador de Caixa Eletronico____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor_saque = int(input('Quanto deseja sacar? R$'))

resultado_inteiro200 = 0
resultado_inteiro100 = 0
resultado_inteiro50 = 0
resultado_inteiro20 = 0
resultado_inteiro10 = 0
resultado_inteiro5 = 0
resultado_inteiro1 = 0

while True:
    if valor_saque >= 200:
        resultado_inteiro200 = valor_saque // 200
        valor_saque %= 200
        print(f'Total de {verde}{resultado_inteiro200}{FIM_COR} cédulas de {azul}R$200{FIM_COR}')
        if valor_saque == 0:
            break

    elif valor_saque >= 100:
        resultado_inteiro100 = valor_saque // 100
        valor_saque %= 100
        print(f'Total de {verde}{resultado_inteiro100}{FIM_COR} cédulas de {azul}R$100{FIM_COR}')
        if valor_saque == 0:
            break

    elif valor_saque >= 50:
        resultado_inteiro50 = valor_saque // 50
        valor_saque %= 50
        print(f'Total de {verde}{resultado_inteiro50}{FIM_COR} cédulas de {azul}R$50{FIM_COR}')
        if valor_saque == 0:
            break

    elif valor_saque >= 20:
        resultado_inteiro20 = valor_saque // 20
        valor_saque %= 20
        print(f'Total de {verde}{resultado_inteiro20}{FIM_COR} cédulas de {azul}R$20{FIM_COR}')
        if valor_saque == 0:
            break

    elif valor_saque >= 10:
        resultado_inteiro10 = valor_saque // 10
        valor_saque %= 10
        print(f'Total de {verde}{resultado_inteiro10}{FIM_COR} cédulas de {azul}R$10{FIM_COR}')
        if valor_saque == 0:
            break

    elif valor_saque >= 5:
        resultado_inteiro5 = valor_saque // 5
        valor_saque %= 5
        print(f'Total de {verde}{resultado_inteiro5}{FIM_COR} cédulas de {azul}R$5{FIM_COR}')
        if valor_saque == 0:
            break

    else:
        resultado_inteiro1 = valor_saque
        valor_saque = 0
        print(f'Total de {verde}{resultado_inteiro1}{FIM_COR} moedas de {azul}R$1{FIM_COR}')
        break
