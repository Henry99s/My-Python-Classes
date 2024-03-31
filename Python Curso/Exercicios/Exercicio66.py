# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Numeros com Flag____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

soma = conta = 0

while True:
    numero = int(input(f'Digite um numero inteiro [Digite {vermelho}999{FIM_COR} para parar]: '))
    if numero == 999:
        break
    soma += numero
    conta += 1
print(f'Foram digitados {azul}{conta}{FIM_COR}, e a soma todos eles é {azul}{soma}{FIM_COR}. ')
