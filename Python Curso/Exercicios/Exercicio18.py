import math

print('=====Descobrindo o Seno, Consseno e Tangente=====')

# Decobrindo o angulo
angulo = float(input('Digite um angulo: '))

# Calculos, transformando o angulo em radial, e descobrindo o seno, cosseno e tangente
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

# Resultado
print('Com um angulo de {0}, o valor do seno será {1:.4f}, de cosseno será {2:.4f} e da tangente será {3:.4f}'
      .format(angulo, seno, cosseno, tangente))
