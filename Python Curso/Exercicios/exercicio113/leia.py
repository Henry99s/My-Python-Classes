# Cores
vermelho = '\033[1;31m'
FIM_COR = '\033[m'


def leiaint(msg):
    while True:
        valor = input(msg)
        try:
            valor = int(valor)
            return valor

        except KeyboardInterrupt:
            print(f'{vermelho}O usuario não informou nenhum dado!{FIM_COR}')

        except (ValueError, TypeError):
            print(f"{vermelho}ERRO! Digite um numero Inteiro valido.{FIM_COR}")


def leiafloat(msg):
    while True:
        valor = input(msg)
        try:
            valor = float(valor)
            return valor

        except KeyboardInterrupt:
            print(f'{vermelho}O usuario não informou nenhum dado!{FIM_COR}')

        except (ValueError, TypeError):
            print(f"{vermelho}ERRO! Digite um numero Inteiro valido.{FIM_COR}")
