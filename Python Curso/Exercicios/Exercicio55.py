# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Grupo de Maioridade____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Criando uma lista para a variavel peso
pesos = []

# Lendo o Peso de cada participante
for pessoas in range(1, 6):
    pessoa = int(input(f'Qual o peso do {verde}{pessoas}º{FIM_COR} participante em Kg? '))
    pesos.append(pessoa)    # Adicionando o peso do participante a lista de Pesos

menor_peso = min(pesos)  # Pegando o menor valor da lista de Pesos
maior_peso = max(pesos)  # Pegando o maior valor da lista de Pesos

# Resultado
print(f'A pessoa com o menor peso tem {azul}{menor_peso}Kg{FIM_COR}')
print(f'A pessoa com o maior peso tem {azul}{maior_peso}Kg{FIM_COR}')
