from time import sleep


# Cores
c = ('\033[m',          # 0 - sem cor
     '\033[1;34m',      # 1 - azul
     '\033[4;34m',      # 2 - azul com underline
     '\033[1;31m',      # 3 - vermelho
     '\033[1;31;40m',   # 4 - vermelho com fundo preto
     '\033[1;32m',      # 5 - verde
     '\033[7;40m'       # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \' {com}\'', 6)
    print(c[4])
    help(com)
    print(c[0])
    sleep(1.5)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATE LOGO!', 3)
