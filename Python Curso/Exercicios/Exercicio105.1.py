# Cores
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Analisando e Gerando Dicionarios____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)


def notas(* valores, sit=False):
    """
    -> Função ára analisar notas e situaçãoes de vários alunos.
    :param sit: valor opcianal, indicando se deve ou não adicionar a sitiação
    :param valores: uma ou mais notas dos alunos (aceita vários valores).
    :return: dícionario com várias informações sobre a situação da turma.
    """

    lista_notas = []
    aluno = 0
    total_media = 0

    for nota in valores:
        aluno += 1
        total_media += nota
        lista_notas.append(nota)

    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media = total_media / aluno

    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif media >= 5:
            situacao = 'RAZOAVEL'
        else:
            situacao = 'RUIM'

        return {'Quantidade_Notas': aluno, 'Maior_Nota': maior_nota, 'Menor_Nota': menor_nota, 'Media': media,
                'Situação': situacao}
    else:
        return {'Quantidade_Notas': aluno, 'Maior_Nota': maior_nota, 'Menor_Nota': menor_nota, 'Media': media}


print(notas(3.5, 2, 6.5, 2, 7, 4, sit=True))
help(notas)
