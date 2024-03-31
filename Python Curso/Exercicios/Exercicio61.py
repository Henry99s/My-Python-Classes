from time import sleep

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Progressão Aritimetica.V2____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------
print(f'Faça uma progressão aritimetica de até {verde}10{FIM_COR} termos')


primeiro_termo = int(input(f'Digite o {azul_underline}PRIMEIRO{FIM_COR} termo desta progressão aritimetica: '))
razao = int(input(f'Digite a {azul_underline}RAZÃO{FIM_COR} dessa progressão:  '))


termos = 10


print(f'Em uma progressão aritimetica, onde o primeiro termo é {azul}{primeiro_termo}{FIM_COR} '
      f'e sua razão é {azul}{razao}{FIM_COR}. Os {verde}10{FIM_COR} primeiros numeros são: ')

PA = primeiro_termo
n = 0
while n < termos:
    print(PA, end=' ')
    PA += razao
    n += 1
