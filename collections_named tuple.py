"""
Modulo Collections - Named Tuple

#  Recap Tuple
tupla = (1, 2, 5, 6)
print(tupla[3])

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros

#  Fazendo Import
from collections import namedtuple

#  Precisamos definir o nome e parâmetros.

#  Forma 1:
cachorro = namedtuple('cachorro', 'idade raça nome')

#  Forma 2:
cachorro = namedtuple('cachorro', 'idade, raça, nome')

#  Forma 3:
cachorro = namedtuple('Cachorro', ['Idade', 'Raça', 'Nome'])

#  Usando
billiejoe = cachorro(Idade= 1.5, Raça= 'Shitzu', Nome='Billie Joe')
print(billiejoe)

#  Acessando dados:

#  Forma 1:
print(billiejoe[0])  # Idade
print(billiejoe[1])  # Raça
print(billiejoe[2])  # Nome

#  Forma 2:
print(billiejoe.Idade)  # Idade
print(billiejoe.Raça)  # Raça
print(billiejoe.Nome)  # Nome

print(billiejoe.index('Billie Joe'))

print(billiejoe.count('Billie Joe'))
"""

