print('====Quantos centimetro e milimetros tem x metros?====')

# Valor e calculos da medida
m = float(input('Escolha um valor: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

# Resultado
print('{0} metros tem, {1} quilometros, {2} hectometros, {3} decametros, {4} decimetros, {5} centimetro e {6} milimetros.'.format(m, km, hm, dam, dm, cm, mm))
