from datetime import date
from time import sleep

# Cores
azul = '\033[1;34m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Categoria De Natação____)\033[m')
print('\033[1;31m-=-\033[m' * 20)
# ----------------------------------------------------------------------------------------------------------------------

# Descobrindo o ano de nascimento do atleta
ano_atleta = int(input('Digite o ano de nascimento do atleta: '))

# Pegando a data atual
data_atual = date.today().year

# Calculando a idade do atleta
idade_atleta = data_atual - ano_atleta

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Classificando o Atleta com base na idade
if idade_atleta <= 9:
    print(f'O atleta tem {verde}{idade_atleta}{FIM_COR} anos de idade. '
          f'Esta qualificado na categoria {azul}MIRIM{FIM_COR}')

elif idade_atleta <= 14:
    print(f'O atleta tem {verde}{idade_atleta}{FIM_COR} anos de idade. '
          f'Esta qualificado na categoria {azul}INFANTIL{FIM_COR}')

elif idade_atleta <= 19:
    print(f'O atleta tem {verde}{idade_atleta}{FIM_COR} anos de idade. '
          f'Esta qualificado na categoria {azul}JUNIOR{FIM_COR}')

elif idade_atleta <= 25:
    print(f'O atleta tem {verde}{idade_atleta}{FIM_COR} anos de idade. '
          f'Esta qualificado na categoria {azul}SENIOR{FIM_COR}')

else:
    print(f'O atleta tem {verde}{idade_atleta}{FIM_COR} anos de idade. '
          f'Esta qualificado na categoria {azul}MASTER{FIM_COR}')
