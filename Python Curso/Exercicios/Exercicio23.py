print('=====Brincando com Separadores de Texto=====')

# Escolhendo um numero
numero = int(input('Digite um numero de 0 a 9999: '))

# Calculos para descobrir a Unidade, Dezena, Centena e Milhar
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

# Resultados
print('A unidade desse numero é {}'.format(u))
print('A dezena desse numero é {}'.format(d))
print('A centena desse numero é {}'.format(c))
print('O milhar desse numero é {}'.format(m))
