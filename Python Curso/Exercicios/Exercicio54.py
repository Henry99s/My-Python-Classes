from datetime import date

# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Grupo de Maioridade____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Pegando o ano atual do computador.
hoje = date.today().year

# Dando o valor inicial para pessoas acima e abixo da idade.
acima_maioridade = 0
abaixo_maioridade = 0

# Informando o ano de nascimento de cada participante e descobrindo sua idade.
for grupo in range(1, 8):
    ano_nascimento = int(input(f'Qual o ano de nascimento do {verde}{grupo}º{FIM_COR} participante: '))
    idade = hoje - ano_nascimento

    if idade < 18:
        abaixo_maioridade += 1  # Calculando quantos são menor de idade.
    else:
        acima_maioridade += 1   # Calculando quantos são maior de idade.

# Resultado
print(f'{azul}{acima_maioridade}{FIM_COR} pessoas são maiores de idade!')
print(f'{azul}{abaixo_maioridade}{FIM_COR} pessoas são abaixo da maioridade!')
