# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Dividindo Valores Em Varias Listas____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []
contador = 0
while True:
    contador += 1
    numero = int(input(f'Digite o {verde}{contador}º{FIM_COR} valor: '))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        lista_numeros_pares.append(numero)

    else:
        lista_numeros_impares.append(numero)

    continuar = str(input(f'Quer continuar? [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}]')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'{vermelho}Tente novamente!{FIM_COR} Quer continuar? '
                              f'[{azul}S{FIM_COR}/{vermelho}N{FIM_COR}]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'A lista de todos os numeros digitados é: {lista_numeros}')
print(f'A lista de todos os numeros PARE é: {lista_numeros_pares}')
print(f'A lista de todos os numeros IMPARES é: {lista_numeros_impares}')
