print('=====Calculo de Porcentagem de Desconto====')

# Preco do produto, desconto, e calculo do desconto
valor_produto = float(input('Quanto custa o produto: R$'))
desconto = 5 * valor_produto / 100
novo_valor = valor_produto - desconto

# Resultado
print('Aplicando 5% de desconto, o produto ficaria por: R${:.2f}'.format(novo_valor))
