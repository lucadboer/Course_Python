"""
Filter

filter() -> Função que serve para filtrar determinados dados, coleção.
"""

import statistics

idades = 4, 66, 5, 2, 31, 41, 4, 9, 6, 3, 5, 4, 12
print(f'Todas as idades {idades}')
media_idades = statistics.mean(idades) # Função "mean" da biblioteca statistics calcula a média de uma coleção de dados

print(f'Media das idades: {int(media_idades)}')

media_alta = filter(lambda idade: idade > media_idades, idades)
print(f'Media alta de idades: {list(media_alta)}')

media_baixa =  filter(lambda idade: idade < media_idades, idades)
print(f'Media baixa de idades: {list(media_baixa)}')

print(list(media_baixa))

paises_subdesenvolvidos = [' ', 'Brasil', 'Bolívia', '', 'Argentina', '', 'Grécia', 'Índia']
print(paises_subdesenvolvidos)

# Forma 1

# filtrar_paises = filter(lambda paises: len(paises) > 0 and paises != ' ', paises_subdesenvolvidos)
# print(list(filtrar_paises))

# Forma 2 - Simplificada

filtrar_paises = filter(None, paises_subdesenvolvidos)
print(list(filtrar_paises))

# Exemplo utilizando map e filter

musicas = ['', 'The Reason', 'Numb', 'RISE', '', 'Still Into You', '', 'A Prophecy']
print(musicas)

filter_musicas = map(lambda musica: f'{musica}', filter(lambda musica: musica != '' and len(musica) < 10 or len(musica) == 10, musicas))
print(list(filter_musicas))