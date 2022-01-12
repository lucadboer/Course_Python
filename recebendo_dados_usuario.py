"""
Recebendo dados do usuário
"""

#  Entrada de Dados

print("Qual o seu nome? ")
nome = input()

print('Seja bem-vindo(a) %s' % nome)

print("Qual a sua idade?")
idade = input()

#  Processamento


# Saída de Dados

print(f"O {nome} nasceu em {2022 - int(idade)}")

nome_moi = input('Qual o nome do seu momoi? ')

idade_momoi = int(input('E qual a idade dela? '))

print(f'Então o nome da sua princesa é {nome_moi}, e ela tem {idade_momoi} anos... Belíssimo')


