print('=====Brincando com Strings=====')

# Digite o Nome completo
nome = str(input('Digite seu nome completo: ')).strip()

# Codigos
print('Seu nome em maiúsculas é {}'.format(nome.upper()))  # transformado tudo em maiúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))  # transformando tudo em minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # Contando o numero de letras do nome completo
primero = nome.split()  # Dividindo as palavras do nome
print('Seu primeiro nome e {}, e tem {} letras'.format(primero[0], len(primero[0])))  # Contando o numero de letras do primeiro nome
