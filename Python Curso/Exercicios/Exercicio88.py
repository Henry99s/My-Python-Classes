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
print(f'{" " * 10}{vermelho_fundo_preto}(_____Palpites Para A Mega Sena____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

mega_sena = []
REPETIDOS = []
vezes_jogar = int(input('Quantos jogo voce quer que eu sorteie? '))

for _ in range(vezes_jogar):
    jogo = []

    while len(jogo) < 6:
        numeros_gerados = randint(1, 60)

        if numeros_gerados not in jogo:
            jogo.append(numeros_gerados)

        else:
            REPETIDOS.append(numeros_gerados)

    jogo.sort()
    mega_sena.append(jogo)

contar = 0
for jogos in mega_sena:
    sleep(1)
    contar += 1
    print(f'Jogo {azul}{contar}{FIM_COR}: {jogos}')
