print('-=-' * 20)
print('(____Descobrindo Qual é o Numero Maior____)')
print('-=-' * 20)

# Escolhendo os tres numeros
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))

# Iniciando a Variavel com o Menor e Maior Numero
maior = numero1
menor = numero1

# Camparando com os Numeros 2 e 3 para Descobrir Quem e o Maior é Quem é o Menor
if numero2 > maior:
    maior = numero2

if numero2 < menor:
    menor = numero2

if numero3 > maior:
    maior = numero3

if numero3 < menor:
    menor = numero3

# Resultado
print(f'O numero menor é {menor}!')
print(f'O numero maior é {maior}!')
