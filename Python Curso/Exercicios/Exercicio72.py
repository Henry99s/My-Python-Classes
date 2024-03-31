# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Numero por Extenso____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

escolha = int(input('Digite um numero de 0 a 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Tente novamente! Digite um numero de 0 a 20: '))

print(f'Voce escolheu {azul}{contagem[escolha]}{FIM_COR}')
