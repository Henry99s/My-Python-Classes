print('(____Aprendendo sobre Condições____)')

# Carro Novo ou Velho
print('__________________________')
print('----Carro novo/velho----')

tempo_carro = int(input('Qual a idade do seu carro? '))
print('Carro Novo' if tempo_carro <= 3 else'Carro Velho')

print('----FIM----')


# Nome Bonito ou Normal...
print('__________________________')
print('----Nome Bonito ou Não----')

nome = str(input('Qual o seu nome? '))
if nome == 'Henrique':
    print('Que nome maravilhoso!')
else:
    print('Poderia ser Henrique, mas tudo bem...')

print(f'Bom dia, {nome}!')

print('----FIM----')


# Media Escolarial
print('__________________________')
print('----Media Boa ou Ruim----')

nota1 = float(input('Nota em Portugues: '))
nota2 = float(input('Nota em Matematica: '))
media = (nota1 + nota2) / 2

print(f'Sua Media foi {media:.1f}')

if media >= 7.0:
    print('Voce passou, PARABÉNS!')
else:
    print('Infelizmente, voce não passou...')

print('----FIM-----')
