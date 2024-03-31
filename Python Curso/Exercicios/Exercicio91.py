from random import randint
from time import sleep

# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Jogo de Dados em Python____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

jogadas = dict()

for jogador in range(4):
    jogadas[f"jogador_{jogador + 1}"] = int(randint(1, 12))

print('Valores Sorteados:')
for j, r in jogadas.items():
    print(f'    O {verde}{j}{FIM_COR} tirou {azul_underline}{r}{FIM_COR}')
    sleep(1)

sorted_jogadas = dict(sorted(jogadas.items(), key=lambda x: x[1], reverse=True))

print('Ranking dos Jogadores:')
lugar = 0
for j, r in sorted_jogadas.items():
    lugar += 1
    print(f'    {azul}{lugar}º{FIM_COR} Lugar: {verde}{j}{FIM_COR} com {azul_underline}{r}{FIM_COR}')
    sleep(1)
