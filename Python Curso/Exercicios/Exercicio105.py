# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Analisando e Gerando Dicionarios____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)


def notas():
    lista_notas = []
    aluno = 1
    total_media = 0
    while True:
        nota = int(input(f'Qual a nota do {azul}{aluno}º{FIM_COR} aluno? '))
        total_media += nota
        aluno += 1
        lista_notas.append(nota)
        continuar = str(input(f'Quer continuar?[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

        while continuar != 'S' and continuar != 'N':
            continuar = str(input(f'ERRO! Tente Novamente. Quer continuar?'
                                  f'[{verde}S{FIM_COR}/{vermelho}N{FIM_COR}] ')).strip().upper()[0]

        if continuar == 'N':
            break

    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media = total_media / (aluno - 1)

    return{'Quantidade_Notas': aluno - 1, 'Maior_Nota': maior_nota, 'Menor_Nota': menor_nota, 'Media': media}


print(notas())
