# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Cadastro de Jogador de Futebol____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

o_jogador = list()


def jogador():
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {azul}{nome}{FIM_COR} jogou? '))
    gols_partidas = list()
    total_gols = 0
    for partida in range(partidas):
        gols_na_partida = int(input(f'Quantos gols na partida {verde}{partida + 1}{FIM_COR}? '))
        total_gols += gols_na_partida
        gols_partidas.append(gols_na_partida)
    return {'nome': nome, 'partidas': partidas, 'gols_partidas': gols_partidas, 'total_gols': total_gols}


performace = jogador()
o_jogador.append(performace)

print(f'{verde}-={FIM_COR}' * 30)
print(performace)
print(f'{verde}-={FIM_COR}' * 30)

print(f'O campo {azul}Nome{FIM_COR} tem o valor {azul_underline}{performace["nome"]}{FIM_COR}')
print(f'O campo {azul}Gols{FIM_COR} tem o valor {azul_underline}{performace["gols_partidas"]}{FIM_COR}')
print(f'O campo {azul}Total{FIM_COR} tem o valor {azul_underline}{performace["total_gols"]}{FIM_COR}')
print(f'{verde}-={FIM_COR}' * 30)

print(f'O jogador {azul}{performace["nome"]}{FIM_COR} jogou {azul}{performace["partidas"]}{FIM_COR} partidas.')

for p, g in enumerate(performace["gols_partidas"]):
    print(f'   => Na partida {verde}{p + 1}{FIM_COR}, fez {azul}{g}{FIM_COR} gols.')

print(f'Foi um total de {azul_underline}{performace["total_gols"]}{FIM_COR} gols.')
