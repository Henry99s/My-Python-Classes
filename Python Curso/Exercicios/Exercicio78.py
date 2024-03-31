# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Maior e Menor Valores na Lista____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_numeros = []
for lista in range(5):
    lista_numeros.append(int(input('Digite um numero: ')))

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

print(f'A lista criada é: {azul}{lista_numeros}{FIM_COR}')

print(f'O maior valor foi {azul}{maior_valor}{FIM_COR} '
      f'que está na posição', end=' ')
for i, v in enumerate(lista_numeros):
    if v == maior_valor:
        print(f'{azul_underline}{i}{FIM_COR}', end=' ')

print(f'\nO menor valor foi {azul}{menor_valor}{FIM_COR} '
      f'que está na posição', end=' ')
for i, v in enumerate(lista_numeros):
    if v == menor_valor:
        print(f'{azul_underline}{i}{FIM_COR}', end=' ')
