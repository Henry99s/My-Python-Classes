# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Maior e menor valores em Tupla____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

from random import randint

menor_numero = 11
maior_numero = -1
for c in range(0, 6):
    numeros1 = randint(0, 10)
    print(numeros1, end=' ')
    if maior_numero < numeros1:
        maior_numero = numeros1

    if menor_numero > numeros1:
        menor_numero = numeros1

print(f'\nMenor número: {azul}{menor_numero}{FIM_COR}')
print(f'Maior número: {azul}{maior_numero}{FIM_COR}')

# OU

import random

# Gerar cinco números aleatórios e armazená-los em uma tupla
numeros_aleatorios = tuple(random.randint(0, 10) for _ in range(5))

# Exibir a lista de números gerados
print("Números gerados:", numeros_aleatorios)

# Encontrar o menor e o maior valor na tupla
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)

# Exibir o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
