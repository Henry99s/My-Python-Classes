# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Calculo de Fatorial____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------


def calculo_fatorial(numero):
    if numero < 0:
        return "Fatorial não definido para números negativos!"

    elif numero == 1:
        return 1

    else:
        fatorial = 1
        i = 1
        while i <= numero:
            fatorial *= i
            i += 1
        return fatorial


numero = int(input('Digite um numero para saber seu fatorial: '))
resultado = calculo_fatorial(numero)
print(f'O fatorial do numero {numero} é {resultado}.')
