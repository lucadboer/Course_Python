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

#  Devemos utilizar tuplas SEMPRE que não serão alterados os dados contidos em uma coleção

meses = ('jan', 'fev', 'març', 'abril', 'maio', 'jun', 'jul', 'ago', 'sete', 'out', 'nov', 'dez')

print(meses)

#  O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[1])

#  Iterando com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

#  Verificando em qual índice está um elemento da tupla:
print(meses.index('març'))

#  Slicing tupla[inicio:fim:passo}

#  Exemplo 1:

print(meses[4::])

#  Devemos utilizar tuplas SEMPRE que não serão alterados os dados contidos em uma coleção

#  Por que utilizar tuplas?

#  - Tuplas são mais rápidas que listas
#  - Tuplas deixam seu código mais seguro

#  *Isso porque trabalhar com elementos imutáveis traz segurança para o código

#  Copiando uma tupla para outra

tupla = (1, 2, 3, 4)
print(tupla)

nova_tupla = tupla
print(tupla)
print(nova_tupla)

outra = (5, 6, 7, 8)
print(outra)

nova_tupla += outra
print(tupla)
print(nova_tupla)

#  Na tupla não temos o problema de shallow copy
"""

