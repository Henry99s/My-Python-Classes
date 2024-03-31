nome = str(input('Qual o seu nome: ')).capitalize().strip()
if nome == 'Henrique':
    print('Que lindo nome!!!')

elif nome == 'Isabella' or nome == 'Sofia':
    print('Caraca!!! Esse e o nome mais bonito que ja vi na minha vida!')

else:
    print('Que nome normal...')

print(f'Tenha um bom dia, {nome}!')
