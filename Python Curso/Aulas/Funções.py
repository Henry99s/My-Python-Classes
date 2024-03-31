def mensagem(msg):
    print('_' * 30)
    print(msg)
    print('_' * 30)


mensagem('     SISTEMA DE ALUNOS     ')


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


def contador(* num):
    print(num)


# Cria Tuplas
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def somas(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f'Somando os valores {numeros} temos {s}')


somas(5, 2)
somas(2, 9, 4)
