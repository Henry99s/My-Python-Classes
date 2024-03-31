lista = [123, 3142345, 521234, 52341, 124, 524, 534, 4, 43, 23, 65, 762, 32, 6, 136, 6, 246, 6, 63,
         5, 35, 6, 37, 357, 51, 4, 45]
print(lista)

lista.sort()
print(lista)

num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)

num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 5')

num2 = [3, 4, 32, 2, 42, 1, 3, 242, 55]
num.extend(num2)
print(num)

for c, v in enumerate(num):
    print(f'Na posicao {c} encontrei o valor {v}!')

for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))

print(num)
print(f'Essa lista tem {len(num)} elementos.')
