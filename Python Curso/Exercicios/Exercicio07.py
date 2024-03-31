print('=====Media do Aluno=====')

# Aluno
alu = input('Nome do aluno: ')

# A nota do aluno em cada mateira
no1 = float(input('Nota de Portugues: '))
no2 = float(input('Nota de Matematica: '))

# Calculo da media
med = (no1+no2)/2

# Resultado
print('A nota do aluno {0} na materia de portugues foi de {1}, e sua nota em matematica foi de {2}'
      .format(alu, no1, no2))
print('Dado as notas, o aluno {0}, teve uma media de {1:.1f}.'.format(alu, med))
