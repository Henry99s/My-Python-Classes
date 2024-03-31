print('=====Separando o Primero e Ultimo Nome de uma Pessoa=====')

# Escolhendo um Nome
nome = input('Digite seu nome: ').strip()

# Dividindo a Frase
dividir_frase = nome.split()

# Achando o primeiro nome
primeiro_nome = dividir_frase[0]
# Achando o ultimo nome
ultimo_nome = dividir_frase[-1]

# Resultado
print(f"Seu primeiro nome é {primeiro_nome}")
print(f"Seu ultimo nome é {ultimo_nome}")
