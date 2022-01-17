"""
Mapas -> Conhecidos em Python como Dicionários

Dicionárops em Python é representado por {}

receita = {'janeiro': 800, 'fevereiro': 2000, 'março': 1500}
print(receita)

#  Iterar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi : {receita[chave]} R$')

#  Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#  Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

#  Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave}, Valor = {valor} R$')

#  Soma*, Valor máximo*, Valor mínimo*, Tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""




