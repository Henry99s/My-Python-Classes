# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Tabuada 2.0____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

n = int(input('Digite o numero que queira saber a sua tabuada: '))
print('_____________')
for tabuada in range(0, 11):
    print(f'{azul}{n}{FIM_COR} X {verde}{tabuada}{FIM_COR} = {azul_marinho}{n * tabuada}{FIM_COR}')
print('_____________')
