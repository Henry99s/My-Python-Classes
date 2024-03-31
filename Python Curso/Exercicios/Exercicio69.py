# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
roxo = '\033[1;35m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Analisando Dados de Grupo____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

participante = 0
maior_idade = 0
homens = 0
mulher_menos_vinte = 0

while True:
    participante += 1
    print('_' * 40)
    print(f'CADASTRE A {participante}º PESSOA')
    print('_' * 40)

    idade = int(input(f'Qual a idade do {azul}{participante}º{FIM_COR} participante: '))
    while idade < 1 or idade > 150:
        print('ERRO! Tente novamente')
        idade = int(input(f'Qual a idade do {azul}{participante}º{FIM_COR} participante: '))

    sexo = str(input(f'Qual o sexo do {azul}{participante}º{FIM_COR} '
                     f'participante: [{azul}M{FIM_COR}/{roxo}F{FIM_COR}] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('ERRO! Tente novamente')
        sexo = str(input(f'Qual o sexo do {azul}{participante}º{FIM_COR} '
                         f'participante: [{azul}M{FIM_COR}/{roxo}F{FIM_COR}] ')).strip().upper()[0]

    if idade > 18:
        maior_idade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulher_menos_vinte += 1

    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('ERRO! Tente novamente')
        continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

    if continuar == 'N':
        print(f'Foram cadastradas {azul_underline}{maior_idade}{FIM_COR} pessoas acima de {verde}18{FIM_COR} anos.')
        print(f'Foram cadastrados {azul_underline}{homens}{FIM_COR} homens.')
        print(f'Foram cadastradas {azul_underline}{mulher_menos_vinte}{FIM_COR} '
              f'mulheres com menos de {verde}20{FIM_COR} anos.')
        break
