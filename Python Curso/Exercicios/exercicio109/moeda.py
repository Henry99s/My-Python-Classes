def aumentar(valor=0, porcentagem=0, formatado=False):
    aumento = valor + (valor * porcentagem / 100)
    if formatado:
        return monetario(aumento)
    else:
        return aumento


def diminuir(valor=0, porcentagem=0, formatado=False):
    diminui = valor - (valor * porcentagem / 100)
    if formatado:
        return monetario(diminui)
    else:
        return diminui


def dobro(valor=0, formatado=False):
    resultado = valor * 2
    if formatado:
        return monetario(resultado)
    else:
        return resultado


def metade(valor=0, formatado=False):
    resultado = valor / 2
    if formatado:
        return monetario(resultado)
    else:
        return resultado


def monetario(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
