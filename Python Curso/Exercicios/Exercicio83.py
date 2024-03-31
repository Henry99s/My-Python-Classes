# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Validando Expressões Mateméticas____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

expresao = str(input('Digite uma expressão: '))
abre = []
fecha = []

for simbolo in expresao:
    if simbolo == '(':
        abre.append('(')
    if simbolo == ')':
        fecha.append(')')

if len(abre) == len(fecha):
    print('Sua expressao é valida!')
else:
    print('Sua expresao é invalida!')
