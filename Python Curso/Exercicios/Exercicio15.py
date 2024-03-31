print('=====Calculo do Aluguel de Carros=====')

# Informacoes sobre o aluguel do Carro.
dias_alugados = int(input('Quantos dias o carro foi alugado? '))
km_percorridos = float(input('Quantos km foram percorridos com o carro? '))

# Calculo do Aluguel sendo que o custo do aluguel é R$60 por dia e R$0,15 por Km rodado.
preco_pagar = (60 * dias_alugados) + (0.15 * km_percorridos)

# Valor final do Aluguel
print('O valor total a pagar é de R${0:.2f}'.format(preco_pagar))
