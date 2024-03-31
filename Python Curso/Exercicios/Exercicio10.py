print('=====Seu Dinheiro em Dolar=====')

# Quanto de Dinheiro a pessoa tem ?
car = float(input('Quanto dinheiro tem em sua carteira ? R$'))
dolar = car / 5.03

# Conversão
print('Convertendo seu dinheiro para dolar, voce teria: US${:.2f}'.format(dolar))
