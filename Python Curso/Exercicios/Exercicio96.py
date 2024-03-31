# Cores
azul = '\033[1;34m'
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Título
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{" " * 10}{vermelho_fundo_preto}(_____Função Que Calcula Área____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

terreno = list()


def area():
    largura = float(input(f'LARGURA ({azul}m{FIM_COR}): '))
    comprimento = float(input(f'COMPRIMENTO ({azul}m{FIM_COR}):'))
    return {'largura': largura, 'comprimento': comprimento}


print('Controle de Terreno')
print(f'{azul}_{FIM_COR}' * 20)

info_terreno = area()
terreno.append(info_terreno)

area_terreno = info_terreno["largura"] * info_terreno["comprimento"]

print(f'{azul}_{FIM_COR}' * 20)
print(f'A area do terreno {verde}{info_terreno["largura"]}{FIM_COR}x{verde}{info_terreno["comprimento"]}{FIM_COR}'
      f' é de {azul_underline}{area_terreno:.2f}m²{FIM_COR}')

