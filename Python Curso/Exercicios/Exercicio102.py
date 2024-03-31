def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de numero n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input("Digite um numero: "))
print(fatorial(n, show=True))
