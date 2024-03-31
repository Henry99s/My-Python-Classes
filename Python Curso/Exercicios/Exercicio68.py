from random import randrange

# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Par ou Impar____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

print(f'=' * 40)
print(f'VAMOS JOGAR PAR OU IMPAR')

vencidas = 0
while True:
    print(f'=' * 40)
    jogador = int(input(f'Diga um valor [{verde}0{FIM_COR} a {verde}10{FIM_COR}]: '))
    par_ou_impar = str(input(f'Par ou Impar? [{azul}P{FIM_COR}/{vermelho}I{FIM_COR}] ')).strip().upper()[0]
    computador = randrange(0, 10)
    resultado = jogador + computador

    if resultado % 2 == 0 and par_ou_impar == 'P' or resultado % 2 >= 1 and par_ou_impar == 'I':

        vencidas += 1

        if resultado % 2 == 0:
            print(f'{azul}_{FIM_COR}' * 40)
            print(f'Voce jogou {verde}{jogador}{FIM_COR} e o computador {vermelho}{computador}{FIM_COR}. '
                  f'Total de {azul}{resultado}{FIM_COR} DEU PAR')

        elif resultado % 2 >= 1:
            print(f'{azul}_{FIM_COR}' * 40)
            print(f'Voce jogou {verde}{jogador}{FIM_COR} e o computador {vermelho}{computador}{FIM_COR}. '
                  f'Total de {azul}{resultado}{FIM_COR} DEU IMPAR')

        print(f'{azul}_{FIM_COR}' * 40)
        print(f'{azul_underline}VOCE VENCEU!!!{FIM_COR}')
        print(f'Vamos jogar novamente...')

    elif resultado % 2 == 0 and par_ou_impar == 'I' or resultado % 2 >= 1 and par_ou_impar == 'P':

        if resultado % 2 == 0:
            print(f'{azul}_{FIM_COR}' * 40)
            print(f'Voce jogou {verde}{jogador}{FIM_COR} e o computador {vermelho}{computador}{FIM_COR}. '
                  f'Total de {azul}{resultado}{FIM_COR} DEU PAR')

        elif resultado % 2 >= 1:
            print(f'{azul}_{FIM_COR}' * 40)
            print(f'Voce jogou {verde}{jogador}{FIM_COR} e o computador {vermelho}{computador}{FIM_COR}. '
                  f'Total de {azul}{resultado}{FIM_COR} DEU IMPAR')

        print(f'{azul}_{FIM_COR}' * 40)
        print(f'{vermelho}VOCE PERDEU!!!{FIM_COR}')
        print(f'{vermelho_fundo_preto}GAME OVER!{FIM_COR} Voce venceu {azul_underline}{vencidas}{FIM_COR} vezes.')
        break
