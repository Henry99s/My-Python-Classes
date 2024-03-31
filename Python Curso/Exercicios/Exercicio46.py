from time import sleep

# Cores
vermelho = '\033[1;31m'
azul_marinho_fundo_preto = '\033[1;36;40m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Fogos de Atificio____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Contagem regressiva para fogos de artificio, com intervalo de 1s
for fogos_artificio in range(10, 0, -1):
    sleep(1)
    print(f'{verde}{fogos_artificio}{FIM_COR}')

sleep(1)
print(f'{azul_marinho_fundo_preto}!!!!!!BOOMMM!!!!!!!{FIM_COR}')

