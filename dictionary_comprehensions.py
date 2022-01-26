"""
Dictionary Comprehensions

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 5.88, 's']

Se quisermos criar uma tupla:

tupla = (1, 5.88, 's')

Se quisermos criar um set (conjunto):

set = {1, 5.88, 's'}

Se quisermos criar um dicionário:

set = {'a': 1, 'b': 5.88, 'c': 's'}

# Sintaxy

{chave:valor for valor in iterável}

# Exemplos:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave:valor ** 2 for chave,valor in numeros.items()}
print(quadrado)

numero = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor ** 2 for valor in numero}
print(quadrado)

chaves = 'abcdef'
valores = [1, 2, 5, 4, 7, 8]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

#  Exemplo com lógica condicional

valores = [1, 2, 5, 4, 7, 8]

par_impar = {num: ('par' if num % 2 == 0 else 'impar') for num in valores}
print(par_impar)
"""




