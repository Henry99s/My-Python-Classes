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
print(f'{vermelho_fundo_preto}(_____Numeros Primos____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

numero_inteiro = int(input('Digite um numero inteiro: '))
contador_primo = 0
for n in range(1, numero_inteiro + 1):
    if numero_inteiro % n == 0:
        print(f'{azul}', end='')
        contador_primo += 1
    else:
        print(f'{FIM_COR}', end='')
    print(f'{n}', end=' ')
print(f'\n{FIM_COR}O numero {verde}{numero_inteiro}{FIM_COR} foi divisivel {azul_underline}{contador_primo}{FIM_COR} vezes.')

if contador_primo == 2:
    print(f'O numero {verde}{numero_inteiro}{FIM_COR} é primo!!!')
else:
    print(f'O numero {verde}{numero_inteiro}{FIM_COR} não é primo!!!')
