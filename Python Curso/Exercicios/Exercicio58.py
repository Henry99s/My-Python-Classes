from random import randrange

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
print(f'{vermelho_fundo_preto}(_____Analisador de Sexo____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

numero = int(randrange(0, 10))  # Maquina escolhendo um numero de 0 á 10.
escolha = int(input('Em qual numero eu pensei? '))  # Jogador advinhando.
vezes_escolha = 1   # Quantas vezes precisou advinhar, para acertar o valor escolhido pela maquina.

# Fazendo jogador escolher um valor, até acertar
while escolha != numero:
    print(f'Que pena! Eu nao pensei nesse numero. {vermelho}TENTE NOVAMENTE!{FIM_COR}')
    escolha = int(input('Em qual numero eu pensei? '))
    vezes_escolha += 1  # adicionando cada vez que precisou advinhar o numero na variavel "vezes_escolha"

# Resultado
if escolha == numero:
    print(f'\n{azul}PARABENS!{FIM_COR} Voce Acertou o Numero!')
    print(f'O Numero escolhido foi {azul_underline}{numero}{FIM_COR}')
    print(f'Voce precisou de {azul_marinho}{vezes_escolha}{FIM_COR} tentativas para ganhar!')
