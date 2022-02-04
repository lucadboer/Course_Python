"""
Zip

Função -> Pega o primeiro elemento de cada coleção e junto em uma tupla formando pares.
"""

# Exemplos

x = 'abc'
y = 'abc'
z = 'abc'

print(list(zip(x, y, z)))  # Pegou o primeiro elemento de cada dado e formou pares

x1 = [1, 3, 5]
x2 = [2, 4, 6, 8]
x3 = [3, 5, 7, 9, 10]  # Adicionando mais elementos que as outras lista

print(list(zip(x1, x2, x3)))  # o Zip para nos valores da menor lista, e o que sobrar é descartado

notas1 = [50, 80, 98]
notas2 = [75, 40, 100]
alunos = ['Baiano', 'Luca', 'Heloisa']

print(list(zip(alunos, notas1, notas2)))

nota_max = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, notas1, notas2)}
print(nota_max)

nota_max2 = zip(alunos, map(lambda nota: max(nota), zip(notas1, notas2)))
print(dict(nota_max2))
