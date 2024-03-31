# Cores
vermelho = '\033[1;31m'
FIM_COR = '\033[m'


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True

            break
        else:
            print(f"{vermelho}ERRO! Digite um numero inteiro valido{FIM_COR}")
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
