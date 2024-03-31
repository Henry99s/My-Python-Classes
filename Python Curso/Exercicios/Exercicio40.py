from time import sleep

print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Base de Conversão____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Nome do aluno
aluno = str(input('Qual o nome do aluno? '))

# Notas do aluno
nota1 = float(input(f'Digite a nota do aluno/a \033[1;32m{aluno}\033[m, em Matematica: '))
nota2 = float(input(f'Digite a nota do aluno/a \033[1;32m{aluno}\033[m, em Portugues: '))

# Calculo da media
calculo_media = (nota1 + nota2) / 2

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado
if calculo_media < 5.0:
    print(f'A media do aluno/a \033[1;32m{aluno}\033[m, foi: \033[1;31m{calculo_media}\033[m')
    print(f'O aluno/a \033[1;32m{aluno}\033[m, foi \033[1;31mREPROVADO!\033[m')

elif calculo_media <= 6.9:
    print(f'A media do aluno/a \033[1;32m{aluno}\033[m, foi: \033[1;33m{calculo_media}\033[m')
    print(f'O aluno/a \033[1;32m{aluno}\033[m, esta de \033[1;33mRECUPERAÇÃO!\033[m')

elif calculo_media >= 7.0:
    print(f'A media do aluno/a \033[1;32m{aluno}\033[m, foi: \033[1;32m{calculo_media}\033[m')
    print(f'O aluno/a \033[1;32m{aluno}\033[m, foi \033[1;32mAPROVADO!\033[m')
