from exercicio107 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentado 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p,13)}')
