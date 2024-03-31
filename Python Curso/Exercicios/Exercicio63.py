# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Sequencia de Fibonacci____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

n = int(input('Escreva a quantidade de numeros na sequencia de Fibonacci voce gostaria de ver: '))
numero1 = 0
numero2 = 1
conta = 0

while conta < n:
    print(f'{azul}{numero1}{FIM_COR}', end=' ')
    numero1, numero2 = numero2, numero1 + numero2
    conta += 1
