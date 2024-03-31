from time import sleep

print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Calculando O Emprestimo Para Compra De Uma Casa____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Escolhendo uma casa e colhendo infomações do usuario.
valor_da_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario mensal? '))
anos_pagando = int(input('Em quantos anos deseja pagar a casa? '))

# Calculado o valor da prestação mensal.
prestacao_mensal = (valor_da_casa / anos_pagando) / 12

# Estabelecendo a regra de não poder exceder 30% do salario
regra = 30 * salario / 100

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Caso o a regra seja cumprida, o emprestimo sera concluido, caso não, então o emprestimo será negado.
if prestacao_mensal >= regra:
    print('\033[1;31mSeu emprestimo foi negado!!!\033[m')

else:
    print('\033[1;32mParabens! Seu emprestimo foi aprovado.\033[m')
