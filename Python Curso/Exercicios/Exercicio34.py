print('-=-' * 20)
print('(____Calculando Novo Salario 2.0____)')
print('-=-' * 20)

# Descobrindo Novo Salario
salario_antigo = float(input('Digite seu salario: '))

# Calculando o aumento, maior ou igual a um salario de R$1250.00, aumento de 10%, se for maior, aumento de 15%
if salario_antigo >= 1250:
     aumento = 10 * salario_antigo / 100
     salario_novo = salario_antigo + aumento

else:
    aumento = 15 * salario_antigo / 100
    salario_novo = salario_antigo + aumento

# Resultado
print(f'Com o novo aumento salarial, seu novo salario sera de: R${salario_novo:.2f} ')
