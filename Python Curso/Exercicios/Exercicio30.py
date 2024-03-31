print('-=-' * 20)
print('(____DESCOBRINDO SE O NUMERO ESCOLHINDO É PAR OU IMPAR____)')
print('-=-' * 20)

# Escolhendo um Numero
numero = int(input('Digite um numero: '))

# Resultado
if numero % 2 == 0:
    print(f'O numero é {numero} par!')
else:
    print(f'O numero é {numero} impar!')
