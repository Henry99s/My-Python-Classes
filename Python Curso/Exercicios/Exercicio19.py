import random

print('=====Sorteio na Sala de Aula====')

# Os 4 alunos da Sala de Aula
a = input('Qual o nome do primeiro aluno: ')
b = input('Qual o nome do segundo aluno: ')
c = input('Qual o nome do terceiro aluno: ')
d = input('Qual o nome do quarto aluno: ')

# Calculo de aleatoriedade
aluno = random.choice([a, b, c, d])

# Resultado
print('O aluno escolhido é: {}'.format(aluno))
