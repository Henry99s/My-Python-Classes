print('=====Descobrindo se tem Silva no nome=====')

# Escolhendo um nome
nome = str(input('Digite um nome completo: ')).strip()

# Encontrando a palavra SILVA
silva = 'SILVA' in nome.upper()

# Resultado
print(f"Esse nome contem a palavra SILVA? {silva}")
