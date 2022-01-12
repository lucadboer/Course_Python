"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmete ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
type([])

lista1 = [1, 55, 8, 95, 65, 4, 44, 21, 23, 54, 65, 88, 74, 65]

#  O Python separa cada string separadamente:'G', 'e', 'e' 'k'...

lista2 = list('Geek University')

lista3 = []

lista4 = list(range(11))

#  Podemos facilmente checar se determinado dado está contido na lista

num = 12
if num in lista4:
    print(f'Achei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#  Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de determinado valor em uma lista

print(lista1.count(65))
print(lista2.count('e'))

#  Adicionar elementos em listas


Para adicionar elementos ou valores em listas utilizamos a função append

OBS: Com "append" só é possível adicionar um elemento por vez


print(lista1)
lista1.append(12)
print(lista1)

#  Errado: lista1.append(12, 4, 15)
#  Certo:

lista1.append([5, 4, 2, 5, 8])  # Coloca o elemento lista como único [sublista]
print(lista1)

if [5, 4, 2, 5, 8] in lista1:
    print('Encontrei a lista!')
else:
    print('Lista não encontrada...')

lista1.extend([4, 55, 87, 100])  # Coloca cada elemento da lista como um valor adicional à lista
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do índice
#  Isso não substitui o valor inicial, o mesmo é deslocado para a direita
lista1.insert(5, 'COE')
print(lista1)

#  Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
#  lista1.extend(lista2)
print(lista1)

#  Podemos facilmente inverter uma lista

#  Forma 1:
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#  Forma 2:
print(lista1[::-1])
print(lista2[::-1])

#  Podemos copiar uma lista
lista7 = lista1.copy()
print(lista7)

#  Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

#  Podemos remover facilmente o último elemento de uma lista
#  OBS: O pop não somente remove o último elemento mas também retorna
print(lista1.pop())
print(lista1)

#  Podemos remover um elemento pelo índice
lista1.pop(1)
print(lista1)

#  Podemos remover todos os elementos (zerar a lista)
lista1.clear()
print(lista1)

#  Podemos facilmente repetir elementos de uma lista
nova = [1, 2, 3, 4, 5]
print(nova)

nova *= 3
print(nova)

#  Podemos facilmente converter uma string em uma lista
#  Exemplo 1:

nome = 'Heloisa Maria Ferreira coisa mais linda da minha vida'
print(nome)

nome = nome.split()
print(nome)

#  Exemplo 2:

nome2 = 'Heloisa,Maria,Ferreira,coisa,mais,linda,da,minha,vida'
print(nome2)
nome2 = nome2.split(',')
print(nome2)

#  Convertendo uma lista em string

listaH = ['Heloisa', 'Maria', 'Ferreira']
print(listaH)

#  Abaixo estamos falando: pega a lista e transforma em string colocando um espaço entre elas

lista_H_string = ' '.join(listaH)
print(lista_H_string)

#  Abaixo estamos falando: pega a lista e transforma em string colocando um $ entre elas

lista_H_string = '$'.join(listaH)
print(lista_H_string)
"""

type([])

lista1 = [1, 55, 8, 95, 65, 4, 44, 21, 23, 54, 65, 88, 74, 65]

#  O Python separa cada string separadamente:'G', 'e', 'e' 'k'...

lista2 = list('Geek University')

lista3 = []

lista4 = list(range(11))

#  Convertendo uma lista em string

listaH = ['Heloisa', 'Maria', 'Ferreira']
print(listaH)

#  Abaixo estamos falando: pega a lista e transforma em string colocando um espaço entre elas

lista_H_string = ' '.join(listaH)
print(lista_H_string)

#  Abaixo estamos falando: pega a lista e transforma em string colocando um $ entre elas

lista_H_string = '$'.join(listaH)
print(lista_H_string)









