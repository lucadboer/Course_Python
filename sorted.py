"""
Sorted

Tem a mesma função do sort, ou seja, de ordenar uma coleção de dados. Porém, o sort só pode ser usado
em uma lista, já o sorted pode ser usado em qualquer coleção de dados

OBS: O sorted gera uma nova lista, ou seja, ele não altera primitivamente a lista original que foi modificada
"""

# Exemplos:

tupla = 1, 4, 6, 8, 7, 2 ,5

print(sorted(tupla)) # Menor maior
print(sorted(tupla, reverse=True))  # Maior menor

musicas = [
    {'título': 'Still Into You', 'tocou': 41},
    {'título': 'Californication', 'tocou': 15},
    {'título': 'The House Of Wolves', 'tocou': 8},
    {'título': 'Happier Than Ever', 'tocou': 13},
    {'título': 'In The Remains', 'tocou': 34}
]

print(musicas)

# Ordem da menos tocada pra mais tocada
print(sorted(musicas, key=lambda musica: musica ['tocou']))

# Ordem da mais tocada pra menos tocada
print(sorted(musicas, key=lambda musica: musica ['tocou'], reverse=True))

# Ordem alfabética
print(sorted(musicas, key=lambda letra: letra ['título']))

# Ordem "desalfatética"
print(sorted(musicas, key=lambda letra: letra ['título'], reverse=True))