from exercicio115 import cadastro, interface
from exercicio115 import arquivo
from time import sleep

# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
FIM_COR = '\033[m'


def sistema():
    interface.menu()
    while True:
        try:
            print('_' * 42)
            escolha = int(input(f'{amarelo}Sua Opção:{FIM_COR} '))
            print('_' * 42)

            if escolha == 1:
                interface.cabecalho('Opção 1')
                cadastro.listar()
                interface.menu()

            elif escolha == 2:
                interface.cabecalho('Opção 2')
                sleep(1)
                cadastro.mostrar_pessoas_cadastradas()
                interface.menu()

            elif escolha == 3:
                interface.cabecalho('Opção 3')
                nome_arquivo = str(input('Qual o nome do arquivo? '))
                if arquivo.arquivo_existe(nome_arquivo):
                    print(f'{verde}Arquivo encontrado com sucesso!{FIM_COR}')
                else:
                    print(f'{vermelho}Arquivo não encontrado!{FIM_COR}')
                interface.menu()

            elif escolha == 4:
                interface.cabecalho('Opção 4')
                nome_novo_arquivo = str(input('Digite o nome do novo arquivo: '))
                arquivo.criar_arquivo(nome_novo_arquivo)
                interface.menu()

            elif escolha == 5:
                interface.cabecalho('Opção 5')
                analisar_arquivo = str(input('Qual arquivo quer ler? '))
                arquivo.ler_arquivo(analisar_arquivo)
                interface.menu()

            elif escolha == 6:
                interface.cabecalho('Opção 6')
                print(f'{azul}Terminando o sistema. Obrigado!{FIM_COR}')
                sleep(2)
                break

            elif escolha is not int:
                print(f'{vermelho}Erro! Digite um numero.{FIM_COR}')

            else:
                print(f'{vermelho}Erro! escolha as opções entre 1 á 3.{FIM_COR}')

        except ValueError:
            print(f'{vermelho}Erro! escolha um numero.{FIM_COR}')
