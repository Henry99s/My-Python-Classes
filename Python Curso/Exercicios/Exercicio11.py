print('====Pintar uma Parede====')

# Dimensoes da parede
Lar = float(input('Quanto de Largura tem a parede ? '))
Alt = float(input('Quanto de Altura tem a parede ? '))

# Calculo de area
Area = Lar*Alt

# Quantidade de tinta nescessaria para pintar a parede
print('Sabendo que cada litro de tinta, pinta uma area de 2m quadrados, voce precisa de {}L de tinta para pintar toda a parede'.format(Area/2))
