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
for c in range(5):
    contador += 1
    numero = int(input(f'Digite o {verde}{contador}º{FIM_COR} numero: '))
    lista_numeros.append(numero)

print(f'Os Valores digitados em ordem {azul_underline}crescente{FIM_COR} são:')
for numero in sorted(lista_numeros):
    print(numero, end=' ')

