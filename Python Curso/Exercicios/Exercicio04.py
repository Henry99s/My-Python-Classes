# Descobrindo um variavel
n = input('Digite algo: ')

# Descobrir o que o "n" é
print('É aplha-numerico? {}'.format(n.isalnum()))
print('É alfabetico? {}'.format(n.isalpha()))
print('É ASCII? {}'.format(n.isascii()))
print('É Digito? {}'.format(n.isdigit()))
print('Esta tudo em minusculo? {}'.format(n.islower()))
print('É decimal? {}'.format(n.isdecimal()))
print('É identificador Python? {}'.format(n.isidentifier()))
print('É numerico? {}'.format(n.isnumeric()))
print('É replicável? {}'.format(n.isprintable()))
print('So tem espaço? {}'.format(n.isspace()))
print('Esta capítalizada? {}'.format(n.istitle()))
