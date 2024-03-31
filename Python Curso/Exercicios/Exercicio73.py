# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Tuplas com Times de Futebol____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

brasileirao = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Athletico-PR', 'Fluminense',
               'Fortaleza', 'São Paulo', 'Internacional', 'Cuiabá', 'Corinthians', 'Santos', 'Bahia', 'Vasco',
               'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

print(f'{verde}={FIM_COR}' * 40)
print(f'A tabela do Brasileirão do {azul}1º{FIM_COR} colocado ao {azul}20º{FIM_COR} colococado é: \n{brasileirao}')

print(f'{verde}={FIM_COR}' * 40)
print(f'Os {azul}5{FIM_COR} primeiro colocados são {brasileirao[:5]}')

print(f'{verde}={FIM_COR}' * 40)
print(f'Os ultimos {azul}4{FIM_COR} colococados da tabela são: {brasileirao[-4:]}')

print(f'{verde}={FIM_COR}' * 40)
print(f'A lista do Brasileirão em {azul}ordem alfabética{FIM_COR} é: \n{sorted(brasileirao)}')

print(f'{verde}={FIM_COR}' * 40)
print(f'O {azul}Fortaleza{FIM_COR} esta na {azul}{brasileirao.index("Fortaleza") + 1}º{FIM_COR} colocação')
