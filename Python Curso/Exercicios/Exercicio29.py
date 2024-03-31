print('\033[1;31m-=-\033[m' * 20)
print('\033[1;31;40m(_____Descobrindo se as Tres Retas Formam um Triangulo____)\033[m')
print('\033[1;31m-=-\033[m' * 20)

# Descobrindo a Velocidader do carro
velocidade_carro = int(input('Seu Veiculo estava em qual velociade? '))

# Quanto passou do limite permitido de 80Km/h
velocidade_acima_limite = float(velocidade_carro - 80)

# Valor da multa por cada Km acima do limite
valor_multa = float(7)

# Se for multado, Calculo do Valor da multa
multa = valor_multa * velocidade_acima_limite
if velocidade_carro > 80:
    print(f'Voce foi MULTADO! Excedeu o limite permitido de 80Km/h. Voce deve pagar uma multa de R${multa}')
else:
    print('Voce estava na velociade permitida! Tenha um Bom Dia!')
