# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Lista com Pares e Impares____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_numeros = [[], []]
numero = 0
for numeros in range(7):
    numero = int(input(f'Digite o {verde}{numeros + 1}º{FIM_COR} valor: '))

    if numero % 2 == 0:
        lista_numeros[0].append(numero)

    elif numero % 2 == 1:
        lista_numeros[1].append(numero)

lista_numeros[0].sort()
lista_numeros[1].sort()
print(f'A lista com os numeros {azul}PARES{FIM_COR} são: {azul}{lista_numeros[0]}{FIM_COR}')
print(f'A lista com os numeros {verde}IMPARES{FIM_COR} são: {verde}{lista_numeros[1]}{FIM_COR}')
