"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas:
numeros = [5, 6.8, 'oi', True]
"""

#  Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(type(listas))

#  Como fazemos para acessar os dados?

print(listas[1][0])  # 4
print(listas[0][1])  # 2
print(listas[2][2])  # 9

#  Iterando com loops em uma lista aninhada
"""for list in listas:
    for num in list:
        print(num)
"""
# List Comprehensions

[[print(valor) for valor in list] for list in listas]

#  Gerando um tabuleiro/Matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for numero in range(1, 4)]
print(tabuleiro)

#  Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for numero in range(1, 4)]
print(velha)

#  Gerando valores iniciais

print([['*' for i in range(1, 4)]for j in range(1, 4)])
