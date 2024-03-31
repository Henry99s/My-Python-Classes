from time import sleep

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Maior e Menor Valor____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

quantidade = 0
soma = 0
maior_numero = None
menor_numero = None

while True:
    numero = int(input('Digite um numero inteiro: '))
    continuar = str(input(f'Quer continuar [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}]? ')).strip().upper()
    soma += numero
    quantidade += 1

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

    if continuar == 'N':
        # Computador processando
        print('\033[4;34mPROCESSANDO...\033[m')
        sleep(2)

        media = soma / quantidade
        print(f'A {verde}MEDIA{FIM_COR} de todos os numeros digitados é {azul_underline}{media}{FIM_COR}')
        print(f'O {verde}MAIOR{FIM_COR} numero digitado é {azul_underline}{maior_numero}{FIM_COR}')
        print(f'O {verde}MENOR{FIM_COR} numero digitado é {azul_underline}{menor_numero}{FIM_COR}')
        break
