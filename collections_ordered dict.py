"""
Modulo Colletions - Ordered Dict

#  Em um dicionário a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave: {chave}  -  Valor: {valor}')

Ordered Dict -> É um dicionário que garante a ordem de inserção dos elementos

#  Fazendo o import
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dicionario)

res = (OrderedDict(dicionario))
for chave, valor in res.items():
    print(f'Chave: {chave}  -  Valor: {valor}')

#  Entendendo a difereça entre dict e Ordered Dict

#  Dicionários comuns:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True Já que a ordem dos elementos não importa, e sim o que está dentro das chaves

#  Ordered Dict:

dict1 = (OrderedDict(dict1))
dict2 = (OrderedDict(dict2))

print(dict2 == dict1)  # False Já que a ordem dos elementos importa para o Ordered Dict
"""





