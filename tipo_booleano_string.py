"""
Tipo Booleano

Álgebra Booleana, criada por Georgie Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial Maiúscula

Errado: true, false

Certo: True, False
"""

ativo = True

print(ativo)

"""
Operações Básicas:
"""

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, 
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)

logado = False

# Ou (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# E (and):

"""
Também é uma operação binária, ou seja, precisa de dois valores. Ambos os valores 
tem que ser verdadeiro.

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""

"""
Tipo String:

nome = 'Angelina Jolie'

print(nome.upper()) - todas as letras MAIÚSCULAS

print(nome.lower()) - todas as letras MINÚSCULAS

print(nome.split()) - transforma em uma LISTA de strings

nome = 'primeiro segundo terceiro quarto'

print(nome.split())

print(nome[0:8])  # -> Slice de tring.

print(nome[::])  # -> Comece do primeiro, vai até o último.

print(nome[::-1])  # -> Comece do primeiro, vai até o último e inverta.

print(nome.replace('e', 'i'))  # -> Trocar o primeiro dado pelo segundo
"""

