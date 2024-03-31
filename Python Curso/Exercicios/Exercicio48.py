# Cores
azul_underline = '\033[4;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Soma Dos Numeros Impares Multiplos De 3____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

soma_dos_numeros_impares_divisiveis_por_3 = 0
contador = 0

for numeros in range(1, 501):
    if numeros % 2 == 1 and numeros % 3 == 0:
        soma_dos_numeros_impares_divisiveis_por_3 += numeros
        contador += 1

print(f"Foram encontrados {verde}{contador}{FIM_COR} múltiplos ímpares de três "
      f"no intervalo de {verde}1{FIM_COR} a {verde}500{FIM_COR}, e soma entre todos eles é: "
      f"{azul_underline}{soma_dos_numeros_impares_divisiveis_por_3}{FIM_COR}")
