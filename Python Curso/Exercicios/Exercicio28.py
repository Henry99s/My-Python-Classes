from random import randrange
from time import sleep
print('(____Advinhando um Numero____)')

print('-=-' * 20)
print('!Vou pensar em um numero entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

# Maquina escolhendo um numero de 0 a 5
numero = int(randrange(0, 5))

# Jogador Advinhando
escolha = int(input('Em qual numero eu pensei? '))

# Computador processando
print('PROCESSANDO...')
sleep(2)

# Resultado
if escolha == numero:
    print('\nPARABENS! Voce Acertou o Numero!')
else:
    print('\nQUE PENA... Voce Errou o Numero!')

# Revelando o numero
print(f'O Numero escolhido foi {numero}')
