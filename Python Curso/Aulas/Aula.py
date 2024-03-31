import datetime

print('====== DESAFIO 02 ======')

dia: str = input('Gostaria de saber, qual é o dia em que voce nasceu!?')
mes: str = input('E em qual mes voce nasceu?')
ano: int = int(input('E qual foi o ano do seu nascimento?'))

# Get the current year
current_year = datetime.datetime.now().year

# Calculate age
idade: int = current_year - ano

print('Voce nasceu no dia {}/{}/{} Correto?'.format(dia, mes, ano))
print('Voce tem {} de idade!'.format(idade))
