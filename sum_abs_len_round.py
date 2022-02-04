"""
sum() -> Soma todos os elementos de um determinado iterável

abs() -> Retorna o valor absoluto de um número real ou int, ou seja, deixa qualquer valor no final positivo

len() -> Retorna o tamanho(quantidade de elementos dentro de um iterável) de uma determinada coleção

round -> Retorna o valor de um número int ou float arredondado
"""

# Exemplo 1 - sum()

xzinho = 1, 2, 3, 4, 5
print(xzinho)
print(sum(xzinho))
print(sum(xzinho, 5))  # Soma todos os valores do iterável e depois soma com o parâmetro "5" determinado
print(sum(xzinho, -5))  # Soma todos os valores do iterável e depois subtrai com o parâmetro "5" determinado

# Exemplo 2 - abs()
print('\n')

a = -1
b = -547
c = -5.554

print(abs(a))
print(abs(b))
print(abs(c))

# Exemplo 3 - len()
print('\n')

qtd = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100

print(len(qtd))

print(len([5, 4, 3]))

print(len('Heloisa Maria Ferreira'))  # O len() também conta os espaços de uma string

# Exemplo 4 - round()

print('\n')

print(round(7.54878, 2))
print(round(7.54878))
print(round(10.54878))
print(round(10.54878, 2))
print(round(-7.54878, 2))

print(abs(round(-7.54878, 2)))  # Exemplo utilizando abs()




