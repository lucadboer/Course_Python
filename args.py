"""
*Args é como se fosse uma tupla, ele simplifica o código, deixando ele mais limpo.
"""

def soma_valores(*args):
    """
    Função soma_valores pega os elementos de entrada do parâmetro args e faz uma soma dentre todos os valores
    :param args: transforma em uma tupla todos os elementos que entrarem na função
    :return: retorna a soma de todos os valores de args
    """
    return sum(args)  # Somando todos os valores entrados em arg

print(soma_valores(1, 2, 3, 4, 5, 6))

numeros = 5, 87, 564, 5.12, 54, 63, 5.22

print(soma_valores(*numeros))  # Utiliza-se o '*' antes de numeros para o python desempacotar a tupla e poder
# fazer operações com os valores dentro dela

# print(soma_valores(numeros))  # Caso não utilize o '*', será retornado TypeError pois o Python só reconhece
# 'numeros' como uma coleção e não como elementos distintos.

