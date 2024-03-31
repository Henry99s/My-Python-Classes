from time import sleep
from datetime import date

print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Alistamento No Serviço Militar____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Descobrindo o ano de nascimento
ano_nascimento = int(input('Qual o ano em que voce nasceu? '))

# Buscando o ano atual
ano_atual = date.today().year

# Idade para alistamento
idade_alistamento = 18

# Calculo de quantos anos faltam ou ja se passaram para o alistamento
falta_passou = (ano_atual - ano_nascimento) - idade_alistamento

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado
if (ano_atual - ano_nascimento) < idade_alistamento:
    print(f'\033[1;34mAinda não é hora de se alistar\033[m, faltam \033[34m{falta_passou}\033[m anos para se alistar!')

elif (ano_atual - ano_nascimento) > idade_alistamento:
    print(f'\033[1;31mJa se passou \033[34m{falta_passou}\033[m \033[1;31manos da hora de se alistar!!!\033[m')

elif (ano_atual - ano_nascimento) == idade_alistamento:
    print(f'\033[1;36mMeus Parabens! Esta na hora de se alistar esse ano.\033[m')
