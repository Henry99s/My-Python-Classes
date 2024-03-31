print('-=-' * 20)
print('(____Calculando o Valor de uma Passagem____)')
print('-=-' * 20)

# Distancia percorrida da Viagem
distancia_viagem = float(input('Qual foi a distancia da sua viagem em Km? '))

# Calculando o valor da passagem, sendo menos de 200km custando R$0.50 ou maior que 200Km custando R$0.45
if distancia_viagem <= 200:
    valor_passagem = distancia_viagem * 0.50
    print(f'O preco da passagem sera de: R${valor_passagem:.2f}')
else:
    valor_passagem = distancia_viagem * 0.45
    print(f'O preco da passagem sera de: R${valor_passagem:.2f}')
