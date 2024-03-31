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
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {azul}{nome}{FIM_COR} jogou? '))
    gols_partidas = list()
    total_gols = 0
    for partida in range(partidas):
        gols_na_partida = int(input(f'Quantos gols na partida {verde}{partida + 1}{FIM_COR}? '))
        total_gols += gols_na_partida
        gols_partidas.append(gols_na_partida)
    return {'nome': nome, 'partidas': partidas, 'gols_partidas': gols_partidas, 'total_gols': total_gols}


while True:
    performace = jogador()
    o_jogador.append(performace)
    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente Novamente! Quer continuar? '
                              f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'{azul}-={FIM_COR}' * 40)
print('cod ', end='')
for i in performace.keys():
    print(f'{i:<15}', end='')
print()

print(f'{verde}-{FIM_COR}' * 80)
for k, v in enumerate(o_jogador):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print(f'{azul}-={FIM_COR}' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [Nº] '))
    if busca >= len(o_jogador):
        print(f'ERRO! Não existe jogador com código {busca}')

    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {o_jogador[busca]["nome"]}:')
        for p, g in enumerate(o_jogador[busca]["gols_partidas"]):
            print(f'   => Na partida {verde}{p + 1}{FIM_COR}, fez {azul}{g}{FIM_COR} gols.')

    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente Novamente! Quer continuar? '
                              f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    if continuar == 'N':
        break
    print(f'{azul}-={FIM_COR}' * 40)
