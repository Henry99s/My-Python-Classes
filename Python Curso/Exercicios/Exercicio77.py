# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}{"(_____Contado Vogais em Tupla____)":^20}{FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
    vogais = [letra.lower() for letra in palavra if letra.lower() in 'aeiou']
    print(f'Na palavra {azul}{palavra.upper()}{FIM_COR}, temos {azul}{" ".join(vogais)}{FIM_COR}')

