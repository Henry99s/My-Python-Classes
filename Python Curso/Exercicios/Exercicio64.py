# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Tratando Vários Valores____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------
print('Neste programa, o computador ira ler todos os numeros digitados pelo usuario, '
      f'soma-los e so vai parar quando for digitado {verde}"999"{FIM_COR}')

quantidade = 0
soma = 0
while True:
    numeros = int(input('Digite um numero inteiro: '))
    if numeros == 999:
        break
    soma += numeros
    quantidade += 1

print(f'Foram digitados {azul}{quantidade}{FIM_COR} numeros, e a soma de todos eles é {azul_underline}{soma}{FIM_COR}.')
