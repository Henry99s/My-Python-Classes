def voto(ano_de_nascimento):
    from datetime import date

    data_atual = date.today().year
    idade = data_atual - ano_de_nascimento

    if idade < 16:
        return print(f'Com a sua idade de {idade}, você NÃO VOTA nas eleições')

    elif 16 <= idade < 18 or idade >= 65:
        return print(f'Com a sua idade de {idade}, seu voto é OPCIONAL nas eleições')

    elif 18 <= idade < 65:
        return print(f'Com a sua idade de {idade}, seu voto é OBRIGATORIO nas eleições')


nasc = int(input("Em que ano voce nasceu? "))
voto(nasc)
