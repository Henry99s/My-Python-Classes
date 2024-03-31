from time import sleep


# Criando uma função para contagem personalizada.
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        sleep(0.3)
        c += p
    print('FIM!')


# Iniciando uma contagem de 2 ate 10, pulando de 2 em 2.
contador(2, 10, 2)

help(contador)
help(sleep)


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra p resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()

help(somar)


def teste(b):
    global a

    a = 8
    b += 4
    c = 2
    print(f'A, dentro vale {a}')
    print(f'B, dentro vale {b}')
    print(f'c, dentro cale {c}')


a = 5
teste(a)
print(f'A, fora vale {a}')


def somar1(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar1(3, 2, 5)
r2 = somar1(1, 7)
r3 = somar1(4)

print(f'Meus calculos deram {r1}, {r2} e {r3}.')
