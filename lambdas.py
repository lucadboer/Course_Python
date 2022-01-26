"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente lambdas, são funções sem nomes, ou seja
funções anônimas.

# Função em Python

def calcular(x):
    return 3 * x + 1

print(calcular(5))
print(calcular(10))

#  Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
cal = lambda x: 3 * x + 1

print(cal(5))
print(cal(10))

#  Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('Luca', 'Boer'))
print(nome_completo('Luca  ', ' BOER'))
print(nome_completo(' LUCa ', 'BoEr'))
print(nome_completo(' Luca ', ' Boer '))

#  Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

amor = lambda : 'Como não amar Python?'
print(amor())

uma = lambda x: 3 * x + 1
duas = lambda x, y: (3 * x + 1) * y
tres = lambda x, y, z: ((3 * x + 1) * y) / z

print(uma(5))
print(duas(5, 2))
print(tres(10, 20, 5))
# print(tres(10, 20, 5, 8))
# OBS: Se passarmos mais argumentos esperados ao parâmetro, teremos #TypeError

#  Outro exemplo

autores = ['Stephen King', 'J. K. Rowling', 'Breno Perrucho', 'Thiago Nigro', 'Orson Scot Hard',  'Arthur C. Clarke']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""

#  Função Quadrática
#  f(x) = a * x ** 2 + b * x + c

# Definindo função
def gerar_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = gerar_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(gerar_funcao_quadratica(2, 3, -5)(0))  # Maneira direta de realizar o cálculo da função
print(gerar_funcao_quadratica(2, 3, -5)(1))
print(gerar_funcao_quadratica(2, 3, -5)(2))








