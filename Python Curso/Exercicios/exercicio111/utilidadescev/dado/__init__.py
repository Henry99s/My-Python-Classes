# Cores
vermelho = '\033[1;31m'
FIM_COR = '\033[m'


def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{vermelho}Erro: \"{entrada}\" é um preço inválido!{FIM_COR}')
        else:
            valido = True
            return float(entrada)
