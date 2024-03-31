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
print(f'{vermelho_fundo_preto}(_____Soma Dos Numeros Pares____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------
# Dado o primeiro valor
soma = 0

# Criando uma estrutura de respetição para escolher 3 numeros inteiros
for numeros in range(1, 7):
    numeros_inteiros = int(input(f'Digite o {azul_marinho}{numeros}º{FIM_COR} numero inteiro: '))
    if numeros_inteiros % 2 == 0:   # Encontrando os numeros pares
        soma += numeros_inteiros    # Soma dos numeros pares

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado
print(f'A {azul}SOMA{FIM_COR} de todos os numeros {azul_underline}PARES{FIM_COR} é: {verde}{soma}{FIM_COR}')
