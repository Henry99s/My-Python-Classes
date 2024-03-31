from math import trunc

print('=====Transformando um Numero Real em Numero Inteiro=====')

# Descobrindo um numero aleatorio real
numero_real = float(input('Digite um numero aleatorio com casas decimais: '))

# Resultado transformando o numero real em inteiro
print('O numero escolhido {0} em sua versao inteira e {1}'.format(numero_real, trunc(numero_real)))
