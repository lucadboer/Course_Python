"""
Módulo Collections Counter (contador)

Collections -> High-performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parãmetro e como valor a quantidade
de ocorrências desse elemento.

#  Realizando o Import

from collections import Counter

#  Exemplo 1

#  Podemos utilizar qualquer tipo de iterável
lista = [1, 1, 1, 2, 2, 3, 3, 3, 5, 8, 7, 7, 99, 99, 54, 54, 6, 6, 6]

#  Utilizando o Counter

res = Counter(lista)
print(type(res))
print(res)

# Counter: Counter({1: 3, 3: 3, 6: 3, 2: 2, 7: 2, 99: 2, 54: 2, 5: 1, 8: 1})

# Veja que para cada elemento da lista, ele criou uma chave e colocou o valor e a quantidade de ocorrências.

#  Exemplo 2

stringg = 'Geek University'

print(Counter(stringg))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

#  Exemplo 3

textao = """O Tesouro Selic funciona de forma simples. Você empresta dinheiro para recebê-lo de volta com juros. Como
ele é emitido pela instituição mais segura do país, que é o Governo Federal, e ainda possui uma ótima liquidez, o seu
rendimento sempre será próximo de 100% do CDI"""

palavras = textao.split()

res = Counter(palavras)
print(res)

#  Encotrando as 5 palavras com mais ocorrências

print(res.most_common(4))
"""



