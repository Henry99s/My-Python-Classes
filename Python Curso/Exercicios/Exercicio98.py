from time import sleep


def contador():
    mais = 0
    for con1 in range(10):
        mais += 1
        sleep(0.3)
        print(mais, end=' ')
    print('FIM!')


def contador1():
    for con2 in range(10, -1, -2):
        sleep(0.4)
        print(con2, end=' ')
    print('FIM!')


def contador2():
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    if inicio > fim:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for con3 in range(inicio, fim - 1, -passo):
            sleep(0.4)
            print(con3, end=' ')
        print('FIM!')

    else:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for con3 in range(inicio, fim + 1, passo):
            sleep(0.4)
            print(con3, end=' ')
        print('FIM!')


print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1\r')
contador()

print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2\r')
contador1()

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador2()
