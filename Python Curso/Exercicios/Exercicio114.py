import urllib.request

# Cores
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print(f'{vermelho}Ouve um ERRO ao acessar o site!{FIM_COR}')

else:
    print(f'{verde}Site Acessado com sucesso!{FIM_COR}')
