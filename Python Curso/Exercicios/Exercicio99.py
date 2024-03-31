from time import sleep


def maior(* numeros):
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.3)

    if len(numeros) >= 1:
        print(f'Foram informados {len(numeros)}, e o numero maior e {max(numeros)}')

    elif len(numeros) == 0:
        print('Nao foram informados nenhum valor!')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

