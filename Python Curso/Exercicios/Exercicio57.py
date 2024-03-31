# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Analisador de Sexo____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Digite seu sexo {azul}[M/F]{FIM_COR}: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print(f'{vermelho}Valor errado. Digite o Valor correto!{FIM_COR}')

if sexo == 'M':
    print(f'{azul}Obrigado!{FIM_COR}')
elif sexo == 'F':
    print(f'{azul}Obrigada!{FIM_COR}')
