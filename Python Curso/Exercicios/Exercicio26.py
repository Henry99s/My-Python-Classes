print('=====Brincando com uma String=====')

# Escolhendo uma Frase
frase = str(input('Digite uma frase: ')).strip()

# Transformando todas as letras em maiusculo
frase1 = frase.upper()

# Contando Quantas letras 'A' aparecem na frase
a = frase1.count('A')

# Quando a letra 'A' aparece a primeira vez
primeira = frase1.find('A')+1

# Quando a letra 'A' aparece uma ultima vez
ultima = frase1.rfind('A')+1

# Resultado
print(f"Nesta frase, quantas vezes aparece a letra 'A'? Ela aparece {a} vezes.")
print(f"Em que posição aparece a letra 'A' aparece pela primeira vez? Na posição {primeira}.")
print(f"Em que posição aparece a letra 'A' pela ultima vez? Ela aparece na posição {ultima} pela ultima vez.")
