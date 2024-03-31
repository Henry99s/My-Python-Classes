from time import sleep

print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Base de Conversão____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Estilo Cores
verde = '\033[32m'
final = '\033[m'

# Escolhendo o numero inteiro
numero_inteiro = int(input('Para a conversão, digite um numero inteiro: '))

# Escolhendo o metodo
escolha = int(input('''Agora escolha o metodo de conversão: 
[ 1 ] para Binario 
[ 2 ] para Octal 
[ 3 ] para Hexadecimal 
Sua escolha: '''))

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Fazendo os calculos e resultado
if escolha == 1:
    numero_inteiro1 = bin(numero_inteiro)
    print(f'O numero {verde}{numero_inteiro}{final} transformado em Binario é: {verde}{numero_inteiro1[2::]}{final}')

elif escolha == 2:
    numero_inteiro2 = oct(numero_inteiro)
    print(f'O numero {verde}{numero_inteiro}{final} transformado em Octal é: {verde}{numero_inteiro2[2::]}{final}')

elif escolha == 3:
    numero_inteiro3 = hex(numero_inteiro)
    print(f'O numero {verde}{numero_inteiro}{final} transformado em Hexadecimal é: {verde}{numero_inteiro3[2::]}{final}')

else:
    print('\033[1;41m---ERRO---')
