from time import sleep

# Cores
azul = '\033[1;34m'
vermelho = '\033[1;31m'
vermelho_fundo_preto = '\033[1;31;40m'
verde = '\033[1;32m'
FIM_COR = '\033[m'

# Titulo
print(f'{vermelho}-=-{FIM_COR}' * 20)
print(f'{vermelho_fundo_preto}(_____Analisador Completo____){FIM_COR}')
print(f'{vermelho}-=-{FIM_COR}' * 20)

# ----------------------------------------------------------------------------------------------------------------------

# Definindo estruturas de dados para armazenar informações.
pessoas = []


# Função para inserir dados de uma pessoa.
def dados_pessoa():
    nome = input("Escreva o nome: ").strip()
    idade = int(input("Digite a idade: "))
    genero = input("Digite o genero como (M/F): ").upper().strip()
    return {"nome": nome,
            "idade": idade,
            "genero": genero}


# Dados de entrada para 4 pessoas.
for i in range(4):
    print(f"Escreva as informações para a {verde}{i + 1}º{FIM_COR} pessoa:")
    pessoa = dados_pessoa()
    pessoas.append(pessoa)

# Caluculo da media de idade
total_idade = sum(pessoa["idade"] for pessoa in pessoas)
media_idade = total_idade / len(pessoas)

# Encontrando o homem mais velho.
homem_mais_velho = None
for pessoa in pessoas:
    if pessoa["genero"] == "M":
        if homem_mais_velho is None or pessoa["idade"] > homem_mais_velho["idade"]:
            homem_mais_velho = pessoa

# Contando o numero de mulheres abaixo de 20 anos.
mulheres_abaixo_de_20 = sum(1 for pessoa in pessoas if pessoa["genero"] == 'F' and pessoa["idade"] < 20)

# Computador processando
print('\033[4;34mPROCESSANDO...\033[m')
sleep(2)

# Resultado da media de idade
print(f'A média de idade deste grupo é: {azul}{media_idade:.1f}{FIM_COR} anos')

# Resultado do homem mais velho da lista.
if homem_mais_velho:
    print(f'O homem mais velho da lista é: {verde}{homem_mais_velho["nome"]}{FIM_COR}')
else:
    print(f'{vermelho}Não tem homens na lista!{FIM_COR}')

# Resultado do numeros de mulheres abaixo de 20 anos na lista.
if mulheres_abaixo_de_20 >= 1:
    print(f'O numeros de mulheres na lista acima de {verde}20{FIM_COR} anos é: {azul}{mulheres_abaixo_de_20}{FIM_COR}')
else:
    print(f'{vermelho}Não tem mulheres abaixo de 20 anos na lista!{FIM_COR}')
