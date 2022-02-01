"""
Map

Com map fazemos mapeamento de valores para função
"""

import math

#  Utilizando map com lambda

raios = [5, 9, 7, 8.55, 69]

def teste():
    return print(list(map(lambda r: math.pi * (r ** 2), raios)))  # Utiliza cada dado da lista "raios" e executa na
# função lambda por meio do parâmetro "r"

print(teste())

# OBS: Após utilizar a função map(), o objeto da primeira utilização do resultado zera

# Exemplo 2

cidade_temperatura = [('Berlim', 20), ('São Paulo', 30), ('Japão', 24), ('Cidade do Alaska', -6)]

c_para_f = lambda c: (c[0], (9/5) * c[1] + 32)

print(list(map(c_para_f, cidade_temperatura)))

