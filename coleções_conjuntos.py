"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da Matemática.

- No Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armanezar elementos mas não nos importamos
com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (Sets) e mapas (dicionários) em Python:
    - Um dicionário tem {}: valor;
    - Um conjunto tem apenas valor;

#  Definindo um conjunto

#  Forma 1

s = set({1, 6, 4, 8, 3, 7, 9, 4})  # Repare que temos valores repetidos.

print(s)
print(type(s))

#  Ao criar um conjunto e tiver repetições de um elemento, o mesmo será ignorado
#  sem gerar erro e não fará parte do conjunto.

#  Forma 2 - Mais comum

s = {1, 6, 4, 8, 3, 7, 9, 4}
print(s)
print(type(s))

#  Podemos verificar se determinado elemento está contido no Set

if 5 in s:
    print('Achamos o valor')
else:
    print('Não foi encontrado...')

#  Importante lembrar que, além de não termos valores duplicados, não temos ordem.

#  Listas aceitam valores duplicados, fechando com 10 elementos
lista = [55, 6, 4, 2, 1, 6, 44, 8, 12, 8]
print(f'Lista: {lista}  -  Com {len(lista)} elementos')

#  tupla aceitam valores duplicados, fechando com 10 elementos
tupla = 55, 6, 4, 2, 1, 6, 44, 8, 12, 8
print(f'Tupla: {tupla}  -  Com {len(tupla)} elementos')

#  dict não aceitam chaves duplicadas, fechando com 8 elementos
dict = {}.fromkeys([55, 6, 4, 2, 1, 6, 44, 8, 12, 8], 'dict')
print(f'Dicionário: {dict}  -  Com {len(dict)} elementos')

#  Set aceitam não valores duplicados, fechando com 8 elementos
Set = {55, 6, 4, 2, 1, 6, 44, 8, 12, 8}
print(f'Set: {Set}  -  Com {len(Set)} elementos')

#  Assim como todo outro conjunto Python, podemos colocar tipos de qualquer dados misturados em Sets

#  Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes inforam manualmente
# a cidade de onde vieram

#  Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos
#  elementos e ter repetição.

cidades = ['Belo Horizonto', 'São Paulo', 'Campinas', 'Ribeirão Preto', 'São Paulo', 'Campinas']
print(cidades)
print(len(cidades))

#  Agora precisamos saber quantas cidades distintas temos:

#  Forma 1:

print(len(set(cidades)))

#  Métodos Conjuntos Matemáticos

# Imagine que temos dois conjuntos:
#   - Estudantes de Python
#   - Estudantes de Java

estudante_python = {'Marcos', 'Pedro', 'Olívia', 'Brup', 'Heloisa'}
estudante_java = {'Pedro', 'Laura', 'Jheniffer', 'Heloisa'}

#  Veja que alguns alunos estudaram duas linguagens
#  Precisamos gerar um conjunto com nomes únicos

# Forma 1:
uniao1 = estudante_python.union(estudante_java)
print(uniao1)
#  uniao1 = estudante_java.union(estudante_python)
# print(uniao1)

# Forma 2:
unicos2 = estudante_python | estudante_java
print(unicos2)

#  Veja que alguns alunos estudaram duas linguagens
#  Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1:
uniao1 = estudante_python.intersection(estudante_java)
print(uniao1)
#  unicos1 = estudante_java.intersection(estudante_python)
# print(uniao1)

# Forma 2:
unicos2 = estudante_python & estudante_java
print(unicos2)

#  Gerar um conjunto de estudantes que não estão em outo curso

# Forma 1:
so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)

#  Soma*, Valor máximo*, Valor mínimo*, Tamanho

conjunto = {1, 6, 4, 8, 9, 6, 3, 1, 11, 22}

print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))
"""







