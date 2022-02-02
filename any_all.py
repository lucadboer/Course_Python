"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any() -> Retorna True se qualquer dos elementos do iterável são verdadeiros, ou retorna false se o iterável está vazio.
"""

# Exemplos de all()

print(all([5, 6, 8, 7, 9, 2]))  # True

print(all([0, 1, 2, 3, 4, 5]))  # False

print(all([numeros for numeros in [1, 2, 3, 4, 5] if numeros % 2 == 1]))  # True

nomes = ['Calor', 'Carla', 'Charlie', 'Aassina']

print(all([nome[0] == 'C' for nome in nomes]))  # False

print(all([nome for nome in nomes if nome[0] == 'C']))  # True

# Exemplos de any()

print(any([0, 1, 2, 3, 4, 5]))  # True

print(any([numeros for numeros in [1, 3, 5] if numeros % 2 == 0]))  # False

print(any([0, False, [], {}, ()]))  # False

print(any([0, False, 2, [], {}, ()]))  # True

nomes = ['Heloisa', 'Carla', 'Charlie', 'Cassina']

print(any([nome[0] == 'C' for nome in nomes]))  # True


