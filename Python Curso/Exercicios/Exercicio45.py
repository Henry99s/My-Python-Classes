from time import sleep
from random import randrange

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
fundo_vermelho = '\033[41m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Jogo Pedra Papel Tesoura____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Boas Vindas!
print('Vamos jogar Pedra, Papel e Tesoura?')

# Criando um dicionario para Pedra, Papel, Tesoura
escolhas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

# Computador escolhendo
computador = randrange(1, 4)

# Jogador escolhendo
escolha_jogador = int(input(f'''
[ {azul}1{FIM_COR} ] Pedra
[ {azul}2{FIM_COR} ] Papel
[ {azul}3{FIM_COR} ] Tesoura

Faça sua escolha: '''))

# Computador processando
print(f'{azul_marinho}-=-{FIM_COR}' * 20)
print(f'{azul}JO{FIM_COR}')
sleep(1)
print(f'{azul}KEN{FIM_COR}')
sleep(1)
print(f'{azul}PO!!!{FIM_COR}')
sleep(1)
print(f'{azul_marinho}-=-{FIM_COR}' * 20)

# Resultado
if computador == escolha_jogador:

    print(f'{vermelho}DROGA!{FIM_COR} Foi empate... Voce escolheu {verde}{escolhas[escolha_jogador]}{FIM_COR} '
          f'e eu escolhi {vermelho}{escolhas[computador]}{FIM_COR}.')
    print(f'{vermelho}EMPATE{FIM_COR}')

elif (computador == 1 and escolha_jogador == 3
      or computador == 2 and escolha_jogador == 1
      or computador == 3 and escolha_jogador == 2):

    print(f'{azul}GANHEI!{FIM_COR} Voce escolheu {verde}{escolhas[escolha_jogador]}{FIM_COR}, '
          f'o eu escolhi {vermelho}{escolhas[computador]}{FIM_COR}.')
    print(f'O Computador {azul}VENCEU{FIM_COR}')

elif (computador == 1 and escolha_jogador == 2
      or computador == 2 and escolha_jogador == 3
      or computador == 3 and escolha_jogador == 1):

    print(f'{azul}VOCE GANHOU!{FIM_COR} Voce escolheu {verde}{escolhas[escolha_jogador]}{FIM_COR}, '
          f'eu escolhi {vermelho}{escolhas[computador]}{FIM_COR}.')
    print(f'O Jogador {azul}VENCEU{FIM_COR}')
