from datetime import date
print('-=-' * 20)
print('(____Calculo de no Bissexto___)')
print('-=-' * 20)

# Escolhendo um ano
ano = int(input('Digite um ano, coloque 0 para analisar o ano atual: '))

# Pegando o ano atual do computador
if ano == 0:
    ano = date.today().year

# Calculando se o ano tem 366 dias ou 365, ou seja, se ele é Bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano não de {ano} é Bissexto!')
