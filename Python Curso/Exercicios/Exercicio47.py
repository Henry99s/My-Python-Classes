from time import sleep
from random import randrange

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
print(f'{vermelho_fundo_preto}(_____Numeros Pares Entre 1 e 50____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

print(f'Os {azul}NUMEROS PARES{FIM_COR} entre {verde}1{FIM_COR} e {verde}50{FIM_COR} são: ')

for numeros_pares in range(2, 51, 2):
    sleep(0.4)
    print(f'{azul_marinho}{numeros_pares}{FIM_COR}', end=' ')
