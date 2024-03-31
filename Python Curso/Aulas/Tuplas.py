lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita'

print(lanche)

print('_' * 30)

print(sorted(lanche))

print('_' * 30)

for comida in range(0, len(lanche)):
    print(f'Eu comi {lanche[comida]} na posicao {comida}')

print('_' * 30)

for comida in lanche:
    print(f'Eu comi {comida}')

print('_' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} comida na posicao {pos}')

print('_' * 30)

print('Comi pra caramba!')
