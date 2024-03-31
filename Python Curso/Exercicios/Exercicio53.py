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
print(f'{vermelho_fundo_preto}(_____Palindromos____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

frase = str(input('Digite uma frase: ')).strip().upper()
dividindo = frase.split()
junto = ''.join(dividindo)
inverso = ''

for letras in range(len(junto) - 1, -1, -1):
   inverso += junto[letras]
print(f'O inverso de {azul}{junto}{FIM_COR} é {azul}{inverso}{FIM_COR}')

if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')
