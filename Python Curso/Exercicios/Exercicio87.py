# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Matriz em Python 2.0____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_coluna2 = par = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para '
                                          f'[{azul}{linha}{FIM_COR}, {vermelho}{coluna}{FIM_COR}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]

        if coluna == 2:
            soma_coluna2 += matriz[linha][coluna]

        if linha == 1:
            maior_valor_linha2: int = max(matriz[linha])

print('-=' * 30)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 30)

print(f'A soma dos valores pares é {azul_underline}{par}{FIM_COR}')
print(f'A soma dos valores da terceira coluna é {azul_underline}{soma_coluna2}{FIM_COR}')
print(f'O maior valor da segunda linha é {azul_underline}{maior_valor_linha2}{FIM_COR}')
