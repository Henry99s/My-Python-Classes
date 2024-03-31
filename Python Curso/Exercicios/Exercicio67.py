# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Tabuada 3.0____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

numero = int(input('Quer ver a tabuada de qual valor? '))

while numero >= 0:
    print(f'{vermelho}_{FIM_COR}' * 20)

    for tabuada in range(1, 11):
        resultado = numero * tabuada
        print(f'{verde}{numero}{FIM_COR} X {azul}{tabuada}{FIM_COR} = {azul_underline}{resultado}{FIM_COR}')

    print(f'{vermelho}_{FIM_COR}' * 20)
    numero = int(input('Quer ver a tabuada de qual valor? '))
