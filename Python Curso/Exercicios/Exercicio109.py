from exercicio109 import moeda

# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Formatando Moedas em Python 2____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

p = float(input('Digite o preço: R$'))

print(f'A metade de {azul}{moeda.monetario(p)}{FIM_COR} é {azul_underline}{moeda.metade(p, True)}{FIM_COR}')
print(f'O dobro de {azul}{moeda.monetario(p)}{FIM_COR} é {azul_underline}{moeda.dobro(p, True)}{FIM_COR}')
print(f'Aumentado {azul}10%{FIM_COR}, temos {azul_underline}{moeda.aumentar(p, 10, True)}{FIM_COR}')
print(f'Reduzindo {azul}13%{FIM_COR}, temos {azul_underline}{moeda.diminuir(p,13, True)}{FIM_COR}')
