from time import sleep

print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Comparação De Dois Numeros____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Escolhendo os dois numeros
primeiro_numero = float(input('Escreva o primeiro numero para comparação: '))
segundo_numero = float(input('Escreva o segundo numero para comparação: '))

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado
if primeiro_numero > segundo_numero:
    print('O \033[32mprimeiro numero\033[m é maior!')

elif segundo_numero > primeiro_numero:
    print('O \033[32msegundo numero\033[m é maior!')

elif primeiro_numero == segundo_numero:
    print(f'Não existe valor maior, os dois são \033[32miguais\033[m!')
