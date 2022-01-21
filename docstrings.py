"""
Documentando funções com docstrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando
a prioridade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""

#  Exemplos

def diz_oi():
    """Uma função que retorna a string 'Oi!'"""
    return 'Oi!'



def exponencial(numero, potencia = 2):
    """
    Função que retorna por padrão o quadrade de um 'numero' à 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é o 2.
    :return: retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

print(exponencial(5))
