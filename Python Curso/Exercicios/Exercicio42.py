from time import sleep

# Cores
azul = '\033[1;34m'
azul_marinho = '\033[1;36m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Descobrindo se as Tres Retas Formam um Triangulo____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Escolhendo o Valor das Tres Retas.
reta1 = int(input('Qual o comprimento da primeira reta ? '))
reta2 = int(input('Qual o comprimento da segunda reta ? '))
reta3 = int(input('Qual o comprimento da terceira reta ? '))

# Descobrindo Qual é a Reta Maior e Quais as Menores.
if reta1 >= reta2 and reta1 >= reta3:
    maior = reta1
    menor1 = reta2
    menor2 = reta3

elif reta2 >= reta1 and reta2 >= reta3:
    maior = reta2
    menor1 = reta1
    menor2 = reta3

else:
    maior = reta3
    menor1 = reta1
    menor2 = reta2

# Calculando as duas retas menores. Se o resultado for Maior que a Reta maior, entao podem formar um triangulo.
soma_menores = menor1 + menor2

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado se pode formar triangulo e Qual e o tipo de triangulo
if soma_menores > maior:
    print(f'{azul_marinho}As tres retas{FIM_COR} {verde}PODEM{FIM_COR} {azul_marinho}formar um triagulo!{FIM_COR}')

    if reta1 == reta2 == reta3:
        print(f'Este triangulo é {azul}EQUILÁTERO{FIM_COR}.(Todos os lados são {verde}IGUAIS{FIM_COR}.)')

    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print(f'Este triangulo é {azul}ISÓSCELES{FIM_COR}.(Apenas dois lados são {verde}IGUAIS{FIM_COR}.)')

    else:
        print(f'Este triangulo é {azul}ESCALENO{FIM_COR}.(Todos os lados são {verde}DIFERENTES{FIM_COR}.)')

else:
    print('\033[1;31mAs tres retas NAO podem formar um triangulo!')
