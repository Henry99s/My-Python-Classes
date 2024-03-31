print('====Aumento Salarial====')

# Salario, aumento mais novo salario
salario_antigo = float(input('Qual é seu salario atual? R$'))
aumento = 15 * salario_antigo / 100
novo_salario = salario_antigo + aumento

# Resultado
print('Com um aumento de 15% do salario, seu novo salario será de: R${:.2f}'.format(novo_salario))
