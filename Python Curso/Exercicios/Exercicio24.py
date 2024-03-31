print('=====Lendo o Nome de Uma Cidade=====')

# Escolhendo uma cidade
cidade = str(input('Escreva o nome de uma cidade: ')).strip()
cidade1 = cidade.upper()

# Dividindo a frase e descobrindo se começa com as palavra SANTO
dividindo = cidade1.split()
santo = 'SANTO' in dividindo[0]

# descobrindo se começa com a palavra SANTO ou não
print('A cidade escolhida comeca com a a palavra SANTO? {}'.format(santo))
