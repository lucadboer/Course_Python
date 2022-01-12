"""
Loop -> Estrutura de Repetição
For  -> Uma dessas estruturas

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos iteráveis:

- String:
    nome = 'Geek University'
- Lista:
    lista = [1, 3, 5, 7, 9, 11]
- Range:
    numeros = range(1, 10)

# Exemplo de for 1:

for letra in nome:
    print(letra)

# Exemplo de for 2:

for numero in lista:
    print(numero)

# Exemplo de for 3:

for numero in range(1, 10):  # valor final não é incluso (-1)
    print(numero)

Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (2, 'U'), (...)

# Exemplo de enumerate 1:

for indice, letra in enumerate(nome):
    print(letra)

# Exemplo de enumerate 2:

for _, letra in enumerate(nome):  # Quando não precisamos de um valor podemos descartá-lo usando underline (_)
    print(letra)

# Exemplo de enumerate 3:

for indice, letra in enumerate(nome):
    print(letra[indice])

# Exemplo de enumerare 4

for valor in enumerate(nome):  # Imprime o índice e o valor do mesmo
    print(valor)

qtd = int(input('Quantos números vão ser digitados?'))
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'Informe o {n}/{qtd} '))
    soma += numero

print(f'A soma é {soma}')

nome = 'Geek University'
for i in nome:
    print(f'{i}', end='')  # Para não pular a linha utiliza o " end='' "

Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
for _ in range(1, qtd+1):
    for n in range(1, 10+1):
        print('\U0001F680' * n)

"""

num = 1

while num < 10:
    print(num)
    num = num + 1


