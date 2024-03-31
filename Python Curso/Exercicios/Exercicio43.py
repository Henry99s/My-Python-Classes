from time import sleep

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Calculo de IMC____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Dados do usuario
nome = str(input('Qual o seu nome? ')).capitalize().strip()
idade = int(input('Qual a sua idade? '))
altura = float(input('Qual a sua altura em Metros? '))
peso = float(input('Qual o seu peso em Kg? '))

# Transformando a altura do usuario em metros, caso tenha colocado altura em centimetros.
if altura.is_integer():
        altura = altura / 100

# Calculo do IMC
imc = peso / (altura ** 2)

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado
if imc < 18.5:
    print(f'Ola {azul_marinho}{nome}{FIM_COR}, seu IMC é de {vermelho}{imc:.1f}{FIM_COR}, '
          f'você está {vermelho}ABAIXO DO PESO{FIM_COR}')

elif 18.5 <= imc < 25:
    print(f'Ola {azul_marinho}{nome}{FIM_COR}, seu IMC é de {azul}{imc:.1f}{FIM_COR}, '
          f'você está no {azul}PESO IDEIAL{FIM_COR}')

elif 25 <= imc < 30:
    print(f'Ola {azul_marinho}{nome}{FIM_COR}, seu IMC é de {azul}{imc:.1f}{FIM_COR}, '
          f'você está com {azul}SOBREPESO{FIM_COR}')

elif 30 <= imc < 40:
    print(f'Ola {azul_marinho}{nome}{FIM_COR}, seu IMC é de {vermelho}{imc:.1f}{FIM_COR}, '
          f'você está com {vermelho}OBESIDADE{FIM_COR}')

elif imc > 40:
    print(f'Ola {azul_marinho}{nome}{FIM_COR}, seu IMC é de {vermelho}{imc:.1f}{FIM_COR}, '
          f'você está com {vermelho}OBESIDADE MÓRBIDA{FIM_COR}')
