def aumentar(valor=0, porcentagem=0, formatado=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o valor que se quer reajustar.
    :param porcentagem: qual a porcentagem do aumento.
    :param formatado: o resultado será formatado ou não.
    :return: retorna o valor reajustado, com ou sem formatação.
    """
    aumento = valor + (valor * porcentagem / 100)
    if formatado:
        return monetario(aumento)
    else:
        return aumento


def diminuir(valor=0, porcentagem=0, formatado=False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o valor que se quer reajustar.
    :param porcentagem: qual a porcentagem da redução.
    :param formatado: o resultado será formatado ou não.
    :return: retorna o valor reajustado, com ou sem formatação.
    """
    diminui = valor - (valor * porcentagem / 100)
    if formatado:
        return monetario(diminui)
    else:
        return diminui


def dobro(valor=0, formatado=False):
    """
    -> Calcular o Dobro de um determinado valor.
    :param valor: o valor que se quer reajustar.
    :param formatado: o resultado será formatado ou não.
    :return: retorna o valor reajustado, com ou sem formatação.
    """
    resultado = valor * 2
    if formatado:
        return monetario(resultado)
    else:
        return resultado


def metade(valor=0, formatado=False):
    """
    -> Calcular a metade de um determinado valor.
    :param valor: o valor que se quer reajustar.
    :param formatado: o resultado será formatado ou não.
    :return: retorna o valor reajustado, com ou sem formatação.
    """
    resultado = valor / 2
    if formatado:
        return monetario(resultado)
    else:
        return resultado


def monetario(valor=0, moeda='R$'):
    """
    -> Trasnforma o valor comum em um valor formatado em uma moeda desejada.
    :param valor: o valor que se quer formatar.
    :param moeda: a moeda desejada para a formatação.
    :return: retorna o valor formatado na moeda desejada.
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, porcentagem_aumento=0, porcentagem_reducao=0):
    """
    -> Cria uma tabela com as informações do preço analisado, seu dobro, sua metade, porcentagem de aumento e
    porcentagem de redução.
    :param valor: o valor desejado para o resumo.
    :param porcentagem_aumento: qual a porcentagem de aumento do valor.
    :param porcentagem_reducao: qual a porcentagem de redução do calor.
    :return: retorna uma tabela com todas as informações desejadas do valor fornecido.
    """
    print(f'-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'-' * 30)
    print(f'Preço analisado: \t{monetario(valor)}')
    print(f'Dobro do preco: \t{dobro(valor, True)}')
    print(f'Metade do preco: \t{metade(valor, True)}')
    print(f'{porcentagem_aumento}% de aumento: \t{aumentar(valor, porcentagem_aumento, True)}')
    print(f'{porcentagem_reducao}% de reducao: \t{diminuir(valor, porcentagem_reducao, True)}')
    print(f'-' * 30)
