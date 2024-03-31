from random import shuffle

print('=====Ordem Aleatoria de Trabalhos=====')

# Escolhendo os Alunos
a = input('Qual o nome do primeiro aluno: ')
b = input('Qual o nome do segundo aluno: ')
c = input('Qual o nome do terceiro aluno: ')
d = input('Qual o nome do quarto aluno: ')

# Sorteando a ordem de apresentação dos alunos
ordem = [a, b, c, d]
shuffle(ordem)

# Resultado
print(' A ordem de apresentacao sera: {}'.format(ordem))
