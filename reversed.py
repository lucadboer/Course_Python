"""
Reversed -> inverte a ordem de um iterável

- Diferente do reverse() que só pode ser utilizado em listas, o reversed() serve para qualquer iterável

OBS: Apenas com um conjunto(set) que não é possível de inverter sua ordem, já que nele a ordem não importa
"""

# Exemplos

numeros = (1, 3, 5, 7, 9, 11)
"""É preciso transformar em alguma coleção para poder utilizar o resultado gerado pelo reversed(),
pois senão ele retornará apenas um objeto"""

print(tuple(reversed(numeros)))

print(numeros[::-1])  # Outra forma de inverter a ordem

moi = 'Heloisa Maria Ferreira'
print(list(reversed(moi)))  # Aqui deixou em strings separadas

print(''.join(reversed(moi)))  # Aqui deixou em apenas uma string

for n in reversed(numeros):
    print(n * 2, end=' ')

print('\n')

for x in range(50, -1, -5):
    print(x, end=' ')

