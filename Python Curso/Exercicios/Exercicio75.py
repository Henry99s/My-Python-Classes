# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Analise de Dados em uma Tupla____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

numeros_pares = []
while True:

    lista_numeros = tuple(int(input('Digite um numero: '))for _ in range(4))

    numeros_pares.extend(numero_par for numero_par in lista_numeros if numero_par % 2 == 0)

    break

print(f'Voce digitou os valores {verde}{lista_numeros}{FIM_COR}')

print(f'O numero 9 apareceu {verde}{lista_numeros.count(9)}{FIM_COR} vezes')

try:
    posicao_3 = lista_numeros.index(3)
    print(f'O valor 3 foi encontrado na {verde}{posicao_3 + 1}º{FIM_COR} posicao')

except ValueError:
    print(f'Nao foi encontrado {vermelho}NENHUM{FIM_COR} valor 3 nos valores digitados!')

print(f'Os valores pares digitados foram {verde}{numeros_pares}{FIM_COR}')
