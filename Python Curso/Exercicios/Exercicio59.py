from time import sleep

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
print(f'{vermelho_fundo_preto}(_____Criando um Menu____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

valor1 = float(input(f'Digite o {azul}primeiro{FIM_COR} valor: '))
valor2 = float(input(f'Digite o {azul}segundo{FIM_COR} valor: '))

while True:
    escolha = int(input(f"""\nEscolha o que gostaria de fazer com os dois valores fornecidos.
        [ {verde}1{FIM_COR} ] Somar
        [ {verde}2{FIM_COR} ] Multiplicar
        [ {verde}3{FIM_COR} ] Qual o maior valor
        [ {verde}4{FIM_COR} ] Escolher novos valores
        [ {verde}5{FIM_COR} ] Sair do programa!
        """))

    if escolha == 1:
        soma = valor1 + valor2
        print(f'A soma dos valores é {azul_underline}{soma}{FIM_COR}')
        print(f'\n{azul_marinho}Gostaia de fazer algo mais?{FIM_COR}')

    elif escolha == 2:
        multiplicar = valor1 * valor2
        print(f'A multiplicação dos valores é {azul_underline}{multiplicar}{FIM_COR}')
        print(f'\n{azul_marinho}Gostaia de fazer algo mais?{FIM_COR}')

    elif escolha == 3:
        if valor1 > valor2:
            print(f'O {azul_underline}PRIMEIRO{FIM_COR} valor é {verde}MAIOR!{FIM_COR}')
        elif valor1 == valor2:
            print(f'Os valores são {azul_underline}IGUAIS!{FIM_COR}')
        else:
            print(f'O {azul_underline}SEGUNDO{FIM_COR} valor é {verde}MAIOR!{FIM_COR}')

        print(f'\n{azul_marinho}Gostaia de fazer algo mais?{FIM_COR}')

    elif escolha == 4:
        valor1 = float(input(f'Digite um novo {azul}primeiro{FIM_COR} valor: '))
        valor2 = float(input(f'Digite um novo {azul}segundo{FIM_COR} valor: '))
        print(f'\nAgora o primeiro valor é {verde}{valor1}{FIM_COR} e o segundo valor é {verde}{valor2}{FIM_COR}')
        print(f'\n{azul_marinho}O que gostaia de fazer com os novos valores?{FIM_COR}')

    elif escolha == 5:
        print(f'{azul_marinho}Muito obrigado, até aproxima!{FIM_COR}')
        break

    else:
        print(f'{vermelho}Opção invalida!!!{FIM_COR}')
        print(f'{vermelho}Por favor, digite um valor valido!{FIM_COR}')

    sleep(1)
