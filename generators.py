"""
Generator Expression

- Else serve principalmente para alocar menos memória no sistema, já que igual no map e filter, ele também
apaga os dados logo depois de gerar o PRIMEIRO resultado.

Na aula de any e all foram utilizados a seguinte sintaxe:
- print(all([nome[0] == 'C' for nome in nomes]))  # False

... Esse tipo de sintaxe usando list comprehension [] aloca muito mais memória no sistema do que se tivesse
utilizando um Generator

Como utilizar o Generator?
- Basta trocar os colchetes da lista por parêntes... Sim, formando uma tupla. Porém pode ser alterado qualquer
tipo de dado, seja uma lista, um Set, um dicionário. Basta trocar por parênteses formando uma tupla
"""
#  Exemplo

"""Importando a biblioteca para ler o tamanho dos dados"""
from sys import getsizeof

# Utilizando list comprehension

list_com = getsizeof([x * 10 for x in range(1000+1)])
print(f'Tamanho dos dados gerados na lista = {list_com} bytes')

# Utilizando Set

sett = getsizeof({x * 10 for x in range(1000+1)})
print(f'Tamanho dos dados gerados no Set = {sett} bytes')

# Utilizando dicionário

list_com = getsizeof({x: x * 10 for x in range(1000+1)})
print(f'Tamanho dos dados gerados no dicionário = {list_com} bytes')

# Utilizando Generator Expression

generator = getsizeof((x * 10 for x in range(1000+1)))
print(f'Tamanho dos dados gerados no Generator = {generator} bytes')

"""Percebe-se que ao utilizar um generator, economiza muita memória e processamento de dados do sistema"""

# Iterando sobre um Generator

gen = (x * 10 for x in range(100+1))

for num in gen:
    print(num)




