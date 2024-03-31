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
print(f'{vermelho_fundo_preto}(_____Progressão Aritimetica____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------
print(f'Faça uma progressão aritimetica de até {verde}10{FIM_COR} termos')

# Lendo os primeiro termo e a sua razão.
primeiro_termo = int(input(f'Digite o {azul_underline}PRIMEIRO{FIM_COR} termo desta progressão aritimetica: '))
razao = int(input(f'Digite a {azul_underline}RAZÃO{FIM_COR} dessa progressão:  '))

# Fazendo a estrutura de repetição "for" mostrar os primeiros 10 numeros.
dez_termos = 10 * razao

# Fazendo a estrutura de repetição "for" mostrar os primeiros 10 numeros.
# Mesmo que a razao seja menor do que o primeiro termo da progressao aritimetica.
if razao <= primeiro_termo:
    dez_termos = (10 * razao) + primeiro_termo

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Mostrando a progresão aritimetica, com o primeiro termo e sua razão fornecidos pelo usuario.
print(f'Em uma progressão aritimetica, onde o primeiro termo é {azul}{primeiro_termo}{FIM_COR} '
      f'e sua razão é {azul}{razao}{FIM_COR}. Os {verde}10{FIM_COR} primeiros numeros são: ')
for PA in range(primeiro_termo, dez_termos, razao):
    print(PA, end=' ')
