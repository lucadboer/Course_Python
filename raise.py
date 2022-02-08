"""
Raise -> serve para alterar uma mensagem de erro, ou seja, você levanta a própria mensagem de
algum erro

Forma geral:

raise TipoDoErro('Mensagem de erro')

Exemplos
"""

def musicas(musica, album):
    album_lp = ['Crawling', 'In the End', 'Pepercut', 'By Myself']
    if type(musica) is not str:
        raise TypeError('O tipo de "muscia" precisa ser uma string')
    if type(album) is not str:
        raise TypeError('O tipo de "album" precisa ser uma string')


musicas('Pepercut', 'Hybrid Theory')


def musicas(musica, album):
    album_lp = ['Crawling', 'In the End', 'Pepercut', 'By Myself']
    if type(musica) is not str:
        raise TypeError('O tipo de "muscia" precisa ser uma string')
    if type(album) is not str:
        raise TypeError('O tipo de "album" precisa ser uma string')
    if musica not in album_lp:
        raise ValueError('O nome da música precisa estar dentro do album')
    print(f'A música {musica} está dentro do album {album}')


musicas('Numb', 'Hybrid Theory')