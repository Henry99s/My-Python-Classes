from exercicio110 import moeda

# Cores
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Reduzindo o Programa 109____){FIM_COR}'.center(20))
print(f'{vermelho}-=-{FIM_COR}' * 20)

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 7, 12)
