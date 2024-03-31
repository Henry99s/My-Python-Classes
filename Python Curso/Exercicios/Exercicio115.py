from exercicio115 import sistema

# Cores
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Criando um Menu____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

sistema.sistema()
