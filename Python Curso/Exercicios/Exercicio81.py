# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Extraindo Dados De Uma Lista____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_numeros = []
contador = 0
while True:
    contador += 1
    numero = int(input(f'Digite o {verde}{contador}º{FIM_COR} valor: '))
    lista_numeros.append(numero)
    continuar = str(input(f'Quer continuar? [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}]')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'{vermelho}Tente novamente!{FIM_COR} Quer continuar? '
                              f'[{azul}S{FIM_COR}/{vermelho}N{FIM_COR}]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Foram digitados {azul_underline}{contador}{FIM_COR} valores')

lista_numeros.sort(reverse=True)
print(f'A lista dos valores em ordem {verde}DECRECENTE{FIM_COR} é: {azul}{lista_numeros}{FIM_COR}')

if 5 in lista_numeros:
    print(f'O numero 5 está na lista e na posição {azul_underline}{lista_numeros.index(5)}{FIM_COR}')
else:
    print(f'{vermelho}Não foi adicionado o numero 5 a lista!{FIM_COR}')
