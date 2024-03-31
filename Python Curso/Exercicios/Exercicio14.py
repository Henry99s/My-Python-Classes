print('=====Transformando Graus Celsius em Graus Fahrenheit=====')

# Encontrando o valor de graus Celsios, e calculo de Fahrenheint
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32

# Resultado
print('A temperatura de {0:.2f}°C corresponde a {1:.2f}ºF!'.format(c, f))
