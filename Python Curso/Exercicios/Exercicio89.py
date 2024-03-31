# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Boletim Com Listas____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

listas_notas_alunos = []


def boletim():
    nome = str(input('Nome: ')).capitalize().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    return {'nome': nome, 'nota1': nota_1, 'nota2': nota_2, 'media': media}


while True:
    alunos = boletim()
    listas_notas_alunos.append(alunos)

    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente novamente! Quer continuar? '
                              f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).upper().strip()

    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"NOME":<20} {"MEDIA":>7}')
print('_' * 32)
for aluno in listas_notas_alunos:
    if aluno["media"] > 5:
        print(f'{verde}{aluno["nome"]:<20}{FIM_COR} {azul}{aluno["media"]:>7.1f}{FIM_COR}')

    elif aluno["media"] < 5:
        print(f'{verde}{aluno["nome"]:<20}{FIM_COR} {vermelho}{aluno["media"]:>7.1f}{FIM_COR}')
print('_' * 32)

while True:
    mostrar = str(input('Quer mostrar as notas de qual aluno: ')).capitalize().strip()
    aluno_encontrado = False

    for aluno in listas_notas_alunos:
        if mostrar == aluno["nome"]:
            aluno_encontrado = True
            print(f'As notas de {azul}{aluno["nome"]}{FIM_COR} '
                  f'são {azul_underline}Nota 1:{FIM_COR} {verde}{aluno["nota1"]}{FIM_COR}, '
                  f'{azul_underline}Nota 2:{FIM_COR} {verde}{aluno["nota2"]}{FIM_COR}')

    if not aluno_encontrado:
        print(f'{vermelho}Este aluno não existe! Tente novamente.{FIM_COR}')

    continuar = str(input(f'Quer continuar? [{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'Tente novamente! Quer continuar? '
                              f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).upper().strip()

    if continuar == 'N':
        break
