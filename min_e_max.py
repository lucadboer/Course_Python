"""
Min e Max

min() -> Mostra o menor valor entre os dados
max() -> Mostra o maior valor entre os dados
"""

# Exemplos

print(max(1, 4, 8, 99, 7, 4, 651, 5, 45, 455))
print(min(9, 4, 8, 99, 7, 4, 651, 5, 45, 455))

print(max('Heloisa Maria Ferreira'))  # Retorna o MAIOR valor da letra alfabética
print(min('HeloisaMariaFerreira'))  # Retorna o MENOR valor da letra alfabética

moi = ['Heloisa', 'Maria', 'Ferreira']  # Retorna o maior nome
print(max(moi, key=lambda nome: len(nome)))

moi = ['Heloisa', 'Maria', 'Ferreira']  # Retorna o menor nome
print(min(moi, key=lambda nome: len(nome)))

musicas = [
    {'título': 'Still Into You', 'tocou': 41},
    {'título': 'Californication', 'tocou': 15},
    {'título': 'The House Of Wolves', 'tocou': 8},
    {'título': 'Happier Than Ever', 'tocou': 13},
    {'título': 'In The Remains', 'tocou': 34}
]

print(musicas)

# Música mais tocada
print(max(musicas, key=lambda musica: musica['tocou']))

"""Mostrando só o título:"""
print(max(musicas, key=lambda musica: musica['tocou'])['título'])


# Música menos tocada
print(min(musicas, key=lambda musica: musica['tocou']))

"""Mostrando só o título:"""
print(min(musicas, key=lambda musica: musica['tocou'])['título'])




