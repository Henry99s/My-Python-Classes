# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Valores Únicos Em Uma Lista____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

lista_numeros = []
contador = 0
while True:
    contador += 1
    numero = int(input(f'Digite o {verde}{contador}º{FIM_COR} numero: '))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
    else:
        print(f'{vermelho}Número repetido!{FIM_COR} Não sera adicionado á lista.')

    continuar = str(input(f'Quer continuar? [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'{vermelho}Tente novamente!{FIM_COR} '
                              f'Quer continuar? [{azul}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    if continuar == 'N':
        break
lista_numeros.sort()
print(f'Os Valores digitados em ordem {azul_underline}crescente{FIM_COR} são:')
print(lista_numeros)
