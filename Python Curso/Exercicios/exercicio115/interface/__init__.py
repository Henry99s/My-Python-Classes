
# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
FIM_COR = '\033[m'


def cabecalho(titulo):
    print('=' * 42)
    print(titulo.center(42))
    print('=' * 42)


def menu():
    cabecalho('MENU PRICIPAL')
    print(f'''
        {verde}1{FIM_COR} - {azul}Cadastrar Nova Pessoa{FIM_COR}
        {verde}2{FIM_COR} - {azul}Ver Pessoas Cadastradas{FIM_COR}
        {verde}3{FIM_COR} - {azul}Ver se Arquivo Existe{FIM_COR}
        {verde}4{FIM_COR} - {azul}Criar um Novo Arquivo{FIM_COR}
        {verde}5{FIM_COR} - {azul}Ler Conteudo do Arquivo{FIM_COR}
        {verde}6{FIM_COR} - {azul}Sair do Sistema{FIM_COR}
        ''')
