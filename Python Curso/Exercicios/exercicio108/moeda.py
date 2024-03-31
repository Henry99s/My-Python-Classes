def aumentar(valor=0, porcentagem=0):
    aumento = valor + (valor * porcentagem / 100)
    return aumento


def diminuir(valor=0, porcentagem=0):
    diminui = valor - (valor * porcentagem / 100)
    return diminui


def dobro(valor=0):
    resultado = valor * 2
    return resultado


def metade(valor=0):
    resultado = valor / 2
    return resultado


def monetario(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
