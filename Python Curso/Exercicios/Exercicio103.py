def ficha(jog, gol):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato")


nome = str(input("Qual o nome do Jogador? "))

if nome.strip() == '':
    nome = "<desconhecido>"

gols = str(input("Quantos gols ele marcou? "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)
