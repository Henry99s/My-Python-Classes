# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Dicionario em Python____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

aluno = dict()

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input('Media: '))

print(f'Nome do aluno é {azul}{aluno["nome"]}{FIM_COR}')

if aluno["media"] < 5:
    print(f'Media do aluno é {vermelho}{aluno["media"]}{FIM_COR}')
    print(f'Situacao do aluno é: {vermelho}REPROVADO!{FIM_COR}')
elif 5 <= aluno["media"] < 7:
    print(f'Media do aluno é {azul_underline}{aluno["media"]}{FIM_COR}')
    print(f'Situacao do aluno é : {verde}RECUPERAÇÃO!{FIM_COR}')
else:
    print(f'Media do aluno é {azul_underline}{aluno["media"]}{FIM_COR}')
    print(f'Situacao do aluno é : {azul_underline}APROVADO!{FIM_COR}')
