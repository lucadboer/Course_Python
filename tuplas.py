"""
Tuplas - (Tuple)

Tuplas são basicamente parecida com listas

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação
em uma tupla gera uma nova tupla.

#  CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#  CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # É uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

#  Podemos concluir que tuplas são definidas pela vírgula e não o uso de ()

"""

