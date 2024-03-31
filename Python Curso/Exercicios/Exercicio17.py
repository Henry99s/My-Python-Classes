from math import hypot

print('=====Fazendo Calculo do Teorema de Pitagoras=====')

# Cordenadas do triangulo retangulo
x = float(input('Digite o valor do Cateto oposto: '))
y = float(input('Digite o valor do Cateto adjacente: '))

# Calculo da Hipotenusa
z = hypot(x, y)

# Resultado
print('Fazendo os calculos, a hipotenusa deste triangulo retangulo seria de: {0:.3f}'.format(z))
